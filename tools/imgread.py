#!/usr/bin/env python3
"""
图片分析统一工具 — OCR + 颜色 + 布局
用法: python3 imgread.py <图片路径>
"""

import subprocess, sys, os, tempfile, struct, zlib, re, json


def run_ocr(img_path):
    """Swift Vision OCR"""
    script = os.path.join(os.path.dirname(__file__), 'imgocr.swift')
    try:
        out = subprocess.run(
            ['swift', script, img_path],
            capture_output=True, text=True, timeout=25
        )
        if out.returncode == 0:
            return out.stdout.strip()
        return f'OCR 失败: {out.stderr[:200]}'
    except Exception as e:
        return f'OCR 异常: {e}'


def color_analysis(img_path):
    """用 sips 缩放后采样颜色"""
    tmp = tempfile.mktemp(suffix='.png')
    # 获取原图尺寸
    info = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', img_path],
                          capture_output=True, text=True).stdout
    ow = int(re.search(r'pixelWidth: (\d+)', info).group(1))
    oh = int(re.search(r'pixelHeight: (\d+)', info).group(1))
    # 缩放到结构分析尺寸
    tw, th = 200, 100
    subprocess.run(['sips', '-z', str(th), str(tw), img_path, '--out', tmp],
                   capture_output=True, check=True)

    with open(tmp, 'rb') as f:
        data = f.read()
    os.remove(tmp)

    idx = data.find(b'IHDR')
    w = struct.unpack('>I', data[idx+4:idx+8])[0]
    h = struct.unpack('>I', data[idx+8:idx+12])[0]

    idat_data = b''
    pos = 0
    while True:
        idx = data.find(b'IDAT', pos)
        if idx < 0: break
        length = struct.unpack('>I', data[idx-4:idx])[0]
        idat_data += data[idx+4:idx+4+length]
        pos = idx + 4 + length
    raw = zlib.decompress(idat_data)
    stride = 1 + w * 4
    pixels = []
    for y in range(h):
        pixels.append(raw[y*stride+1:y*stride+stride])

    def avg_region(x1p, x2p, y1p, y2p):
        x1, x2 = int(w*x1p), int(w*x2p)
        y1, y2 = int(h*y1p), int(h*y2p)
        rs, gs, bs, n = 0, 0, 0, 0
        for y in range(max(0,y1), min(h,y2)):
            r = pixels[y]
            for x in range(max(0,x1), min(w,x2)):
                rs += r[x*4]; gs += r[x*4+1]; bs += r[x*4+2]; n += 1
        if n == 0: return (0,0,0)
        return (rs//n, gs//n, bs//n)

    def to_hex(rgb):
        return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

    regions = {
        '侧边栏背景': (0.02, 0.12, 0.2, 0.5),
        '侧边栏文字区': (0.02, 0.12, 0.2, 0.15),
        '主区域背景': (0.5, 0.5, 0.6, 0.6),
        '聊天气泡': (0.35, 0.35, 0.65, 0.45),
        '输入区背景': (0.3, 0.92, 0.7, 0.98),
        '输入框内部': (0.35, 0.93, 0.65, 0.96),
        '顶栏': (0.3, 0.02, 0.7, 0.06),
        '底栏': (0.3, 0.90, 0.7, 0.93),
    }

    print(f'图片尺寸: {ow}x{oh}')
    print()
    print('=== 颜色分析 ===')
    for name, coords in regions.items():
        r, g, b = avg_region(*coords)
        lum = 0.299*r + 0.587*g + 0.114*b
        print(f'{name}: {to_hex((r,g,b))} 亮度{lum:.0f}')

    # ASCII 预览
    print()
    print('=== 布局预览 ===')
    chars = ' ░▒▓█'
    for y in range(h):
        line = ''
        for x in range(w):
            r, g, b = pixels[y][x*4], pixels[y][x*4+1], pixels[y][x*4+2]
            brt = (r + g + b) / 3
            idx = min(int(brt / 51), 4)
            line += chars[idx]
        print(line)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f'文件不存在: {path}')
        sys.exit(1)

    # 颜色分析
    color_analysis(path)

    # OCR
    print()
    print('=== OCR 文字识别 ===')
    ocr = run_ocr(path)
    print(ocr)


if __name__ == '__main__':
    main()
