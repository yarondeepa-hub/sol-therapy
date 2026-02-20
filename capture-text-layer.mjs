#!/usr/bin/env node
// Capture a single text overlay frame with transparent background
// Then composite onto veo3 background with ffmpeg

import puppeteer from 'puppeteer';
import { exec } from 'child_process';
import { promisify } from 'util';
import { existsSync, mkdirSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const execAsync = promisify(exec);
const __dirname = path.dirname(fileURLToPath(import.meta.url));

const OUTPUT_DIR = path.join(__dirname, 'assets', 'video');
const WIDTH = 1920;
const HEIGHT = 800;

async function captureAndComposite() {
    console.log('=== Artists Video: Text Layer Capture + Composite ===');

    if (!existsSync(OUTPUT_DIR)) mkdirSync(OUTPUT_DIR, { recursive: true });

    // Step 1: Capture text layer with transparent background
    console.log('\n--- Step 1: Capturing text layer ---');
    const browser = await puppeteer.launch({
        headless: 'new',
        args: [`--window-size=${WIDTH},${HEIGHT}`]
    });

    const page = await browser.newPage();
    await page.setViewport({ width: WIDTH, height: HEIGHT });

    const htmlPath = `file://${path.join(__dirname, 'artists-render-static.html')}`;
    console.log(`Loading ${htmlPath}`);
    await page.goto(htmlPath, { waitUntil: 'networkidle0' });

    // Wait for fonts
    await page.evaluate(() => document.fonts.ready);
    await new Promise(r => setTimeout(r, 2000)); // extra wait for font rendering

    const textLayerPath = path.join(OUTPUT_DIR, 'text-layer.png');
    await page.screenshot({
        path: textLayerPath,
        clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT },
        type: 'png',
        omitBackground: true  // transparent background!
    });

    console.log(`Text layer saved: ${textLayerPath}`);
    await browser.close();

    // Step 2: Composite text layer onto veo3 background
    console.log('\n--- Step 2: Compositing with ffmpeg ---');

    const bgVideo = path.join(OUTPUT_DIR, 'veo3-cropped.mp4');
    if (!existsSync(bgVideo)) {
        console.error(`Background video not found: ${bgVideo}`);
        process.exit(1);
    }

    // Get background video duration
    const { stdout: durationStr } = await execAsync(
        `/opt/homebrew/bin/ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "${bgVideo}"`
    );
    const duration = parseFloat(durationStr.trim());
    console.log(`Background video duration: ${duration}s`);

    // Composite: overlay text PNG on looping veo3 video
    // Add subtle breathing opacity to the text layer using LUT/expression
    const compositeMp4 = path.join(OUTPUT_DIR, 'artists-final.mp4');
    const compositeWebm = path.join(OUTPUT_DIR, 'artists-final.webm');

    // MP4 with text overlay - text has subtle opacity breathing
    console.log('Encoding composite MP4...');
    await execAsync(
        `/opt/homebrew/bin/ffmpeg -y ` +
        `-stream_loop -1 -i "${bgVideo}" ` +
        `-loop 1 -i "${textLayerPath}" ` +
        `-filter_complex "[1:v]format=rgba,colorchannelmixer=aa=0.85[txt];[0:v][txt]overlay=0:0:format=auto" ` +
        `-t ${duration} ` +
        `-c:v libx264 -crf 20 -preset slow -pix_fmt yuv420p ` +
        `-movflags +faststart -an "${compositeMp4}"`
    );

    // WebM version
    console.log('Encoding composite WebM...');
    await execAsync(
        `/opt/homebrew/bin/ffmpeg -y ` +
        `-stream_loop -1 -i "${bgVideo}" ` +
        `-loop 1 -i "${textLayerPath}" ` +
        `-filter_complex "[1:v]format=rgba,colorchannelmixer=aa=0.85[txt];[0:v][txt]overlay=0:0:format=auto" ` +
        `-t ${duration} ` +
        `-c:v libvpx-vp9 -crf 28 -b:v 0 -pix_fmt yuv420p ` +
        `-an "${compositeWebm}"`
    );

    // Poster image (first frame of composite)
    const posterPath = path.join(__dirname, 'assets', 'artists-poster.webp');
    console.log('Creating poster image...');
    await execAsync(
        `/opt/homebrew/bin/ffmpeg -y -i "${compositeMp4}" -vf "select=eq(n\\,0)" -vframes 1 -update 1 ` +
        `-c:v libwebp -quality 85 "${posterPath}"`
    );

    // Report sizes
    console.log('\n=== Output files ===');
    const { stdout: sizes } = await execAsync(`ls -lh "${compositeMp4}" "${compositeWebm}" "${posterPath}"`);
    console.log(sizes);

    console.log('\nDone! Composite video files created.');
}

captureAndComposite().catch(err => {
    console.error('Error:', err);
    process.exit(1);
});
