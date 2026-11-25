# Component & Effect Gallery (50 standalone HTML demos)

Open any file in a browser (internet needed for CDN libs). No image/model assets required. All handle `prefers-reduced-motion` (or graceful fallback).
Status: JS syntax-checked with `node --check` (all pass). Components `01, 06, 08, 13, 19, 24` were browser-verified via local HTTP server (HTTP 200, 0 console/network errors).

## 3D
| # | File | Effect | Libs |
|---|---|---|---|
| 01 | `01-3d-floating-product.html` | Procedural bottle floating, spinning, mouse tilt, shadow blob, giant bg text | three |
| 02 | `02-3d-scroll-rotate-model.html` | Pinned torus-knot changes pose/color per section on scroll | three, GSAP, Lenis |
| 03 | `03-3d-particles-sphere.html` | 14k particles morph sphere/torus/text, mouse repel | three, GSAP |
| 04 | `04-3d-card-carousel.html` | CSS-3D card ring, drag inertia, wheel, keys, snap | GSAP |
| 05 | `05-3d-cube-css.html` | Pure CSS 3D cube, drag, hover explode | none |
| 06 | `06-3d-ring-slabs.html` | Cota-Zero ring of slabs rotating/descending on scroll | three, GSAP, Lenis |

## Text & cursor
| # | File | Effect | Libs |
|---|---|---|---|
| 07 | `07-split-text-reveal.html` | Lines/words/chars rise from masks on scroll | GSAP, ScrollTrigger |
| 08 | `08-gradient-wave-text.html` | Per-letter wave + drifting gradient + pointer scale | GSAP |
| 09 | `09-scramble-text.html` | Decode scramble on hover/focus/scroll | GSAP, ScrollTrigger |
| 10 | `10-custom-cursor-trail.html` | Dot + blend ring + trail + labelled hover states | GSAP |
| 11 | `11-magnetic-buttons-grid.html` | Magnetic pull, circular fill, arrow swap | GSAP |
| 12 | `12-text-marquee-velocity.html` | Marquees reacting to scroll velocity + skew | GSAP, ScrollTrigger |

## Backgrounds & shaders
| # | File | Effect | Libs |
|---|---|---|---|
| 13 | `13-shader-gradient-webgl.html` | Raw WebGL mesh gradient, noise, grain, mouse | WebGL |
| 14 | `14-light-rays.html` | Volumetric god-rays shader | WebGL |
| 15 | `15-grain-aurora.html` | Pure CSS aurora blobs + SVG grain | none |
| 16 | `16-dot-grid-reactive.html` | Canvas dot grid spring physics, click shockwave | Canvas 2D |
| 17 | `17-liquid-distortion-image.html` | Liquid ripple + RGB split shader on procedural image | WebGL |
| 18 | `18-spotlight-border-cards.html` | Cursor spotlight + conic animated border | none |

## Scroll, layout & interactive sections
| # | File | Effect | Libs |
|---|---|---|---|
| 19 | `19-horizontal-scroll.html` | Pinned horizontal gallery + progress bar | GSAP, ScrollTrigger, Lenis |
| 20 | `20-clip-path-image-reveal.html` | Clip-path/curtain reveals + zoom | GSAP, ScrollTrigger, Lenis |
| 21 | `21-parallax-layers.html` | SVG multi-layer scroll + mouse parallax | GSAP, ScrollTrigger, Lenis |
| 22 | `22-accordion-gallery.html` | Expanding flex panels on hover/click/focus | GSAP |
| 23 | `23-bento-hover.html` | Bento grid, batch entrance, count-up, tilt, glow | GSAP, ScrollTrigger, Lenis |
| 24 | `24-preloader-counter.html` | 0-100 preloader, curtain reveal, hero intro | GSAP, Lenis |
| 25 | `25-scroll-sequence.html` | Pinned canvas frame-sequence scrub + Lenis sync + chapter captions + loader | GSAP, ScrollTrigger, Lenis |
| 26 | `26-sticky-layers-scrollytelling.html` | MELT-style product assembly: pinned stage, layers dropping, per-chapter bg color change | GSAP, ScrollTrigger, Lenis |
| 27 | `27-tilt-marquee-glass.html` | DEUCE-style hero type with italic accent, tilted marquee, glass pill nav, 3D tilt card, magnetic CTA | GSAP |
| 28 | `28-product-configurator-builder.html` | Oakberry-style interactive configurator: state, caps, price, layered toppings animation, order modal | GSAP |

## Subtle, generic & SaaS/product UI (no external libs)
| # | File | Effect | Libs |
|---|---|---|---|
| 29 | `29-command-palette.html` | Cmd/Ctrl+K modal, fast scale/opacity open, fuzzy filter, keyboard nav | none |
| 30 | `30-sliding-pill-tabs.html` | Sliding pill/underline indicator + subtle crossfade + arrow keys | none |
| 31 | `31-toast-notification-stack.html` | Sonner-style stacked toasts, hover expand, swipe/click dismiss | none |
| 32 | `32-smooth-accordion-faq.html` | CSS `grid-template-rows` `0fr->1fr` accordion + single/multi toggle | none |
| 33 | `33-drawer-bottom-sheet.html` | Vaul-style bottom sheet, pointer drag-to-close, backdrop scale | none |
| 34 | `34-segmented-control-toggles.html` | Sliding segmented control, switches, radio option cards | none |
| 35 | `35-copy-button-tooltip.html` | Copy-to-clipboard SVG morph + directional tooltips | none |
| 36 | `36-pricing-toggle-cards.html` | Monthly/annual toggle + vertical digit roll + clean SaaS cards | none |
| 37 | `37-sticky-toc-scrollspy.html` | Sticky docs TOC with `IntersectionObserver` active rail | none |
| 38 | `38-skeleton-shimmer-card.html` | Zero-CLS shimmer skeleton crossfading into loaded cards | none |

## Landing page & product showcase (crafted motion)
| # | File | Effect | Libs |
|---|---|---|---|
| 39 | `39-product-exploded-view.html` | Scroll & toggle 3D exploded smartwatch assembly + callout lines | GSAP, ScrollTrigger |
| 40 | `40-product-colorway-morph.html` | Colorway/finish switcher with radial clip-path wipe + tint morph | GSAP |
| 41 | `41-product-hotspot-zoom.html` | Interactive numbered hotspots with pan & zoom into hardware details | GSAP |
| 42 | `42-editorial-lookbook-parallax.html` | Asymmetric editorial lookbook with speed differentials & overlapping type | GSAP, ScrollTrigger, Lenis |
| 43 | `43-product-feature-orbit.html` | Rotating orbital feature ring around central hero product | GSAP, ScrollTrigger |
| 44 | `44-before-after-compare-slider.html` | Draggable/keyboard comparison curtain (CAD vs finished) + 3D tilt | GSAP |
| 45 | `45-3d-apartment-walkthrough.html` | Three.js 3D apartment tour: enter through glass + click rooms (Lounge/Kitchen/Suite) | three, GSAP |
| 46 | `46-hero-mask-reveal-curtain.html` | Giant SVG knockout text masking hardware stage expanding on scroll | GSAP, ScrollTrigger |
| 47 | `47-floating-review-social-proof.html` | Depth-layered hero lens with drifting press quotes & cursor parallax | GSAP, ScrollTrigger |
| 48 | `48-scroll-progress-story-rail.html` | 3-act launch narrative with vertical progress rail & sticky morphing visual | GSAP, ScrollTrigger, Lenis |
| 49 | `49-hover-image-trail-gallery.html` | Editorial collection index spawning velocity-tilted floating preview cards | GSAP |
| 50 | `50-3d-spatial-tour-scroll.html` | Three.js continuous `CatmullRomCurve3` scroll-scrubbed loft apartment tour | three, GSAP, ScrollTrigger, Lenis |

## Mapping to the reels
- Floating product (reels 3/sneaker) -> `01`, `02`
- Ring of slabs (Cota Zero, reel 3) -> `06`
- Tilt card (Spell UI, reel 5) -> `05`, `18`, `23`, `27`
- Marquee (Oakberry, reel 1) -> `12`, `27`
- Shader gradient & light rays (Spell UI, reel 5) -> `13`, `14`
- Scrubbed video/frames (reels 4, 6, 7) -> `25`
- Scrollytelling product stack (MELT, reel 2) -> `26`
- Interactive configurator (Oakberry, reel 1) -> `28`
- Preloader / intro -> `24`

Next steps for a real project: replace procedural/SVG placeholders with AI-generated assets, add `DESIGN.md`, split into React/framework components if needed, and add R3F/Spline for custom 3D (see `references/03-3d-webgl.md`).
