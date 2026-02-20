#!/usr/bin/env node
// Capture animation frames from artists-render.html using Puppeteer
// Then assemble into video with ffmpeg

import puppeteer from 'puppeteer';
import { exec } from 'child_process';
import { promisify } from 'util';
import { existsSync, mkdirSync, readdirSync, unlinkSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const execAsync = promisify(exec);
const __dirname = path.dirname(fileURLToPath(import.meta.url));

const FRAMES_DIR = path.join(__dirname, 'frames-tmp');
const OUTPUT_DIR = path.join(__dirname, 'assets', 'video');
const FPS = 24;
const DURATION_SECONDS = 8;
const TOTAL_FRAMES = FPS * DURATION_SECONDS; // 192 frames
const WIDTH = 1920;
const HEIGHT = 800;

async function captureFrames() {
    console.log('=== Artists Animation Frame Capture ===');
    console.log(`FPS: ${FPS}, Duration: ${DURATION_SECONDS}s, Total frames: ${TOTAL_FRAMES}`);

    // Ensure directories
    if (!existsSync(FRAMES_DIR)) mkdirSync(FRAMES_DIR, { recursive: true });
    if (!existsSync(OUTPUT_DIR)) mkdirSync(OUTPUT_DIR, { recursive: true });

    // Clean previous frames
    const oldFrames = readdirSync(FRAMES_DIR).filter(f => f.endsWith('.png'));
    for (const f of oldFrames) unlinkSync(path.join(FRAMES_DIR, f));

    console.log('Launching browser...');
    const browser = await puppeteer.launch({
        headless: 'new',
        args: [`--window-size=${WIDTH},${HEIGHT}`]
    });

    const page = await browser.newPage();
    await page.setViewport({ width: WIDTH, height: HEIGHT });

    const htmlPath = `file://${path.join(__dirname, 'artists-render.html')}`;
    console.log(`Loading ${htmlPath}`);
    await page.goto(htmlPath, { waitUntil: 'networkidle0' });

    // Wait for fonts to load
    await page.evaluate(() => document.fonts.ready);
    await new Promise(r => setTimeout(r, 1000)); // extra wait for font rendering

    console.log(`Capturing ${TOTAL_FRAMES} frames...`);
    const frameInterval = 1000 / FPS; // ms per frame

    for (let i = 0; i < TOTAL_FRAMES; i++) {
        const frameNum = String(i).padStart(4, '0');
        const framePath = path.join(FRAMES_DIR, `frame_${frameNum}.png`);

        // Set animation time by pausing all animations and seeking
        await page.evaluate((time) => {
            document.getAnimations().forEach(anim => {
                anim.currentTime = time;
            });
        }, i * frameInterval);

        await page.screenshot({
            path: framePath,
            clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT },
            type: 'png'
        });

        if (i % 48 === 0) {
            console.log(`  Frame ${i + 1}/${TOTAL_FRAMES} (${Math.round((i / TOTAL_FRAMES) * 100)}%)`);
        }
    }

    console.log('All frames captured. Closing browser.');
    await browser.close();

    // Assemble with ffmpeg
    console.log('\n=== Assembling video with ffmpeg ===');

    const framesPattern = path.join(FRAMES_DIR, 'frame_%04d.png');

    // WebM (VP9) - primary
    const webmOutput = path.join(OUTPUT_DIR, 'artists-loop.webm');
    console.log('Encoding WebM (VP9)...');
    await execAsync(
        `/opt/homebrew/bin/ffmpeg -y -framerate ${FPS} -i "${framesPattern}" ` +
        `-c:v libvpx-vp9 -crf 32 -b:v 0 -pix_fmt yuv420p ` +
        `-an "${webmOutput}"`
    );

    // MP4 (H.264) - fallback
    const mp4Output = path.join(OUTPUT_DIR, 'artists-loop.mp4');
    console.log('Encoding MP4 (H.264)...');
    await execAsync(
        `/opt/homebrew/bin/ffmpeg -y -framerate ${FPS} -i "${framesPattern}" ` +
        `-c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p ` +
        `-movflags +faststart -an "${mp4Output}"`
    );

    // Also create a poster image (first frame)
    const posterOutput = path.join(__dirname, 'assets', 'artists-poster.webp');
    console.log('Creating poster image...');
    await execAsync(
        `/opt/homebrew/bin/ffmpeg -y -i "${path.join(FRAMES_DIR, 'frame_0000.png')}" ` +
        `-c:v libwebp -quality 85 "${posterOutput}"`
    );

    // Report sizes
    const { stdout: sizes } = await execAsync(`ls -lh "${webmOutput}" "${mp4Output}" "${posterOutput}"`);
    console.log('\n=== Output files ===');
    console.log(sizes);

    console.log('\nDone! Video files created at:');
    console.log(`  WebM: ${webmOutput}`);
    console.log(`  MP4:  ${mp4Output}`);
    console.log(`  Poster: ${posterOutput}`);
}

captureFrames().catch(err => {
    console.error('Error:', err);
    process.exit(1);
});
