# Component & Effect Gallery (100 standalone HTML demos)

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
| 29 | `29-date-range-picker.html` | Interactive calendar popover with range hover preview & keyboard navigation | none |
| 30 | `30-combobox-multiselect-tags.html` | Searchable multi-select combobox with animated tag chips & arrow-key selection | none |
| 31 | `31-context-menu-submenu.html` | Right-click / Shift+F10 context menu with nested submenu & viewport-safe positioning | none |
| 32 | `32-popover-hovercard-origin.html` | Origin-aware anchored popover & hover card with intent delay & Escape dismiss | none |
| 33 | `33-stepper-wizard-form.html` | Multi-step wizard with directional slide transition, validation & step indicator | none |
| 34 | `34-file-dropzone-upload-progress.html` | Drag-and-drop file uploader with simulated progress bar, cancel & retry states | none |
| 35 | `35-notification-inbox-popover.html` | Top-bar notification bell popover with unread filter, mark-all-read & row archive | none |
| 36 | `36-sortable-data-table-expand.html` | Sortable SaaS table with filter & `grid-template-rows` expandable detail rows | none |
| 37 | `37-range-slider-otp-input.html` | Custom-tracked range slider + 6-digit OTP input with paste & error shake | none |
| 38 | `38-kanban-drag-drop.html` | 3-column Kanban board with HTML5 drag-and-drop & accessible arrow move buttons | none |

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

## Advanced motion, CSS timelines & interactive canvas (51–70)
| # | File | Effect | Libs |
|---|---|---|---|
| 51 | `51-word-by-word-scroll-opacity.html` | Scroll-scrubbed word-by-word opacity highlight of a paragraph | GSAP, ScrollTrigger |
| 52 | `52-sticky-card-stack.html` | Sticky cards stack while earlier cards scale down and dim as the next slides over | GSAP, ScrollTrigger |
| 53 | `53-magnetic-dock.html` | macOS-style dock where icon scale follows pointer distance (cosine falloff, rAF lerp) | none |
| 54 | `54-3d-tilt-flip-cards.html` | Click-to-flip cards with pointer 3D tilt and moving glare | none |
| 55 | `55-curtain-page-transition.html` | Hash-routed SPA transition with 5 staggered curtain panels | none (WAAPI) |
| 56 | `56-fullscreen-menu-image-reveal.html` | Clip-path overlay menu with staggered link rise & cursor-following preview | GSAP |
| 57 | `57-svg-path-draw-scroll.html` | SVG path drawn by scroll (`stroke-dashoffset`) with a marker riding the path | GSAP, ScrollTrigger |
| 58 | `58-odometer-stats-ticker.html` | Rolling-digit odometer counters that start on view | none |
| 59 | `59-glass-orbs-parallax-hero.html` | Glassmorphism hero with floating gradient orbs and mouse-parallax depth layers | none |
| 60 | `60-infinite-drag-carousel.html` | Draggable infinite looping carousel with inertia and keyboard nudging | none |
| 61 | `61-morphing-blob-svg.html` | Smooth SVG blob path morphing driven by hover/scroll/loop | GSAP |
| 62 | `62-scroll-driven-css-timeline.html` | Pure CSS `animation-timeline: scroll()/view()` progress & reveal with fallback | none (CSS) |
| 63 | `63-view-transitions-gallery.html` | View Transitions API grid-to-detail morph with graceful fallback | none (View Transitions) |
| 64 | `64-canvas-particle-text.html` | Canvas text formed by particles with pointer repulsion and spring return | Canvas 2D |
| 65 | `65-horizontal-timeline-scrub.html` | Pinned horizontal company timeline scrubbed on scroll with active milestone markers | GSAP, ScrollTrigger |
| 66 | `66-split-screen-scroll-compare.html` | Two-column opposing-direction scroll comparison | GSAP, ScrollTrigger |
| 67 | `67-cursor-lens-magnifier.html` | Circular magnifier lens following cursor over an SVG/CSS illustration | none |
| 68 | `68-audio-visualizer-bars.html` | Simulated audio-reactive bars/canvas visualizer with play/pause toggle | Canvas 2D |
| 69 | `69-elastic-string-line.html` | Interactive SVG string that stretches toward pointer and springs back | GSAP |
| 70 | `70-text-scramble-hero-intro.html` | Cinematic hero intro: staggered letter drop, SVG line draw, counter & subtle grain | GSAP |

## Product UI craft, gestures & ambient effects (71–100)
Status: JS syntax-checked with `node --check`; not yet browser-verified. References: Rauno cmdk, Sonner, Vaul, Motion Primitives, Origin UI, Design Spells, Details Matter.
| # | File | Effect | Libs |
|---|---|---|---|
| 71 | `71-command-palette-cmdk.html` | Ctrl/Cmd+K palette with one sliding highlight | none |
| 72 | `72-sliding-pill-tabs.html` | Tabs with a single resizing pill indicator | none |
| 73 | `73-toast-stack-sonner.html` | Stacked toasts that fan out on hover | none |
| 74 | `74-drawer-bottom-sheet-vaul.html` | Draggable bottom sheet with snap points | none |
| 75 | `75-smooth-accordion-faq.html` | FAQ accordion via `grid-template-rows` | none |
| 76 | `76-segmented-control-toggle.html` | Sliding segmented control + spring switch | none |
| 77 | `77-copy-button-tooltip.html` | Copy button with icon morph and tooltip | none |
| 78 | `78-pricing-toggle-cards.html` | Billing toggle with animated price swap | none |
| 79 | `79-sticky-toc-scrollspy.html` | Sticky TOC with scrollspy marker | none |
| 80 | `80-skeleton-to-content-shimmer.html` | Skeleton shimmer cross-fading to content | none |
| 81 | `81-empty-state-illustrated.html` | Rich empty state with SVG illustration | none |
| 82 | `82-morphing-dialog-flip.html` | Card-to-dialog FLIP morph | none |
| 83 | `83-swipe-to-dismiss-list.html` | Swipe rows to delete/archive with undo | none |
| 84 | `84-animated-checkbox-todo.html` | SVG check draw-on, strike wipe, FLIP reorder | none |
| 85 | `85-search-input-expand-filter.html` | Expanding search with live filter | none |
| 86 | `86-link-hover-underline-styles.html` | Six editorial link hover treatments | none |
| 87 | `87-image-zoom-lightbox-flip.html` | Thumbnail to lightbox FLIP | none |
| 88 | `88-scroll-snap-story-cards.html` | Scroll-snap cards with progress dots | none |
| 89 | `89-editorial-hero-load-stagger.html` | Masked line rise hero intro | GSAP |
| 90 | `90-number-stepper-spring.html` | Quantity stepper with digit roll | none |
| 91 | `91-logo-marquee-pause-hover.html` | Two-row marquee, pause on hover/focus | none |
| 92 | `92-cursor-follow-tooltip-card.html` | Preview card following the cursor | none |
| 93 | `93-border-beam-card.html` | CSS light beam around a card border | none (CSS) |
| 94 | `94-flip-clock-countdown.html` | Split-flap countdown | none |
| 95 | `95-progress-ring-scroll-top.html` | Scroll progress ring / back-to-top | none |
| 96 | `96-stacked-avatars-hover-expand.html` | Avatar stack fanning on hover | none |
| 97 | `97-dropdown-nav-morph.html` | Nav with one morphing dropdown background | none |
| 98 | `98-3d-scroll-tunnel.html` | CSS 3D tunnel driven by scroll | none |
| 99 | `99-spotlight-mask-reveal.html` | Cursor mask revealing a hidden layer | none |
| 100 | `100-motion-preference-showcase.html` | Live reduce-motion switch showcase | none |

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
