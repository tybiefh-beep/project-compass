#!/usr/bin/env python3
"""
图片转文本分析工具 — 纯标准库，无需安装依赖。
依赖 macOS 的 sips 命令做缩放，Python 标准库解析 PNG。

用法:
  python3 img2text.py <图片路径> [宽度] [--color] [--regions]

  python3 img2text.py screenshot.png          # 默认 120 字符宽
  python3 img2text.py screenshot.png 160      # 160 字符宽
  python3 img2text.py screenshot.png --color  # ANSI 彩色输出
  python3 img2text.py screenshot.png --regions # 分析各区域颜色
"""

import struct, zlib, subprocess, sys, os, tempfile


def resize_with_sips(src_path, max_w, max_h):
    """用 macOS sips 缩放图片，返回临时 PNG 路径"""
    tmp = tempfile.mktemp(suffix='.png')
    subprocess.run(
        ['sips', '-z', str(max_h), str(max_w), src_path, '--out', tmp],
        capture_output=True, check=True
    )
    return tmp


def parse_png(filepath):
    """解析 PNG 文件，返回 (width, height, raw_pixels_rgba)"""
    with open(filepath, 'rb') as f:
        data = f.read()

    # 找 IHDR
    idx = data.find(b'IHDR')
    if idx < 0:
        raise ValueError("不是有效的 PNG 文件")
    w = struct.unpack('>I', data[idx+4:idx+8])[0]
    h = struct.unpack('>I', data[idx+8:idx+12])[0]

    # 收集所有 IDAT 数据
    idat_data = b''
    pos = 0
    while True:
        idx = data.find(b'IDAT', pos)
        if idx < 0:
            break
        length = struct.unpack('>I', data[idx-4:idx])[0]
        idat_data += data[idx+4:idx+4+length]
        pos = idx + 4 + length

    raw = zlib.decompress(idat_data)

    # 重建像素行（每行有 filter byte + w*4 bytes RGBA）
    stride = 1 + w * 4
    pixels = []
    for y in range(h):
        filt = raw[y * stride]
        row = raw[y * stride + 1:y * stride + stride]
        # 处理 filter（只处理 type 0 = None，绝大多数截图都是）
        if filt == 0:
            pixels.append(row)
        elif filt == 1:  # Sub
            prev = [0, 0, 0, 0]
            decoded = bytearray()
            for i in range(0, len(row), 4):
                r = (row[i] + prev[0]) & 0xFF
                g = (row[i+1] + prev[1]) & 0xFF
                b = (row[i+2] + prev[2]) & 0xFF
                a = (row[i+3] + prev[3]) & 0xFF
                decoded.extend([r, g, b, a])
                prev = [r, g, b, a]
            pixels.append(bytes(decoded))
        else:
            # 其他 filter 类型极罕见，按 None 处理
            pixels.append(row)

    return w, h, pixels


def brightness(r, g, b):
    """感知亮度（加权）"""
    return 0.299 * r + 0.587 * g + 0.114 * b


def to_ascii(pixels, w, h, use_color=False):
    """像素转 ASCII 文本"""
    # 从暗到亮的字符
    if use_color:
        # ANSI 真彩色输出
        lines = []
        for y in range(h):
            line = ''
            for x in range(w):
                r = pixels[y][x*4]
                g = pixels[y][x*4+1]
                b = pixels[y][x*4+2]
                brt = brightness(r, g, b)
                if brt < 30:
                    ch = ' '
                elif brt < 70:
                    ch = '\033[38;2;60;60;55m█\033[0m'
                elif brt < 110:
                    ch = '\033[38;2;100;100;90m▓\033[0m'
                elif brt < 160:
                    ch = '\033[38;2;150;150;140m▒\033[0m'
                elif brt < 210:
                    ch = '\033[38;2;200;200;195m░\033[0m'
                else:
                    ch = ' '
                line += ch
            lines.append(line)
        return '\n'.join(lines)
    else:
        chars = ' ░▒▓█'
        lines = []
        for y in range(h):
            row = pixels[y]
            line = ''
            for x in range(w):
                r = row[x*4]
                g = row[x*4+1]
                b = row[x*4+2]
                brt = brightness(r, g, b)
                idx = min(int(brt / 51), 4)
                line += chars[idx]
            lines.append(line)
        return '\n'.join(lines)


def analyze_regions(pixels, img_w, img_h):
    """分析 UI 关键区域的颜色"""
    # 侧边栏（左 15%）
    sb_x1, sb_x2 = 0, int(img_w * 0.15)
    # 主区域（50%）
    main_x1, main_x2 = int(img_w * 0.3), int(img_w * 0.7)
    main_y1, main_y2 = int(img_h * 0.3), int(img_h * 0.6)
    # 输入区（底部 10%）
    inp_y1, inp_y2 = int(img_h * 0.9), img_h - 1
    inp_x1, inp_x2 = int(img_w * 0.3), int(img_w * 0.7)
    # 顶栏
    top_y1, top_y2 = 0, int(img_h * 0.05)

    def avg_rgb(x1, x2, y1, y2):
        rs, gs, bs, count = 0, 0, 0, 0
        for y in range(max(0,y1), min(img_h,y2)):
            row = pixels[y]
            for x in range(max(0,x1), min(img_w,x2)):
                rs += row[x*4]
                gs += row[x*4+1]
                bs += row[x*4+2]
                count += 1
        if count == 0: return (0,0,0)
        return (rs//count, gs//count, bs//count)

    regions = {
        '侧边栏(左15%)': (sb_x1, sb_x2, 0, img_h),
        '主区域中央': (main_x1, main_x2, main_y1, main_y2),
        '输入区(底部)': (inp_x1, inp_x2, inp_y1, inp_y2),
        '顶栏': (int(img_w*0.2), int(img_w*0.8), top_y1, top_y2),
    }

    print(f'图片尺寸: {img_w}x{img_h}')
    print()
    for name, (x1, x2, y1, y2) in regions.items():
        r, g, b = avg_rgb(x1, x2, y1, y2)
        brt = brightness(r, g, b)
        label = '暗' if brt < 50 else '较暗' if brt < 100 else '中等' if brt < 150 else '较亮' if brt < 200 else '亮'
        print(f'{name}: RGB({r},{g},{b}) 亮度{brt:.0f} [{label}]')


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    src = sys.argv[1]
    if not os.path.exists(src):
        print(f'文件不存在: {src}')
        sys.exit(1)

    args = sys.argv[2:]
    use_color = '--color' in args
    show_regions = '--regions' in args

    # 目标宽度
    target_w = 120
    for a in args:
        if a.isdigit():
            target_w = int(a)
            break

    # 缩放：宽度 = target_w，高度按比例
    # 先用 sips 获取原始尺寸
    info = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', src],
                         capture_output=True, text=True).stdout
    import re
    ow = int(re.search(r'pixelWidth: (\d+)', info).group(1))
    oh = int(re.search(r'pixelHeight: (\d+)', info).group(1))
    target_h = int(oh * target_w / ow)
    # 限制最大高度
    max_h = 80
    if target_h > max_h:
        target_w = int(ow * max_h / oh)
        target_h = max_h

    tmp = resize_with_sips(src, target_w, target_h)
    try:
        w, h, pixels = parse_png(tmp)

        if show_regions:
            analyze_regions(pixels, w, h)
            print()

        # 输出 ASCII
        art = to_ascii(pixels, w, h, use_color)
        print(art)
    finally:
        os.remove(tmp)


if __name__ == '__main__':
    main()
