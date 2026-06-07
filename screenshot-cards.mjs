import puppeteer from 'puppeteer';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, '小红书素材_Claude技能生成器.html');
const outDir = path.join(__dirname, '卡片截图');
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir);

const browser = await puppeteer.launch({ headless: true });
const page = await browser.newPage();
await page.setViewport({ width: 600, height: 900, deviceScaleFactor: 2 });
await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });

const cardLabels = ['01-封面图', '02-功能介绍', '03-使用流程', '04-知识速查', '05-结尾CTA'];
const cards = await page.$$('.card');

for (let i = 0; i < cards.length; i++) {
  const filename = `${cardLabels[i]}.png`;
  await cards[i].screenshot({ path: path.join(outDir, filename) });
  console.log(`✅ ${filename}`);
}

await browser.close();
console.log('\n全部完成，文件在: ' + outDir);
