# CTO Handoff - Round 2 Revision: Code Examples for Phases 2-3

> **AGENT:** CTO
> **STATUS:** complete
> **MERGE_KEY:** code_examples_phase2_3
> **ROUND:** 2 (Gatekeeper revision)
> **DEPENDENCIES_SATISFIED:** [report_update, gatekeeper_re_review]

---

## 1. Film Grain / Noise Shader (Three.js Post-Processing)

Animated film grain overlay for Sol Therapy's sumi-e illustrations - "living paper" feel.

```html
<!--
  FILM GRAIN POST-PROCESSING PASS - Three.js
  Overlays animated noise on any Three.js scene.
  Inspired by aroke01.com's textural aesthetic.
  For Sol Therapy: use over sumi-e illustrations to create "living paper" effect.

  Dependencies: Three.js r160+ (ES module)
  Usage: Drop this into any page with an existing Three.js scene,
         or use standalone to overlay grain on a static background.
-->

<div id="grain-canvas" style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999;"></div>

<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js"
  }
}
</script>

<script type="module">
import * as THREE from 'three';

// --- VERTEX SHADER ---
// Simple fullscreen quad - passes UVs to fragment shader
const vertexShader = `
  varying vec2 vUv;
  void main() {
    vUv = uv;
    gl_Position = vec4(position, 1.0);
  }
`;

// --- FRAGMENT SHADER ---
// Animated film grain with controllable intensity
const fragmentShader = `
  precision highp float;

  varying vec2 vUv;
  uniform float uTime;
  uniform float uIntensity;   // 0.0 = no grain, 1.0 = full grain
  uniform vec2 uResolution;

  // Pseudo-random hash function - fast, good distribution
  float hash(vec2 p) {
    vec3 p3 = fract(vec3(p.xyx) * 0.1031);
    p3 += dot(p3, p3.yzx + 33.33);
    return fract((p3.x + p3.y) * p3.z);
  }

  void main() {
    // Scale UV to pixel coordinates for per-pixel grain
    vec2 pixelCoord = vUv * uResolution;

    // Time-varying seed creates animation
    // Floor to 24fps equivalent for filmic feel (not smooth - chunky like real film)
    float timeSeed = floor(uTime * 24.0) / 24.0;

    // Generate noise value per pixel, seeded by time
    float noise = hash(pixelCoord + timeSeed * 100.0);

    // Center noise around 0.5 and apply intensity
    // This means grain brightens AND darkens, like real film
    float grain = (noise - 0.5) * uIntensity;

    // Output: semi-transparent white/black based on grain value
    // Positive grain = white speck, negative = dark speck
    float alpha = abs(grain) * 0.6;  // 0.6 caps max opacity
    float luminance = grain > 0.0 ? 1.0 : 0.0;

    gl_FragColor = vec4(vec3(luminance), alpha);
  }
`;

// --- SETUP ---
const container = document.getElementById('grain-canvas');
const renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
container.appendChild(renderer.domElement);

// Fullscreen quad: plane geometry from -1 to 1 in clip space
const geometry = new THREE.PlaneGeometry(2, 2);
const material = new THREE.ShaderMaterial({
  vertexShader,
  fragmentShader,
  uniforms: {
    uTime: { value: 0.0 },
    uIntensity: { value: 0.08 },       // <-- ADJUST THIS: 0.03 = subtle, 0.15 = heavy
    uResolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) }
  },
  transparent: true,
  depthTest: false,
  depthWrite: false
});

const scene = new THREE.Scene();
const camera = new THREE.Camera(); // No-op camera - vertex shader handles positioning
scene.add(new THREE.Mesh(geometry, material));

// --- ANIMATION LOOP ---
const clock = new THREE.Clock();

function animate() {
  requestAnimationFrame(animate);
  material.uniforms.uTime.value = clock.getElapsedTime();
  renderer.render(scene, camera);
}
animate();

// --- RESPONSIVE ---
window.addEventListener('resize', () => {
  renderer.setSize(window.innerWidth, window.innerHeight);
  material.uniforms.uResolution.value.set(window.innerWidth, window.innerHeight);
});

// --- PUBLIC API (optional) ---
// Access from console or other scripts:
// window.grainControl.setIntensity(0.12)
window.grainControl = {
  setIntensity: (val) => { material.uniforms.uIntensity.value = val; },
  getIntensity: () => material.uniforms.uIntensity.value,
  pause: () => { clock.stop(); },
  resume: () => { clock.start(); }
};
</script>
```

**Key decisions:**
- 24fps grain stepping (not smooth) mimics real film stock - matches aroke01's analog aesthetic
- Overlay mode with `pointer-events:none` - layers on top of anything without blocking interaction
- `uIntensity: 0.08` is the sweet spot for "barely there, but alive" - Sol Therapy's paper feel
- Uses `alpha: true` on renderer so grain composites naturally over page content

---

## 2. View Transitions API - Page Transitions

Smooth cross-document page transitions for Sol Therapy's multi-page site. Modern browsers get cinematic crossfade + directional slide. Older browsers get instant navigation (no breakage).

```css
/* === VIEW TRANSITIONS - CSS ===
   Add this to your global stylesheet (e.g., base.css)
   Works for multi-page (MPA) navigation between same-origin pages.
   Both the source and destination pages must include this CSS. */

/* --- Step 1: Opt in to cross-document transitions --- */
@view-transition {
  navigation: auto;
}

/* --- Step 2: Default crossfade (applies to all navigations) --- */
::view-transition-old(root) {
  animation: sol-fade-out 0.4s ease-out both;
}
::view-transition-new(root) {
  animation: sol-fade-in 0.4s ease-in both;
}

@keyframes sol-fade-out {
  from { opacity: 1; filter: blur(0px); }
  to   { opacity: 0; filter: blur(2px); }
}
@keyframes sol-fade-in {
  from { opacity: 0; filter: blur(2px); }
  to   { opacity: 1; filter: blur(0px); }
}

/* --- Step 3: Directional slide for "forward" navigation --- */
/* Applied via JS (see below) by adding class to <html> */
html.vt-forward::view-transition-old(root) {
  animation: sol-slide-out-left 0.5s cubic-bezier(0.4, 0, 0.2, 1) both;
}
html.vt-forward::view-transition-new(root) {
  animation: sol-slide-in-right 0.5s cubic-bezier(0.4, 0, 0.2, 1) both;
}

html.vt-back::view-transition-old(root) {
  animation: sol-slide-out-right 0.5s cubic-bezier(0.4, 0, 0.2, 1) both;
}
html.vt-back::view-transition-new(root) {
  animation: sol-slide-in-left 0.5s cubic-bezier(0.4, 0, 0.2, 1) both;
}

@keyframes sol-slide-out-left {
  from { opacity: 1; transform: translateX(0); }
  to   { opacity: 0; transform: translateX(-8%); }
}
@keyframes sol-slide-in-right {
  from { opacity: 0; transform: translateX(8%); }
  to   { opacity: 1; transform: translateX(0); }
}
@keyframes sol-slide-out-right {
  from { opacity: 1; transform: translateX(0); }
  to   { opacity: 0; transform: translateX(8%); }
}
@keyframes sol-slide-in-left {
  from { opacity: 0; transform: translateX(-8%); }
  to   { opacity: 1; transform: translateX(0); }
}

/* --- Step 4: Named element transitions (optional) ---
   Give specific elements their own transition identity.
   Example: hero image morphs between pages instead of crossfading. */
.sol-hero-image {
  view-transition-name: hero-image;
  contain: layout;  /* Required for view-transition-name */
}

::view-transition-old(hero-image),
::view-transition-new(hero-image) {
  animation-duration: 0.6s;
  /* Browser handles the morph automatically - just set duration */
}

/* --- Step 5: Reduce motion support --- */
@media (prefers-reduced-motion: reduce) {
  ::view-transition-old(root),
  ::view-transition-new(root) {
    animation: none;
  }
}
```

```javascript
/* === VIEW TRANSITIONS - JavaScript ===
   Add to every page. Handles:
   1. Direction detection (forward/back) for slide animations
   2. Cleanup of direction classes
   3. Fallback: does nothing in unsupported browsers (graceful degradation)
*/

(function() {
  'use strict';

  // --- Feature detection ---
  // If browser doesn't support View Transitions, all navigation works normally.
  // No polyfill needed - this is pure progressive enhancement.
  const supportsViewTransitions = Boolean(document.startViewTransition)
    || CSS.supports?.('view-transition-name', 'none');

  if (!supportsViewTransitions) {
    console.log('[Sol] View Transitions not supported - using standard navigation');
    return;
  }

  // --- Track navigation history for direction ---
  const pageOrder = [
    '/',
    '/about',
    '/retreats',
    '/events',
    '/gallery',
    '/contact'
  ];

  function getPageIndex(pathname) {
    const clean = pathname.replace(/\/+$/, '') || '/';
    return pageOrder.indexOf(clean);
  }

  // --- Outgoing page: set direction class ---
  window.addEventListener('pageswap', (event) => {
    if (!event.viewTransition) return;

    const fromIndex = getPageIndex(window.location.pathname);
    const toUrl = event.activation?.entry?.url;
    if (!toUrl) return;

    const toIndex = getPageIndex(new URL(toUrl).pathname);

    if (fromIndex >= 0 && toIndex >= 0) {
      document.documentElement.classList.add(
        toIndex > fromIndex ? 'vt-forward' : 'vt-back'
      );
    }
  });

  // --- Incoming page: set direction class + cleanup after transition ---
  window.addEventListener('pagereveal', (event) => {
    if (!event.viewTransition) return;

    const fromUrl = navigation?.activation?.from?.url;
    if (!fromUrl) return;

    const fromIndex = getPageIndex(new URL(fromUrl).pathname);
    const toIndex = getPageIndex(window.location.pathname);

    if (fromIndex >= 0 && toIndex >= 0) {
      document.documentElement.classList.add(
        toIndex > fromIndex ? 'vt-forward' : 'vt-back'
      );
    }

    // Clean up direction classes after transition completes
    event.viewTransition.finished.then(() => {
      document.documentElement.classList.remove('vt-forward', 'vt-back');
    });
  });

  // --- SPA-style transitions for dynamic content (optional) ---
  // Use this if you load content via fetch instead of full page navigation
  window.solTransition = function(updateCallback) {
    if (!document.startViewTransition) {
      updateCallback();
      return;
    }
    document.startViewTransition(() => updateCallback());
  };
  // Usage: solTransition(() => { document.querySelector('.content').innerHTML = newHTML; });

})();
```

**Key decisions:**
- 8% slide distance (not 100%) - subtle, contemplative movement that matches Sol Therapy's pace
- Blur on crossfade (`filter: blur(2px)`) - mimics ink dissolving, ties to sumi-e theme
- `pageOrder` array defines navigation direction - edit to match Sol Therapy's actual nav structure
- `contain: layout` on named elements is required by the spec, not optional

---

## 3. CSS Keyframes to GSAP ScrollTrigger Equivalents

Direct translations of aroke01.com's Cargo site animations into GSAP ScrollTrigger code.

```html
<!--
  GSAP SCROLLTRIGGER EQUIVALENTS - aroke01.com animations
  Dependencies: GSAP 3.12+ with ScrollTrigger plugin
  CDN: https://cdn.jsdelivr.net/npm/gsap@3.12/dist/gsap.min.js
       https://cdn.jsdelivr.net/npm/gsap@3.12/dist/ScrollTrigger.min.js
-->

<script src="https://cdn.jsdelivr.net/npm/gsap@3.12/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12/dist/ScrollTrigger.min.js"></script>

<script>
gsap.registerPlugin(ScrollTrigger);

// ============================================================
// ANIMATION 1: Fade Up (scrollTransitionFadeUp)
// ============================================================
// Original CSS:
//   0%   { opacity: 0; transform: translateY(40px); }
//   25%  { opacity: 1; transform: translateY(0); }
//
// Meaning: element fades in and rises 40px during first 25% of scroll range.
// Remaining 75% it stays visible (already at final state).

gsap.utils.toArray('.sol-fade-up').forEach((el) => {
  gsap.fromTo(el,
    // FROM state
    { opacity: 0, y: 40 },
    // TO state + ScrollTrigger config
    {
      opacity: 1,
      y: 0,
      duration: 1,
      ease: 'power2.out',
      scrollTrigger: {
        trigger: el,
        start: 'top 85%',       // starts when element is 85% down viewport
        end: 'top 60%',         // completes over 25% of viewport height (matches 25% keyframe)
        scrub: 1,               // smooth scroll-linked animation
        // toggleActions: 'play none none reverse',  // alternative: trigger-based instead of scrub
      }
    }
  );
});
// HTML usage: <div class="sol-fade-up">Your content here</div>


// ============================================================
// ANIMATION 2: Blur In (scrollAnimationBlurIn)
// ============================================================
// Original CSS:
//   0%     { filter: blur(8px); }
//   12.5%  { filter: blur(8px); }   <-- holds blur for first 12.5%
//   35%    { filter: blur(0px); }   <-- then clears blur by 35%
//
// Meaning: delayed de-blur. Element stays blurred during initial scroll,
// then sharpens. Creates a "coming into focus" effect.

gsap.utils.toArray('.sol-blur-in').forEach((el) => {
  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: el,
      start: 'top 85%',
      end: 'top 50%',
      scrub: 1,
    }
  });

  // Phase 1: Hold blur (12.5% of timeline = first ~1/8)
  tl.fromTo(el,
    { filter: 'blur(8px)' },
    { filter: 'blur(8px)', duration: 0.125 }  // 12.5% duration - holds
  );

  // Phase 2: De-blur from 12.5% to 35% (= 22.5% of timeline)
  tl.to(el,
    { filter: 'blur(0px)', duration: 0.225, ease: 'power1.out' }
  );

  // Phase 3: Stay clear for remaining 65% (implicit - already at final state)
});
// HTML usage: <div class="sol-blur-in">Your content here</div>


// ============================================================
// ANIMATION 3: Helix Rotation (scrollAnimationHelix)
// ============================================================
// Original CSS:
//   0%   { transform: perspective(3000px) rotateY(60deg) rotateZ(2deg); }
//   100% { transform: perspective(3000px) rotateY(-60deg) rotateZ(-2deg); }
//
// Meaning: element rotates 120 degrees on Y axis as you scroll through it,
// with slight Z-axis tilt. Creates a "turning page" / helix effect.
// The 3000px perspective keeps it subtle (not extreme 3D).

gsap.utils.toArray('.sol-helix').forEach((el) => {
  // Set perspective on parent (GSAP handles rotations, but perspective
  // needs to be on the containing element for proper 3D rendering)
  gsap.set(el.parentElement || el, { perspective: 3000 });

  gsap.fromTo(el,
    // FROM state
    { rotateY: 60, rotateZ: 2 },
    // TO state
    {
      rotateY: -60,
      rotateZ: -2,
      ease: 'none',           // linear - matches CSS 0% to 100% linear interpolation
      scrollTrigger: {
        trigger: el,
        start: 'top bottom',  // starts when element enters viewport from below
        end: 'bottom top',    // ends when element exits viewport above
        scrub: 0.5,           // slight smoothing for buttery feel
      }
    }
  );
});
// HTML usage: <div class="sol-helix-wrapper"><div class="sol-helix">Your content</div></div>


// ============================================================
// COMBINED: All three effects on one element (like aroke01.com uses)
// ============================================================
// aroke01 often stacks these: fade up + blur in + helix on gallery items.
// Here's how to combine them cleanly with a single ScrollTrigger:

gsap.utils.toArray('.sol-gallery-item').forEach((el) => {
  gsap.set(el.parentElement || el, { perspective: 3000 });

  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: el,
      start: 'top 90%',
      end: 'bottom 10%',
      scrub: 1,
    }
  });

  // Fade up + blur in + rotation - all in one timeline
  tl.fromTo(el,
    {
      opacity: 0,
      y: 40,
      filter: 'blur(8px)',
      rotateY: 60,
      rotateZ: 2
    },
    {
      opacity: 1,
      y: 0,
      filter: 'blur(0px)',
      rotateY: 0,             // rest at center (neutral), not full -60
      rotateZ: 0,
      duration: 0.35,         // first 35% of scroll range
      ease: 'power2.out'
    }
  );

  // Continue rotation through remaining scroll
  tl.to(el, {
    rotateY: -60,
    rotateZ: -2,
    duration: 0.65,           // remaining 65% of scroll range
    ease: 'none'
  });
});
// HTML usage: <div class="sol-gallery-item">Image / card here</div>
</script>
```

**Key decisions:**
- `scrub: 1` on fade/blur (smoothed) vs `scrub: 0.5` on helix (more responsive to scroll)
- `perspective` set on parent element, not the rotating element itself - this is the correct CSS/GSAP approach
- Combined animation uses `rotateY: 0` as midpoint (not -60) so gallery items face forward when centered in viewport
- Timeline durations (0.35, 0.65) map to the original keyframe percentages

---

## 4. Three.js Turntable with Washi Paper Texture

Complete, embeddable Three.js scene: slowly rotating torus (enso shape) with washi paper texture.

```html
<!--
  THREE.JS ENSO TURNTABLE
  A slowly rotating torus with washi paper texture.
  Contemplative, almost invisible rotation speed.
  Embed in any page section via the container div.

  Dependencies: Three.js r160+ (ES module from CDN)
  Texture: Uses a washi paper texture URL. Replace with your own asset.
-->

<div id="enso-scene" style="width:100%;height:500px;position:relative;overflow:hidden;background:#faf8f5;"></div>

<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js"
  }
}
</script>

<script type="module">
import * as THREE from 'three';

// --- CONFIG ---
const CONFIG = {
  // Torus (enso) dimensions
  torusRadius: 2.2,           // main radius - distance from center to tube center
  tubeRadius: 0.35,           // tube thickness - thin for calligraphic feel
  radialSegments: 64,         // smoothness around the ring
  tubularSegments: 128,       // smoothness along the tube

  // Rotation
  rotationSpeed: 0.0003,      // radians per frame - barely perceptible, contemplative

  // Texture
  textureUrl: 'https://images.unsplash.com/photo-1541123437800-1bb1317badc2?w=1024&q=80',
  // ^ Placeholder washi paper texture. Replace with actual asset:
  // textureUrl: '/assets/textures/washi-paper.jpg'

  // Scene
  bgColor: '#faf8f5',         // warm off-white, Sol Therapy palette
  ambientIntensity: 0.6,
  directionalIntensity: 0.8,
};

// --- SCENE SETUP ---
const container = document.getElementById('enso-scene');
const width = container.clientWidth;
const height = container.clientHeight;

const scene = new THREE.Scene();
scene.background = new THREE.Color(CONFIG.bgColor);

// Camera: slight angle for depth, not straight-on
const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
camera.position.set(0, 1.2, 6);
camera.lookAt(0, 0, 0);

// Renderer
const renderer = new THREE.WebGLRenderer({
  antialias: true,
  alpha: false,
});
renderer.setSize(width, height);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.1;
container.appendChild(renderer.domElement);

// --- LIGHTING ---
// Soft ambient: fills shadows, prevents harsh contrast
const ambientLight = new THREE.AmbientLight(0xfff5e6, CONFIG.ambientIntensity);
scene.add(ambientLight);

// Directional: simulates natural window light from upper-left
const directionalLight = new THREE.DirectionalLight(0xffffff, CONFIG.directionalIntensity);
directionalLight.position.set(-3, 4, 5);
scene.add(directionalLight);

// Subtle fill light from opposite side
const fillLight = new THREE.DirectionalLight(0xe8dfd0, 0.3);
fillLight.position.set(3, -1, -2);
scene.add(fillLight);

// --- TEXTURE ---
const textureLoader = new THREE.TextureLoader();
const washiTexture = textureLoader.load(
  CONFIG.textureUrl,
  (texture) => {
    // Texture loaded - configure wrapping
    texture.wrapS = THREE.RepeatWrapping;
    texture.wrapT = THREE.RepeatWrapping;
    texture.repeat.set(3, 1);  // stretch across torus surface
    texture.colorSpace = THREE.SRGBColorSpace;
  },
  undefined,
  (err) => {
    console.warn('[Sol Enso] Texture load failed, using fallback color:', err);
  }
);

// --- TORUS (ENSO) ---
const geometry = new THREE.TorusGeometry(
  CONFIG.torusRadius,
  CONFIG.tubeRadius,
  CONFIG.radialSegments,
  CONFIG.tubularSegments
);

// MeshStandardMaterial: physically-based, reacts to light naturally
const material = new THREE.MeshStandardMaterial({
  map: washiTexture,
  roughness: 0.85,          // high roughness = matte paper feel
  metalness: 0.02,          // near-zero = non-metallic, organic
  color: 0xf5efe6,          // warm tint if texture fails to load
  side: THREE.DoubleSide,   // visible from both sides during rotation
});

const torus = new THREE.Mesh(geometry, material);
// Slight X tilt so it's not perfectly vertical - more natural
torus.rotation.x = Math.PI * 0.08;
scene.add(torus);

// --- ANIMATION ---
let animationId;

function animate() {
  animationId = requestAnimationFrame(animate);

  // Y-axis rotation: slow turntable
  torus.rotation.y += CONFIG.rotationSpeed;

  renderer.render(scene, camera);
}
animate();

// --- RESPONSIVE ---
const resizeObserver = new ResizeObserver((entries) => {
  for (const entry of entries) {
    const { width: w, height: h } = entry.contentRect;
    if (w === 0 || h === 0) continue;

    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  }
});
resizeObserver.observe(container);

// --- CLEANUP ---
// Call this if the section is removed from DOM (SPA navigation, etc.)
window.ensoCleanup = function() {
  cancelAnimationFrame(animationId);
  resizeObserver.disconnect();
  geometry.dispose();
  material.dispose();
  washiTexture.dispose();
  renderer.dispose();
  container.removeChild(renderer.domElement);
};

// --- VISIBILITY OPTIMIZATION ---
// Pause animation when not visible (saves GPU)
const visibilityObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      if (!animationId) animate();
    } else {
      cancelAnimationFrame(animationId);
      animationId = null;
    }
  });
}, { threshold: 0.1 });
visibilityObserver.observe(container);
</script>
```

**Key decisions:**
- `rotationSpeed: 0.0003` - one full revolution takes ~35 minutes. You notice it only if you look away and back. Contemplative.
- `TorusGeometry` (not TorusKnot) - clean circle = enso. Thin tube radius (0.35) makes it calligraphic, not donut-like.
- `roughness: 0.85` + `metalness: 0.02` = matte paper material that responds to light without any sheen
- `ResizeObserver` instead of window resize event - works when container size changes (responsive layouts, not just window resize)
- `IntersectionObserver` pauses rendering when out of viewport - critical performance optimization
- ACES Filmic tone mapping gives the warm, slightly compressed tonal range that matches sumi-e aesthetic
- Cleanup function exposed for SPA contexts where the section might be removed/re-added

---

## Technical Notes

1. **All code is copy-paste ready.** Each block runs standalone with only its stated dependencies (Three.js from CDN, GSAP from CDN). No build step required.

2. **Texture URL in Block 4** is a placeholder. Replace `CONFIG.textureUrl` with an actual washi paper texture asset path (e.g., `/assets/textures/washi-paper.jpg`).

3. **View Transitions (Block 2)** requires Chrome 126+ for cross-document transitions. Firefox and Safari support is shipping. The code gracefully degrades - no feature = normal navigation.

4. **GSAP (Block 3)** requires a GSAP license for commercial use. Sol Therapy should use GSAP's standard license (free for most sites) or their Business license if revenue exceeds their threshold.

5. **Performance:** Block 1 (grain shader) and Block 4 (turntable) both run WebGL. If both are on the same page, they share the GPU. The grain shader is extremely lightweight (single fullscreen quad, no geometry). The turntable pauses when off-screen via IntersectionObserver.
