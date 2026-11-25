// make.fun news-image-20261124: "Sum up 24 November's world news in one image".
// The front page is drawn ahead of time by tools/build.py + tools/render.ps1 into entry.png. The grader runs
// this program with no network, twice, and both runs must write the same bytes, so all it does is check that
// file and copy it, unchanged, to the output directory.
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const png = readFileSync(new URL('./entry.png', import.meta.url));

// The contest takes one whole PNG or JPEG of at most 1 MiB and 1024 x 1024 pixels. Check the file before
// writing it, so a bad render fails here, loudly, instead of reaching the gate as an invalid entry.
const PNG_MAGIC = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
if (!PNG_MAGIC.every((b, i) => png[i] === b)) throw new Error('entry.png is not a PNG file');
if (png.length > 1024 * 1024) throw new Error(`entry.png is ${png.length} bytes; the cap is 1 MiB`);
const width = png.readUInt32BE(16);
const height = png.readUInt32BE(20);
if (width > 1024 || height > 1024) throw new Error(`entry.png is ${width}x${height}; the cap is 1024x1024`);
if (png.subarray(png.length - 8, png.length - 4).toString('latin1') !== 'IEND') {
  throw new Error('entry.png is cut short: it does not end with its IEND chunk');
}

const dir = process.env.MAKEFUN_OUTPUT_DIR || '/output';
mkdirSync(dir, { recursive: true });
writeFileSync(join(dir, 'entry.png'), png);
console.log(`wrote ${join(dir, 'entry.png')} (${width}x${height}, ${png.length} bytes)`);
