---
name: cinematic-web-motion
description: Build award-style, scroll-driven landing pages with cinematic animation, scrollytelling, scrubbed video/frame sequences, 3D (Three.js/R3F/Spline), editorial typography, tilt cards, marquees and configurators. Use when the user wants a "premium", "animated", "3D", "scrollytelling" or "Awwwards-like" website, a product reveal site, concept/brand site, or says "make a site like this reel".
---

# Cinematic Web Motion

Recreates the look of viral "one prompt, $8k site" reels: a single product/place told as ONE continuous scroll journey, bold type, a strong 2-3 color palette, and one signature interaction.

## Workflow (follow in order)
1. **Pick the concept & archetype** -> `references/06-case-studies.md`. Choose ONE signature moment (e.g. layers stacking, camera through glass, pour transition, configurator). Everything else supports it.
2. **Write a design brief / DESIGN.md** (palette, fonts, radii, motion language) -> `references/05-design-system.md`. Never leave defaults (no generic purple gradient, no Inter-only look).
3. **Choose the hero technique** with the decision table below.
4. **Produce assets** (AI images/video, transparent PNG layers, GLB model) -> `references/02-scroll-video-pipeline.md`, `03-3d-webgl.md`.
5. **Build**: scaffold, smooth scroll (Lenis) synced to GSAP ScrollTrigger, sections, UI effects (`04-ui-effects.md`).
6. **Polish**: performance, reduced-motion, mobile fallback, loader -> `08-performance-a11y.md`.
7. **Verify** in a browser at 1440x900 and 390x844: scroll through top to bottom, check no jank, no layout shift, console clean.

## Hero technique decision table
| Need | Use | Reference |
|---|---|---|
| Product assembles/pours/transforms as user scrolls | Scroll-scrubbed frame sequence on `<canvas>` (frames from AI video) | 02 |
| Few layered objects dropping in (cookie layers) | Sticky stage + transparent PNG/WebP layers animated by GSAP timeline `scrub` | 02, example `26-sticky-layers-scrollytelling.html` |
| Real 3D object reacting to scroll/mouse | React Three Fiber / Three.js + GLB, or Spline embed | 03 |
| Walk-through/space tour | Frame sequence per room (clip A->B), click triggers play-through; or gaussian splat | 02, 06 |
| Cards/hover polish | CSS 3D tilt, spotlight, marquee, stagger text | 04 |
| Quick, no-build | Single HTML + CDN GSAP/Lenis (see examples) | examples/ |

## Default stack
- Static/single page: HTML + CSS + vanilla JS, GSAP 3 + ScrollTrigger + Lenis via CDN.
- App: Vite/Next.js + React + Tailwind + GSAP (`@gsap/react` `useGSAP`) or Framer/Motion + `@react-three/fiber` + `@react-three/drei`.
- Components: shadcn registry (Spell UI, Magic UI, Aceternity, 21st.dev) -> `07-resources.md`.

## Non-negotiable rules
- One signature interaction, 2-3 colors + 1 accent, 2 font families max (display + UI), big type (clamp 4rem-14rem).
- Section copy is short: eyebrow + 2-4 word headline + 1 sentence + pill CTA.
- Alternate section background colors in the same palette family to mark chapters.
- Easing: `cubic-bezier(.2,.7,.2,1)` for reveals; `power3.out`/`expo.out` in GSAP; scrub smoothing 0.5-1.
- Always add `prefers-reduced-motion` fallback, `loading` state, mobile fallback (lighter frames or static).
- Never use copyrighted brand assets for real clients; concept sites must carry a disclaimer (as in the Oakberry reel).
- Check licenses of copied components (dotmira lists author+license).

## Prompting an AI agent with this skill (template)
"Use the cinematic-web-motion skill. Concept: <brand/product>. Archetype: <from case studies>. Signature moment: <...>. Palette/fonts: <...>. Stack: <...>. Build, run dev server, screenshot at desktop+mobile, fix issues."

## Files
- `references/01-workflow-and-prompting.md` prompt recipes & AI tooling pipeline
- `references/02-scroll-video-pipeline.md` frames, canvas scrub, layers
- `references/03-3d-webgl.md` R3F, Three, Spline, shaders
- `references/04-ui-effects.md` code for marquee, tilt, text reveals, dividers, glass, configurator
- `references/05-design-system.md` palettes, type, DESIGN.md template
- `references/06-case-studies.md` the 8 reels broken down as recipes
- `references/07-resources.md` curated links
- `references/08-performance-a11y.md`
- `references/09-reference-sites.md` verified reference sites, galleries, component registries, Codrops repos
- `references/10-subtle-ui-references.md` 15+ subtle, generic, product/SaaS UI references (Design Spells, Details Matter, Dead Simple Sites, animations.dev, Origin UI, Kibo UI, SmoothUI, Motion Primitives, etc.)
- `examples/` 100 standalone HTML components (indexed below by goal; details in `examples/README.md`)

## Example Index (pick by goal)
**Product Showcase & Launch Landing Pages**
- `01-3d-floating-product.html` — 3D bottle floating/spinning, mouse tilt, studio lighting, giant bg text
- `26-sticky-layers-scrollytelling.html` — MELT-style product assembly, layers drop on scroll, bg color shifts
- `28-product-configurator-builder.html` — interactive customizer/builder with live layered preview & order modal
- `39-product-exploded-view.html` — scroll/toggle 3D exploded hardware view with callout lines
- `40-product-colorway-morph.html` — colorway/finish switcher with radial clip-path wipe & tint morph
- `41-product-hotspot-zoom.html` — interactive numbered hotspots with smooth pan & zoom into details
- `43-product-feature-orbit.html` — rotating orbital feature ring around central hero product
- `44-before-after-compare-slider.html` — draggable/keyboard split curtain comparing raw vs finished hardware
- `45-3d-apartment-walkthrough.html` — Three.js 3D apartment tour: enter through glass + click rooms (Lounge/Kitchen/Suite)
- `50-3d-spatial-tour-scroll.html` — Three.js continuous `CatmullRomCurve3` scroll-scrubbed loft apartment tour
- `46-hero-mask-reveal-curtain.html` — giant SVG knockout text masking hardware stage expanding on scroll
- `47-floating-review-social-proof.html` — depth-layered hero product with drifting press quotes & cursor parallax
- `48-scroll-progress-story-rail.html` — 3-act product story with vertical progress rail & sticky morphing visual
- `49-hover-image-trail-gallery.html` — editorial product index spawning velocity-tilted floating preview cards

**Scroll Choreography & Layout**
- `19-horizontal-scroll.html` (pinned horizontal gallery) | `20-clip-path-image-reveal.html` (curtain/iris reveals)
- `21-parallax-layers.html` (8-layer SVG scroll+mouse parallax) | `22-accordion-gallery.html` (expanding flex panels)
- `23-bento-hover.html` (bento grid, count-up, tilt, glow) | `24-preloader-counter.html` (0-100 curtain hero intro)
- `25-scroll-sequence.html` (canvas frame-sequence scrub + Lenis + captions)
- `42-editorial-lookbook-parallax.html` (asymmetric lookbook with speed differentials & overlapping type)

**3D & WebGL**
- `02-3d-scroll-rotate-model.html` (scroll-driven pose/color) | `03-3d-particles-sphere.html` (14k morphing particles)
- `04-3d-card-carousel.html` (CSS-3D ring carousel) | `05-3d-cube-css.html` (pure CSS 3D cube)
- `06-3d-ring-slabs.html` (Cota-Zero tilted slab ring on scroll)

**Typography, Cursor & Backgrounds/Shaders**
- `07-split-text-reveal.html` | `08-gradient-wave-text.html` | `09-scramble-text.html` | `10-custom-cursor-trail.html`
- `11-magnetic-buttons-grid.html` | `12-text-marquee-velocity.html` | `27-tilt-marquee-glass.html` (hero+marquee+tilt+glass nav)
- `13-shader-gradient-webgl.html` | `14-light-rays.html` | `15-grain-aurora.html` (CSS-only)
- `16-dot-grid-reactive.html` | `17-liquid-distortion-image.html` | `18-spotlight-border-cards.html`

**Subtle, Generic & Product/SaaS UI (zero deps)**
- `29-date-range-picker.html` | `30-combobox-multiselect-tags.html` | `31-context-menu-submenu.html`
- `32-popover-hovercard-origin.html` | `33-stepper-wizard-form.html` | `34-file-dropzone-upload-progress.html`
- `35-notification-inbox-popover.html` | `36-sortable-data-table-expand.html` | `37-range-slider-otp-input.html` | `38-kanban-drag-drop.html`

**Advanced Motion, CSS Timelines & Interactive Canvas (51–70)**
- `51-word-by-word-scroll-opacity.html` | `52-sticky-card-stack.html` | `53-magnetic-dock.html` | `54-3d-tilt-flip-cards.html`
- `55-curtain-page-transition.html` | `56-fullscreen-menu-image-reveal.html` | `57-svg-path-draw-scroll.html` | `58-odometer-stats-ticker.html`
- `59-glass-orbs-parallax-hero.html` | `60-infinite-drag-carousel.html` | `61-morphing-blob-svg.html` | `62-scroll-driven-css-timeline.html`
- `63-view-transitions-gallery.html` | `64-canvas-particle-text.html` | `65-horizontal-timeline-scrub.html` | `66-split-screen-scroll-compare.html`
- `67-cursor-lens-magnifier.html` | `68-audio-visualizer-bars.html` | `69-elastic-string-line.html` | `70-text-scramble-hero-intro.html`

**Product UI Craft: Overlays, Feedback & Forms (71–82)**
- `71-command-palette-cmdk.html` | `72-sliding-pill-tabs.html` | `73-toast-stack-sonner.html` | `74-drawer-bottom-sheet-vaul.html`
- `75-smooth-accordion-faq.html` | `76-segmented-control-toggle.html` | `77-copy-button-tooltip.html` | `78-pricing-toggle-cards.html`
- `79-sticky-toc-scrollspy.html` | `80-skeleton-to-content-shimmer.html` | `81-empty-state-illustrated.html` | `82-morphing-dialog-flip.html`

**Gestures, Lists, Links & Media (83–88)**
- `83-swipe-to-dismiss-list.html` | `84-animated-checkbox-todo.html` | `85-search-input-expand-filter.html`
- `86-link-hover-underline-styles.html` | `87-image-zoom-lightbox-flip.html` | `88-scroll-snap-story-cards.html`

**Hero Intros, Ambient Effects & Navigation (89–100)**
- `89-editorial-hero-load-stagger.html` | `90-number-stepper-spring.html` | `91-logo-marquee-pause-hover.html` | `92-cursor-follow-tooltip-card.html`
- `93-border-beam-card.html` | `94-flip-clock-countdown.html` | `95-progress-ring-scroll-top.html` | `96-stacked-avatars-hover-expand.html`
- `97-dropdown-nav-morph.html` | `98-3d-scroll-tunnel.html` | `99-spotlight-mask-reveal.html` | `100-motion-preference-showcase.html`

