import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ALLUCO | Aluminium Logistics Experience",
    page_icon="A",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    r"""
    <style>
    html, body, [data-testid="stAppViewContainer"], .stApp {
        margin: 0 !important;
        padding: 0 !important;
        background: #f4f3ef !important;
        overflow: hidden !important;
    }
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    footer,
    #MainMenu {
        display: none !important;
    }
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    .block-container {
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
    }
    [data-testid="stVerticalBlock"] { gap: 0 !important; }
    iframe {
        position: fixed !important;
        inset: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        min-height: 100vh !important;
        border: 0 !important;
        display: block !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

SITE_HTML = r'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="theme-color" content="#f4f3ef" />
<meta name="description" content="ALLUCO - aluminium systems, international logistics, stock and distribution." />
<title>ALLUCO | Aluminium in motion</title>
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<style>
:root {
  --paper: #f4f3ef;
  --paper-2: #faf9f6;
  --ink: #14171a;
  --muted: #6f777e;
  --line: rgba(20,23,26,.13);
  --blue: #1d6fb8;
  --blue-soft: #7fb2d8;
  --card: rgba(250,249,246,.91);
  --shadow: 0 24px 70px rgba(31,38,44,.12);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; background: var(--paper); }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  overflow-x: hidden;
}
a { color: inherit; text-decoration: none; }
button { font: inherit; }
#webgl {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  display: block;
  z-index: 0;
}
.world-wash {
  position: fixed;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  background:
    linear-gradient(90deg, rgba(244,243,239,.25), rgba(244,243,239,0) 42%, rgba(244,243,239,.07)),
    radial-gradient(circle at 54% 48%, transparent 20%, rgba(244,243,239,.06) 75%, rgba(244,243,239,.22));
}
.header {
  position: fixed;
  inset: 0 0 auto 0;
  height: 72px;
  z-index: 90;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 0 clamp(22px, 4vw, 64px);
  background: rgba(250,249,246,.76);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(18px);
}
.brand { display: flex; align-items: center; gap: 12px; font-weight: 900; letter-spacing: .17em; font-size: .86rem; }
.brand-mark {
  width: 32px; height: 32px; position: relative; display: inline-block;
  background: linear-gradient(145deg,#f8f8f5,#9ba4aa);
  border: 1px solid rgba(20,23,26,.16);
  overflow: hidden;
}
.brand-mark::before { content:""; position:absolute; left:7px; right:7px; bottom:7px; top:7px; border-left:3px solid #2c343b; border-bottom:3px solid #2c343b; transform:skew(-12deg); }
.brand-mark::after { content:""; position:absolute; width:3px; height:20px; left:14px; top:5px; background:var(--blue); transform:skew(-12deg); }
.nav { display: flex; align-items: center; gap: 26px; color: #626a71; font-size: .65rem; font-weight: 800; text-transform: uppercase; letter-spacing: .14em; }
.nav a { transition: color .2s ease; }
.nav a:hover { color: var(--ink); }
.nav .contact-link { border: 1px solid var(--line); padding: 10px 14px; background: rgba(255,255,255,.5); }
.menu { display: none; border: 0; background: transparent; padding: 8px; }
.menu span { display:block; width:22px; height:1px; background:#222; margin:5px 0; }

main { position: relative; z-index: 4; }
.story {
  min-height: 100svh;
  padding: 98px clamp(22px,5vw,78px) 54px;
  display: flex;
  align-items: flex-end;
  position: relative;
}
.hero { min-height: 108svh; }
.copy-card {
  width: min(390px, 34vw);
  padding: 26px 27px 25px;
  background: var(--card);
  border: 1px solid rgba(20,23,26,.12);
  box-shadow: var(--shadow);
  backdrop-filter: blur(20px);
}
.copy-card.right { margin-left: auto; }
.kicker {
  margin: 0 0 13px;
  color: var(--blue);
  font-size: .62rem;
  font-weight: 900;
  letter-spacing: .19em;
  text-transform: uppercase;
}
.copy-card h1,
.copy-card h2 {
  margin: 0;
  font-size: clamp(2.25rem,4vw,4.35rem);
  line-height: .94;
  letter-spacing: -.055em;
  font-weight: 760;
}
.copy-card h1 span { color:#7c858b; font-weight: 520; }
.copy-card p:not(.kicker) {
  margin: 18px 0 0;
  color: var(--muted);
  font-size: .92rem;
  line-height: 1.68;
}
.actions { display:flex; gap:8px; margin-top:22px; flex-wrap:wrap; }
.btn {
  display:inline-flex; align-items:center; justify-content:center;
  min-height: 41px; padding: 0 14px;
  border:1px solid var(--line); background: rgba(255,255,255,.52);
  font-size:.61rem; text-transform:uppercase; letter-spacing:.12em; font-weight:900;
}
.btn.primary { background:#161b20; border-color:#161b20; color:#fff; }
.specs { display:grid; grid-template-columns:repeat(3,1fr); gap:9px; padding-top:16px; margin-top:18px; border-top:1px solid var(--line); }
.specs span { display:block; color:#8c949a; font-size:.52rem; text-transform:uppercase; letter-spacing:.11em; }
.specs b { display:block; margin-top:4px; font-size:.68rem; }

.stage-dots {
  position: fixed;
  z-index: 60;
  right: 24px;
  bottom: 26px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.stage-dots button {
  width: 8px; height: 8px; padding: 0; border-radius: 50%;
  border: 1px solid rgba(20,23,26,.4); background: rgba(255,255,255,.75); cursor:pointer;
  transition:.25s ease;
}
.stage-dots button.active { background:var(--blue); border-color:var(--blue); box-shadow:0 0 0 5px rgba(29,111,184,.12); }
.world-caption {
  position: fixed;
  z-index: 8;
  top: 92px;
  right: clamp(24px,4vw,62px);
  padding: 9px 11px;
  border:1px solid rgba(20,23,26,.10);
  background:rgba(250,249,246,.82);
  backdrop-filter:blur(14px);
  color:#687078;
  font-size:.56rem;
  letter-spacing:.14em;
  text-transform:uppercase;
  opacity:0;
  transform:translateY(-4px);
  transition:.25s ease;
}
.world-caption.show { opacity:1; transform:none; }

.content {
  position: relative;
  z-index: 12;
  padding: 108px clamp(24px,6vw,96px);
  background:#fff;
  border-top:1px solid var(--line);
}
.content.alt { background:#f0f2f1; }
.wrap { width:min(1280px,100%); margin:0 auto; }
.section-kicker { margin:0 0 18px; color:var(--blue); font-size:.64rem; font-weight:900; letter-spacing:.18em; text-transform:uppercase; }
.section-head { display:grid; grid-template-columns:1.1fr .9fr; gap:56px; align-items:end; margin-bottom:44px; }
.section-head h2 { margin:0; font-size:clamp(2.8rem,5vw,5.7rem); line-height:.95; letter-spacing:-.055em; font-weight:720; }
.section-head p { margin:0; color:var(--muted); line-height:1.75; }
.stats { display:grid; grid-template-columns:repeat(3,1fr); border-left:1px solid var(--line); border-top:1px solid var(--line); }
.stats article { min-height:138px; padding:28px; display:flex; flex-direction:column; justify-content:space-between; border-right:1px solid var(--line); border-bottom:1px solid var(--line); background:#fff; }
.stats strong { font-size:clamp(2rem,3.1vw,3.5rem); letter-spacing:-.05em; font-weight:680; }
.stats span { color:var(--muted); font-size:.75rem; }
.services { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; }
.services article { padding:28px; background:#fff; border:1px solid var(--line); min-height:210px; }
.services .index { color:var(--blue); font-size:.62rem; font-weight:900; letter-spacing:.13em; }
.services h3 { margin:25px 0 12px; font-size:1.35rem; }
.services p { margin:0; color:var(--muted); line-height:1.7; }
.products { display:grid; grid-template-columns:repeat(2,1fr); border-left:1px solid var(--line); border-top:1px solid var(--line); }
.products article { padding:30px; border-right:1px solid var(--line); border-bottom:1px solid var(--line); background:#fff; }
.products h3 { margin:0 0 15px; font-size:1.35rem; }
.products ul { margin:0; padding-left:18px; color:var(--muted); line-height:1.8; }
.contact { background:#11181f; color:#f4f7f8; }
.contact .section-kicker { color:#76b8ec; }
.contact .section-head p { color:#a6b1ba; }
.contact-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:rgba(255,255,255,.12); }
.contact-grid > * { min-height:118px; padding:23px; background:#11181f; display:flex; flex-direction:column; justify-content:flex-end; gap:7px; }
.contact-grid span { color:#84919d; font-size:.58rem; text-transform:uppercase; letter-spacing:.13em; }
.contact-grid strong { font-size:.9rem; line-height:1.45; }
.footer { margin-top:50px; padding-top:22px; border-top:1px solid rgba(255,255,255,.12); display:flex; align-items:center; justify-content:space-between; gap:20px; color:#93a1ad; font-size:.72rem; }
.footer b { color:#fff; letter-spacing:.16em; }

.loader {
  position: fixed; inset:0; z-index:160; background:#f4f3ef;
  display:grid; place-items:center; transition:opacity .55s ease, visibility .55s ease;
}
.loader.off { opacity:0; visibility:hidden; pointer-events:none; }
.loader-box { width:min(470px,calc(100% - 48px)); }
.loader-logo { font-size:1.26rem; font-weight:950; letter-spacing:.22em; }
.loader-text { margin-top:14px; color:#75808a; font-size:.61rem; letter-spacing:.14em; }
.loader-track { height:1px; background:#d4d7d8; margin-top:20px; overflow:hidden; }
.loader-track span { display:block; width:0; height:100%; background:var(--blue); transition:width .22s ease; }
.fallback { position:fixed; z-index:100; inset:auto 22px 22px auto; padding:14px 16px; background:#fff; border:1px solid var(--line); box-shadow:var(--shadow); font-size:.72rem; }

@media (max-width: 900px) {
  .nav { position:fixed; top:72px; left:0; right:0; display:none; flex-direction:column; align-items:flex-start; background:#faf9f6; padding:24px; border-bottom:1px solid var(--line); }
  .nav.open { display:flex; }
  .menu { display:block; }
  .story { padding:100px 18px 36px; }
  .copy-card, .copy-card.right { width:min(100%,440px); margin-left:0; }
  .copy-card h1,.copy-card h2 { font-size:clamp(2.2rem,12vw,4rem); }
  .section-head { grid-template-columns:1fr; gap:20px; }
  .stats { grid-template-columns:1fr 1fr; }
  .services { grid-template-columns:1fr 1fr; }
  .products { grid-template-columns:1fr; }
  .contact-grid { grid-template-columns:1fr 1fr; }
  .world-caption { display:none; }
}
@media (max-width: 560px) {
  .stats,.services,.contact-grid { grid-template-columns:1fr; }
  .stage-dots { display:none; }
  .specs { grid-template-columns:1fr; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior:auto; }
  *,*::before,*::after { animation:none!important; transition:none!important; }
}
</style>
</head>
<body>
<div class="loader" id="loader">
  <div class="loader-box">
    <div class="loader-logo">ALLUCO</div>
    <div class="loader-text" id="loaderText">BUILDING THE INDUSTRIAL WORLD...</div>
    <div class="loader-track"><span id="loaderBar"></span></div>
  </div>
</div>

<header class="header">
  <a class="brand" href="#home" aria-label="ALLUCO home"><span class="brand-mark"></span><span>ALLUCO</span></a>
  <nav class="nav" id="nav">
    <a href="#supply">Supply</a>
    <a href="#port">Logistics</a>
    <a href="#warehouse">Stock</a>
    <a href="#products">Aluminium</a>
    <a class="contact-link" href="#contact">Contact</a>
  </nav>
  <button class="menu" id="menu" aria-label="Open menu"><span></span><span></span></button>
</header>

<canvas id="webgl" aria-hidden="true"></canvas>
<div class="world-wash" aria-hidden="true"></div>
<div class="world-caption" id="worldCaption">ALLUCO GLOBAL LOGISTICS</div>
<div class="stage-dots" id="stageDots">
  <button data-go="home"></button>
  <button data-go="supply"></button>
  <button data-go="fleet"></button>
  <button data-go="port"></button>
  <button data-go="warehouse"></button>
  <button data-go="aluminium"></button>
</div>

<main>
  <section class="story hero" id="home" data-scene="0">
    <article class="copy-card">
      <p class="kicker">ALUMINIUM / IMPORT / EXPORT / TUNISIA</p>
      <h1>ALLUCO.<br><span>ONE CONNECTED WORLD.</span></h1>
      <p>A continuous 3D industrial landscape connecting international sourcing, transport, maritime operations, warehouse stock and aluminium systems.</p>
      <div class="actions"><a class="btn primary" href="#supply">Explore the flow</a><a class="btn" href="#company">About ALLUCO</a></div>
    </article>
  </section>

  <section class="story" id="supply" data-scene="1">
    <article class="copy-card">
      <p class="kicker">01 / INTERNATIONAL SUPPLY</p>
      <h2>From global sourcing<br>to a single hub.</h2>
      <p>The journey starts at the air terminal and international supply zone. Every route converges toward the same ALLUCO network.</p>
      <div class="specs"><div><span>Network</span><b>International</b></div><div><span>Gateway</span><b>Tunisia</b></div><div><span>Flow</span><b>Connected</b></div></div>
    </article>
  </section>

  <section class="story" id="fleet" data-scene="2">
    <article class="copy-card right">
      <p class="kicker">02 / ALLUCO ROAD FLEET</p>
      <h2>The brand<br>in motion.</h2>
      <p>ALLUCO-branded trucks move through a shared road network linking terminal, port, warehouse and distribution areas.</p>
      <div class="specs"><div><span>Fleet</span><b>ALLUCO</b></div><div><span>Cargo</span><b>Aluminium</b></div><div><span>Mode</span><b>Road</b></div></div>
    </article>
  </section>

  <section class="story" id="port" data-scene="3">
    <article class="copy-card">
      <p class="kicker">03 / MARITIME LOGISTICS</p>
      <h2>Port. Vessel.<br>Containers.</h2>
      <p>A container ship, gantry cranes and cargo stacks form the maritime layer of the supply chain. The same route continues directly into the port.</p>
      <div class="specs"><div><span>Mode</span><b>Sea freight</b></div><div><span>Handling</span><b>Gantry</b></div><div><span>Unit</span><b>Container</b></div></div>
    </article>
  </section>

  <section class="story" id="warehouse" data-scene="4">
    <article class="copy-card right">
      <p class="kicker">04 / ALLUCO WAREHOUSE</p>
      <h2>Receive. Store.<br>Prepare.</h2>
      <p>The camera enters the ALLUCO industrial site: racks, forklift operations and aluminium stock are part of the same visual logistics chain.</p>
      <div class="specs"><div><span>Stock</span><b>Profiles</b></div><div><span>Handling</span><b>Forklift</b></div><div><span>Status</span><b>Ready</b></div></div>
    </article>
  </section>

  <section class="story" id="aluminium" data-scene="5">
    <article class="copy-card">
      <p class="kicker">05 / ALUMINIUM SYSTEMS</p>
      <h2>From logistics<br>to architecture.</h2>
      <p>The journey ends on the product itself: extruded aluminium profiles and architectural systems designed for demanding projects.</p>
      <div class="specs"><div><span>Material</span><b>Aluminium</b></div><div><span>Finish</span><b>Premium</b></div><div><span>Use</span><b>Architecture</b></div></div>
    </article>
  </section>

  <section class="content" id="company">
    <div class="wrap">
      <p class="section-kicker">ALLUCO / INDUSTRIAL PLATFORM</p>
      <div class="section-head">
        <h2>Industrial capability behind every aluminium system.</h2>
        <p>Founded in 2008 and part of the Demco group, ALLUCO develops architectural aluminium systems with integrated industrial, finishing, stock and logistics capabilities.</p>
      </div>
      <div class="stats">
        <article><strong>2008</strong><span>Company founded</span></article>
        <article><strong>11,750 m2</strong><span>Industrial site announced</span></article>
        <article><strong>350 t/month</strong><span>Production capacity announced</span></article>
        <article><strong>600+</strong><span>Profiles / dies developed</span></article>
        <article><strong>450+</strong><span>Colours and finishes</span></article>
        <article><strong>10 years</strong><span>Surface treatment warranty announced</span></article>
      </div>
    </div>
  </section>

  <section class="content alt">
    <div class="wrap">
      <p class="section-kicker">CAPABILITIES</p>
      <div class="section-head"><h2>Engineering, finishing and distribution.</h2><p>A premium aluminium offer depends on more than the profile itself: design, finishing, stock and distribution work as one operating system.</p></div>
      <div class="services">
        <article><span class="index">01</span><h3>Product engineering</h3><p>Architectural aluminium systems, technical development and continuous R&amp;D for demanding project requirements.</p></article>
        <article><span class="index">02</span><h3>Surface finishing</h3><p>Industrial finishing capabilities with a wide palette of colours and effects for architectural applications.</p></article>
        <article><span class="index">03</span><h3>Logistics platform</h3><p>Strategic stock, organised shipping and international distribution through a connected logistics network.</p></article>
      </div>
    </div>
  </section>

  <section class="content" id="products">
    <div class="wrap">
      <p class="section-kicker">ALUMINIUM SYSTEMS</p>
      <div class="section-head"><h2>A portfolio organised by application.</h2><p>ALLUCO publicly presents systems for doors and windows, indoor solutions, outdoor applications, guardrails and fencing.</p></div>
      <div class="products">
        <article><h3>Door &amp; Window Systems</h3><ul><li>ALTO 15400</li><li>KLIMA 7400</li><li>OIKOS 4700</li><li>Prima 6300</li><li>SUPRA 6000</li><li>Square 40 / Square 67</li></ul></article>
        <article><h3>Indoor</h3><ul><li>Dressing Alluco</li><li>Parolit shower partition</li><li>Folding and sliding doors</li><li>Glass interior doors</li><li>Pivot doors</li><li>VEROLIT interior glazing</li></ul></article>
        <article><h3>Outdoor</h3><ul><li>Roller shutter slats</li><li>Pergola Azore</li></ul></article>
        <article><h3>Guardrails &amp; Fencing</h3><ul><li>BlendLine guardrail</li><li>Gates and fencing solutions</li></ul></article>
      </div>
    </div>
  </section>

  <section class="content contact" id="contact">
    <div class="wrap">
      <p class="section-kicker">CONTACT</p>
      <div class="section-head"><h2>Build the next aluminium project.</h2><p>Public contact details from ALLUCO.</p></div>
      <div class="contact-grid">
        <a href="mailto:info@alluco.com"><span>Email</span><strong>info@alluco.com</strong></a>
        <a href="tel:+21670284142"><span>Soukra</span><strong>+216 70 284 142</strong></a>
        <a href="tel:+21670284140"><span>Moknine</span><strong>+216 70 284 140</strong></a>
        <div><span>Soukra showroom</span><strong>64 BIS Av. Fattouma Bourguiba, Tunis</strong></div>
      </div>
      <div class="footer"><b>ALLUCO</b><span>Aluminium / Systems / Logistics / International</span></div>
    </div>
  </section>
</main>
<div class="fallback" id="fallback" hidden>3D unavailable. The ALLUCO content remains accessible.</div>

<script>
(() => {
'use strict';
const $ = (s) => document.querySelector(s);
const $$ = (s) => [...document.querySelectorAll(s)];
const loader = $('#loader');
const loaderBar = $('#loaderBar');
const loaderText = $('#loaderText');
const canvas = $('#webgl');
const fallback = $('#fallback');
const sections = $$('[data-scene]');
const stageButtons = $$('#stageDots button');
const worldCaption = $('#worldCaption');
const mobile = matchMedia('(max-width:900px)').matches;
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

$('#menu').addEventListener('click', () => $('#nav').classList.toggle('open'));
$$('#nav a').forEach(a => a.addEventListener('click', () => $('#nav').classList.remove('open')));
stageButtons.forEach(b => b.addEventListener('click', () => document.getElementById(b.dataset.go).scrollIntoView({behavior:'smooth'})));

function progress(n, text) {
  loaderBar.style.width = n + '%';
  if (text) loaderText.textContent = text;
}
progress(10, 'INITIALISING ALLUCO WORLD...');

function webglAvailable() {
  try {
    const c = document.createElement('canvas');
    return !!(window.WebGLRenderingContext && (c.getContext('webgl2') || c.getContext('webgl')));
  } catch (_) { return false; }
}
if (!window.THREE || !webglAvailable()) {
  fallback.hidden = false;
  canvas.style.display = 'none';
  progress(100, 'READY');
  setTimeout(() => loader.classList.add('off'), 350);
  return;
}

const THREE = window.THREE;
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xf4f3ef);
scene.fog = new THREE.FogExp2(0xf4f3ef, mobile ? 0.0068 : 0.0046);

let frustum = mobile ? 24 : 30;
const aspect = innerWidth / innerHeight;
const camera = new THREE.OrthographicCamera(-frustum*aspect, frustum*aspect, frustum, -frustum, 0.1, 1000);
camera.position.set(88, 92, 110);
camera.lookAt(24, 0, 0);

const renderer = new THREE.WebGLRenderer({canvas, antialias: !mobile, powerPreference:'high-performance', alpha:false});
renderer.setSize(innerWidth, innerHeight);
renderer.setPixelRatio(Math.min(devicePixelRatio, mobile ? 1.15 : 1.6));
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.04;
renderer.shadowMap.enabled = !mobile;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const C = {
  paper:0xf4f3ef, white:0xfaf9f6, concrete:0xe7e7e2, road:0xcfd1ce, line:0xf3f3ef,
  graphite:0x343b40, deep:0x161c20, steel:0x7d878d, alu:0xbcc4c9, alu2:0xe5e8e9,
  blue:0x1d6fb8, blue2:0x78add3, sage:0x8fb6a7, sage2:0xbacfc4, grass:0xdfe6de,
  sea:0xa7c9d6, wood:0xad845f, glass:0xbdd9e4, yellow:0xd8ad57
};
const M = {
  white:new THREE.MeshStandardMaterial({color:C.white,roughness:.78,metalness:.02}),
  concrete:new THREE.MeshStandardMaterial({color:C.concrete,roughness:.95,metalness:.02}),
  road:new THREE.MeshStandardMaterial({color:C.road,roughness:.96,metalness:.01}),
  line:new THREE.MeshStandardMaterial({color:C.line,roughness:.9}),
  graphite:new THREE.MeshStandardMaterial({color:C.graphite,roughness:.48,metalness:.38}),
  deep:new THREE.MeshStandardMaterial({color:C.deep,roughness:.55,metalness:.34}),
  steel:new THREE.MeshStandardMaterial({color:C.steel,roughness:.4,metalness:.72}),
  alu:new THREE.MeshStandardMaterial({color:C.alu,roughness:.28,metalness:.9}),
  alu2:new THREE.MeshStandardMaterial({color:C.alu2,roughness:.3,metalness:.76}),
  blue:new THREE.MeshStandardMaterial({color:C.blue,roughness:.34,metalness:.35}),
  sage:new THREE.MeshStandardMaterial({color:C.sage,roughness:.82}),
  sage2:new THREE.MeshStandardMaterial({color:C.sage2,roughness:.86}),
  grass:new THREE.MeshStandardMaterial({color:C.grass,roughness:1}),
  wood:new THREE.MeshStandardMaterial({color:C.wood,roughness:.74}),
  yellow:new THREE.MeshStandardMaterial({color:C.yellow,roughness:.54,metalness:.12}),
  glass:new THREE.MeshPhysicalMaterial({color:C.glass,roughness:.08,transmission:.28,transparent:true,opacity:.62})
};

scene.add(new THREE.HemisphereLight(0xffffff, 0xb6b1a8, 2.8));
const sun = new THREE.DirectionalLight(0xffffff, 4.2);
sun.position.set(65, 90, 45);
sun.castShadow = !mobile;
sun.shadow.mapSize.set(mobile ? 512 : 2048, mobile ? 512 : 2048);
sun.shadow.camera.left = -150; sun.shadow.camera.right = 150; sun.shadow.camera.top = 110; sun.shadow.camera.bottom = -110;
sun.shadow.bias = -0.00025;
scene.add(sun);
const fill = new THREE.DirectionalLight(0xcfe5f4, 1.05); fill.position.set(-70, 35, -45); scene.add(fill);

const world = new THREE.Group();
scene.add(world);

function mesh(group, geometry, material, pos=[0,0,0], rot=[0,0,0], cast=true) {
  const m = new THREE.Mesh(geometry, material);
  m.position.set(...pos); m.rotation.set(...rot);
  m.castShadow = cast && !mobile; m.receiveShadow = !mobile;
  group.add(m); return m;
}
function box(group, size, pos, material=M.alu, rot=[0,0,0], cast=true) { return mesh(group, new THREE.BoxGeometry(...size), material, pos, rot, cast); }
function cyl(group, r, depth, pos, material=M.alu, rot=[0,0,0], segments=24, cast=true) { return mesh(group, new THREE.CylinderGeometry(r,r,depth,segments), material, pos, rot, cast); }

function seeded(seed) {
  let t = seed >>> 0;
  return () => { t += 0x6D2B79F5; let r = Math.imul(t ^ t >>> 15, 1 | t); r ^= r + Math.imul(r ^ r >>> 7, 61 | r); return ((r ^ r >>> 14) >>> 0) / 4294967296; };
}
const rnd = seeded(7192008);

function brandMaterial(bg='#f9f9f6', fg='#1d6fb8', sub='ALUMINIUM SYSTEMS') {
  const c = document.createElement('canvas'); c.width=1024; c.height=256;
  const x=c.getContext('2d'); x.fillStyle=bg; x.fillRect(0,0,c.width,c.height);
  x.fillStyle=fg; x.font='900 110px Arial'; x.textAlign='center'; x.textBaseline='middle'; x.fillText('ALLUCO',512,108);
  x.font='700 28px Arial'; x.globalAlpha=.88; x.fillText(sub,512,194);
  const tx=new THREE.CanvasTexture(c); tx.colorSpace=THREE.SRGBColorSpace; tx.anisotropy=8;
  return new THREE.MeshStandardMaterial({map:tx, roughness:.43, metalness:.08});
}
const brandWhite = brandMaterial('#f9f9f6','#1d6fb8');
const brandBlue = brandMaterial('#1d6fb8','#ffffff');

function makeRibbon(curve, width, y, material, segments=180) {
  const positions=[]; const uvs=[]; const indices=[];
  for(let i=0;i<=segments;i++) {
    const t=i/segments; const p=curve.getPointAt(t); const tangent=curve.getTangentAt(t).normalize();
    const normal=new THREE.Vector3(-tangent.z,0,tangent.x).normalize().multiplyScalar(width/2);
    positions.push(p.x+normal.x,y,p.z+normal.z, p.x-normal.x,y,p.z-normal.z);
    uvs.push(0,t,1,t);
    if(i<segments) { const a=i*2,b=a+1,c=a+2,d=a+3; indices.push(a,c,b,c,d,b); }
  }
  const g=new THREE.BufferGeometry(); g.setAttribute('position',new THREE.Float32BufferAttribute(positions,3)); g.setAttribute('uv',new THREE.Float32BufferAttribute(uvs,2)); g.setIndex(indices); g.computeVertexNormals();
  return mesh(world,g,material,[0,0,0],[0,0,0],false);
}

// Ground and soft industrial islands
mesh(world,new THREE.PlaneGeometry(300,170),M.grass,[35,-2.35,0],[-Math.PI/2,0,0],false);
box(world,[62,.16,46],[-67,-2.23,-28],M.white);
box(world,[58,.16,44],[36,-2.23,-37],M.white);
box(world,[58,.16,52],[90,-2.23,28],M.white);
box(world,[46,.16,40],[132,-2.23,4],M.white);

// Curved roads and branches
const mainRoadPts=[[-86,23],[-70,17],[-53,13],[-34,16],[-16,11],[2,14],[20,8],[38,5],[56,10],[72,19],[91,24],[111,17],[132,8],[151,4]];
const mainRoad=new THREE.CatmullRomCurve3(mainRoadPts.map(p=>new THREE.Vector3(p[0],-2.13,p[1])),false,'catmullrom',.22);
makeRibbon(mainRoad,5.2,-2.12,M.road);
makeRibbon(mainRoad,.09,-2.055,M.line);
const portRoadPts=[[18,9],[22,-3],[30,-16],[40,-26],[50,-33],[61,-36]];
const portRoad=new THREE.CatmullRomCurve3(portRoadPts.map(p=>new THREE.Vector3(p[0],-2.13,p[1])),false,'catmullrom',.25);
makeRibbon(portRoad,4.3,-2.11,M.road,120); makeRibbon(portRoad,.08,-2.045,M.line,120);
const whRoadPts=[[69,18],[75,26],[84,33],[96,35],[108,31]];
const whRoad=new THREE.CatmullRomCurve3(whRoadPts.map(p=>new THREE.Vector3(p[0],-2.13,p[1])),false,'catmullrom',.25);
makeRibbon(whRoad,4.1,-2.11,M.road,100); makeRibbon(whRoad,.08,-2.045,M.line,100);

// Trees and landscape details
function tree(x,z,s=1) {
  const g=new THREE.Group(); g.position.set(x,-1.75,z); world.add(g);
  cyl(g,.10*s,1.3*s,[0,.15,0],M.wood,[0,0,0],12);
  const crown=mesh(g,new THREE.IcosahedronGeometry(.72*s,1),rnd()>.5?M.sage:M.sage2,[0,1.2*s,0]); crown.scale.y=1.25;
}
const treeCount=mobile?34:72;
for(let i=0;i<treeCount;i++) {
  const x=-105+rnd()*265, z=-62+rnd()*120;
  const nearMain=mainRoadPts.some(p=>Math.hypot(x-p[0],z-p[1])<7);
  const reserved=(x<-45&&z<-8)||(x>14&&x<72&&z<-18)||(x>65&&z>16)||(x>112&&z>-15&&z<25);
  if(!nearMain&&!reserved) tree(x,z,.62+rnd()*.48);
}

// Airport and terminal
const airport=new THREE.Group(); airport.position.set(-66,0,-29); world.add(airport);
box(airport,[54,.12,24],[0,-2.14,0],M.concrete);
box(airport,[48,.10,5],[0,-2.04,-7.5],M.graphite);
for(let x=-20;x<=20;x+=6) box(airport,[2.6,.025,.10],[x,-1.98,-7.5],M.line,[0,0,0],false);
box(airport,[20,4.6,6],[2,.15,5.4],M.white); box(airport,[20,.2,6.1],[2,2.55,5.4],M.graphite);
box(airport,[18,.85,.06],[2,.45,8.45],M.glass);
for(let x=-5;x<=9;x+=7){ box(airport,[3.6,.26,.26],[x,.3,1.1],M.steel); box(airport,[.26,2.2,.26],[x-1.6,-.6,1.1],M.steel); }

function aircraft(scale=.65) {
  const g=new THREE.Group(); g.scale.setScalar(scale);
  cyl(g,.58,7.8,[0,0,0],M.alu2,[0,0,Math.PI/2],28);
  const nose=mesh(g,new THREE.ConeGeometry(.60,1.45,28),M.alu2,[4.6,0,0],[0,0,-Math.PI/2]);
  box(g,[3.4,.13,10.3],[.15,0,0],M.alu2);
  box(g,[1.5,1.7,.12],[-3.45,.8,0],M.blue,[0,0,-.08]);
  box(g,[1.55,.11,4.0],[-3.35,.55,0],M.alu);
  [-2.2,2.2].forEach(z=>cyl(g,.38,1.2,[.55,-.55,z],M.graphite,[Math.PI/2,0,0],20));
  return g;
}
const plane1=aircraft(.78); plane1.position.set(-72,-.65,-25); plane1.rotation.y=.05; world.add(plane1);
const plane2=aircraft(.62); plane2.position.set(-57,-.82,-22); plane2.rotation.y=-.08; world.add(plane2);
const taxiPlane=aircraft(.55); taxiPlane.position.set(-87,-.82,-36.5); world.add(taxiPlane);

// Headquarters / city cluster
function office(x,z,w,d,h,accent=false) {
  const g=new THREE.Group(); g.position.set(x,-2.15,z); world.add(g);
  box(g,[w,h,d],[0,h/2,0],M.white); box(g,[w+.14,.18,d+.14],[0,h+.08,0],accent?M.blue:M.graphite);
  for(let yy=1;yy<h-1;yy+=1.35) box(g,[w*.78,.20,.04],[0,yy,d/2+.03],M.glass);
  return g;
}
office(-26,30,12,9,7,true); office(-10,32,9,8,5,false); office(-39,30,8,7,4,false);

// Trucks
function wheel(g,p,r=.36) { return cyl(g,r,.22,p,M.deep,[0,0,Math.PI/2],18); }
function truck() {
  const g=new THREE.Group();
  box(g,[2.1,1.75,1.78],[-3.0,.68,0],M.white);
  box(g,[1.4,.58,1.53],[-3.0,1.04,0],M.glass);
  box(g,[.8,.24,1.83],[-1.65,.12,0],M.graphite);
  box(g,[5.75,2.12,1.9],[1.45,.82,0],M.white);
  mesh(g,new THREE.PlaneGeometry(5.0,1.25),brandWhite,[1.46,1.00,.96],[0,0,0],false);
  mesh(g,new THREE.PlaneGeometry(5.0,1.25),brandWhite,[1.46,1.00,-.96],[0,Math.PI,0],false);
  box(g,[5.85,.10,1.97],[1.45,1.92,0],M.alu);
  [-3.05,-1.72,2.10,3.35].forEach(x=>[.96,-.96].forEach(z=>wheel(g,[x,-.22,z],x>1?.34:.40)));
  box(g,[.16,1.6,.10],[-4.05,.60,.72],M.blue);
  return g;
}
const fleet=[];
for(let i=0;i<8;i++){const g=truck();g.scale.setScalar(.73);world.add(g);fleet.push({g,curve:i<5?mainRoad:portRoad,offset:(i%5)/5+.06*(i>4),speed:.010+.001*(i%3)});}

// Port and sea
mesh(world,new THREE.PlaneGeometry(68,42),new THREE.MeshStandardMaterial({color:C.sea,roughness:.27,metalness:.03,transparent:true,opacity:.63}),[48,-2.15,-49],[-Math.PI/2,0,0],false);
const port=new THREE.Group(); port.position.set(40,0,-36); world.add(port);
box(port,[46,.22,18],[0,-2.08,3],M.concrete);

function container(g,p,material=M.graphite,s=.8){
  const q=new THREE.Group();q.position.set(...p);q.scale.setScalar(s);g.add(q);
  box(q,[3.2,1.46,1.42],[0,0,0],material);
  for(let x=-1.28;x<=1.28;x+=.50) box(q,[.038,1.22,1.44],[x,0,0],M.steel);
  return q;
}
for(let x=-18;x<=10;x+=3.55){
  for(let z=-1;z<=9;z+=3.0){
    if(rnd()>.22){container(port,[x,-1.15,z],rnd()>.84?M.blue:(rnd()>.55?M.graphite:M.steel),.74); if(rnd()>.52) container(port,[x,-.07,z],rnd()>.82?M.blue:M.graphite,.74);}
  }
}

function gantry(x,z,s=1){
  const g=new THREE.Group();g.position.set(x,0,z);g.scale.setScalar(s);port.add(g);
  [-4.3,4.3].forEach(px=>{box(g,[.32,9.4,.32],[px,2.7,0],M.graphite);box(g,[1.2,.18,.18],[px,6.8,1.2],M.steel,[0,0,-.55]);});
  box(g,[9.3,.36,.36],[0,7.25,0],M.graphite);box(g,[12.4,.20,.20],[1.5,6.55,0],M.steel);
  return g;
}
const crane1=gantry(13,0,1.0); const crane2=gantry(2,0,.88); const crane3=gantry(-9,0,.78);
const craneLoad=container(crane1,[1.3,2.2,0],M.blue,.72);
const craneCable=box(crane1,[.05,4.3,.05],[1.3,4.5,0],M.steel);

const ship=new THREE.Group();ship.position.set(56,-.42,-51);world.add(ship);
const hullShape=new THREE.Shape();hullShape.moveTo(-12,-1);hullShape.lineTo(8.7,-1);hullShape.lineTo(12,-.25);hullShape.lineTo(9,1.25);hullShape.lineTo(-10.2,1.25);hullShape.lineTo(-12,.22);hullShape.closePath();
const hullGeo=new THREE.ExtrudeGeometry(hullShape,{depth:5.2,bevelEnabled:true,bevelSize:.14,bevelThickness:.14,bevelSegments:2});hullGeo.translate(0,0,-2.6);mesh(ship,hullGeo,M.deep);
box(ship,[17,.35,5.35],[-.5,1.42,0],M.steel);box(ship,[3.2,4.0,3.5],[-8.2,3.2,0],M.white);box(ship,[2.45,.92,3.0],[-8.2,4.32,0],M.glass);
let si=0;[-5,-1.4,2.2,5.8].forEach(x=>[-1.45,0,1.45].forEach(z=>{container(ship,[x,2.28,z],si++%6===0?M.blue:M.graphite,.63); if(x<3.5)container(ship,[x,3.25,z],si++%7===0?M.blue:M.steel,.63);}));

// Warehouse
const wh=new THREE.Group();wh.position.set(92,0,34);world.add(wh);
box(wh,[34,.22,24],[0,-2.08,0],M.concrete);
for(let x=-16;x<=16;x+=8){box(wh,[.22,8.4,.22],[x,1.95,-10.7],M.steel);box(wh,[.22,8.4,.22],[x,1.95,10.7],M.steel);}
box(wh,[34,.30,24],[0,6.05,0],new THREE.MeshStandardMaterial({color:0xe8e9e7,transparent:true,opacity:.76,roughness:.78}));
box(wh,[34,3.2,.34],[0,4.0,-10.85],M.white);
mesh(wh,new THREE.PlaneGeometry(11.5,2.1),brandBlue,[0,4.30,-11.04],[0,Math.PI,0],false);

for(const side of[-1,1]){
  for(let i=0;i<5;i++){
    const x=-13+i*6;
    for(let h=0;h<4;h++){
      box(wh,[5.0,.12,1.6],[x+2.1,-1.18+h*1.55,side*6.3],M.steel);
      if(h<3){box(wh,[1.35,.44,1.10],[x+1.1,-.88+h*1.55,side*6.3],M.alu2);box(wh,[1.35,.44,1.10],[x+3.0,-.88+h*1.55,side*6.3],i%2?M.graphite:M.blue);}
    }
  }
}
const forklift=new THREE.Group();forklift.position.set(-7,-.93,0);wh.add(forklift);
box(forklift,[2.2,1.12,1.62],[0,0,0],M.graphite);box(forklift,[1.05,.92,1.45],[-.48,.78,0],M.glass);box(forklift,[.14,3.1,.14],[1.05,.85,.55],M.steel);box(forklift,[.14,3.1,.14],[1.05,.85,-.55],M.steel);
box(forklift,[2.25,.08,.08],[2.08,-.43,.48],M.steel);box(forklift,[2.25,.08,.08],[2.08,-.43,-.48],M.steel);box(forklift,[.48,.24,1.62],[-.82,.28,0],M.blue);
[[-.7,.84],[-.7,-.84],[.75,.84],[.75,-.84]].forEach((p,i)=>wheel(forklift,[p[0],-.68,p[1]],i<2?.44:.34));
const pallet=new THREE.Group();pallet.position.set(3.0,-.16,0);forklift.add(pallet);box(pallet,[2.6,.12,1.4],[0,0,0],M.wood);for(let i=0;i<10;i++)box(pallet,[2.42,.075,.10],[0,.16+i*.10,-.5+(i%3)*.5],M.alu2);

// Aluminium yard and profile hero
const alu=new THREE.Group();alu.position.set(133,0,6);world.add(alu);
box(alu,[28,.18,24],[0,-2.12,0],M.concrete);
for(let i=0;i<22;i++){const row=Math.floor(i/11);box(alu,[12,.20,.20],[-4,-1.40+(i%11)*.28,-2.2+row*4.4],M.alu2);}
const prof=new THREE.Group();prof.position.set(4.5,2.4,0);alu.add(prof);
const sh=new THREE.Shape();sh.moveTo(-2.2,-2.2);sh.lineTo(2.2,-2.2);sh.lineTo(2.2,2.2);sh.lineTo(-2.2,2.2);sh.closePath();
const hole=new THREE.Path();hole.moveTo(-1.5,-1.5);hole.lineTo(-1.5,1.5);hole.lineTo(1.5,1.5);hole.lineTo(1.5,-1.5);hole.closePath();sh.holes.push(hole);
const pg=new THREE.ExtrudeGeometry(sh,{depth:6.2,bevelEnabled:true,bevelSize:.06,bevelThickness:.06,bevelSegments:2});pg.translate(0,0,-3.1);mesh(prof,pg,M.alu2);
box(prof,[.25,3.75,6.35],[0,0,0],M.alu);box(prof,[3.75,.25,6.35],[0,0,0],M.alu);

// Small wayfinding markers
function marker(x,z){const g=new THREE.Group();g.position.set(x,-1.78,z);world.add(g);mesh(g,new THREE.RingGeometry(.35,.52,32),new THREE.MeshBasicMaterial({color:C.blue,side:THREE.DoubleSide,transparent:true,opacity:.78}),[0,0,0],[-Math.PI/2,0,0],false);return g;}
[[-66,-29],[-15,12],[42,-36],[92,34],[133,6]].forEach(p=>marker(p[0],p[1]));

progress(66,'CONNECTING AIR, ROAD, PORT AND WAREHOUSE...');

// Camera storyboard: one world, multiple cinematic views
const cameraStops=[
  {pos:[78,92,112],target:[24,0,0],zoom:.72,caption:'ALLUCO GLOBAL LOGISTICS'},
  {pos:[-42,42,50],target:[-64,0,-25],zoom:1.10,caption:'INTERNATIONAL SUPPLY'},
  {pos:[15,36,44],target:[4,-1,11],zoom:1.18,caption:'ALLUCO ROAD FLEET'},
  {pos:[72,39,30],target:[43,0,-38],zoom:1.12,caption:'PORT AND MARITIME LOGISTICS'},
  {pos:[118,39,65],target:[92,0,34],zoom:1.10,caption:'ALLUCO WAREHOUSE'},
  {pos:[160,28,38],target:[133,1,6],zoom:1.25,caption:'ALUMINIUM SYSTEMS'}
];
let wantedPos=new THREE.Vector3(...cameraStops[0].pos);
let wantedTarget=new THREE.Vector3(...cameraStops[0].target);
let wantedZoom=cameraStops[0].zoom;
camera.position.copy(wantedPos);camera.zoom=wantedZoom;camera.updateProjectionMatrix();camera.lookAt(wantedTarget);
const va=new THREE.Vector3(),vb=new THREE.Vector3();
let currentScene=0;

function scrollState(){
  const y=scrollY+innerHeight*.48;let idx=0,local=0;
  for(let i=0;i<sections.length;i++){
    const a=sections[i].offsetTop;
    const b=i<sections.length-1?sections[i+1].offsetTop:document.documentElement.scrollHeight;
    if(y>=a&&y<b){idx=i;local=THREE.MathUtils.clamp((y-a)/Math.max(1,b-a),0,1);break;}
  }
  return {idx,local};
}
function smooth(t){return t*t*(3-2*t);}
function updateCamera(){
  const s=scrollState();currentScene=s.idx;
  stageButtons.forEach((b,i)=>b.classList.toggle('active',i===s.idx));
  const a=cameraStops[s.idx]||cameraStops[cameraStops.length-1];
  const b=cameraStops[Math.min(s.idx+1,cameraStops.length-1)];
  const t=reduced?0:smooth(s.local);
  wantedPos.copy(va.set(...a.pos).lerp(vb.set(...b.pos),t));
  wantedTarget.copy(va.set(...a.target).lerp(vb.set(...b.target),t));
  wantedZoom=THREE.MathUtils.lerp(a.zoom,b.zoom,t);
  camera.position.lerp(wantedPos,reduced?1:.055);
  camera.zoom=THREE.MathUtils.lerp(camera.zoom,wantedZoom,reduced?1:.055);camera.updateProjectionMatrix();
  camera.lookAt(wantedTarget);
  worldCaption.textContent=a.caption;
  worldCaption.classList.toggle('show',s.idx>0);
  // Scroll-driven operational actions
  if(s.idx===3){const lift=s.local;craneLoad.position.y=2.2-lift*2.35;craneCable.scale.y=.5+lift*.6;craneCable.position.y=4.5-lift*.85;}
  if(s.idx===4){forklift.position.x=-7+s.local*9;}
  if(s.idx===5){prof.rotation.y=s.local*.9;prof.rotation.x=s.local*.08;}
}

const clock=new THREE.Clock();
function animate(){
  const t=clock.getElapsedTime();updateCamera();
  if(!reduced){
    fleet.forEach((o,i)=>{const u=(t*o.speed+o.offset)%1;const p=o.curve.getPointAt(u),tan=o.curve.getTangentAt(u);o.g.position.copy(p);o.g.position.y=-1.42;o.g.rotation.y=-Math.atan2(tan.z,tan.x);});
    taxiPlane.position.x=-87+(t*.7)%38;taxiPlane.position.z=-36.5;
    ship.position.x=56+Math.sin(t*.16)*.28;ship.position.y=-.42+Math.sin(t*.48)*.035;
    if(currentScene!==4) forklift.position.z=Math.sin(t*.38)*.18;
    if(currentScene!==5) prof.rotation.y=t*.07;
  }
  renderer.render(scene,camera);requestAnimationFrame(animate);
}

addEventListener('resize',()=>{
  const a=innerWidth/innerHeight;frustum=mobile?24:30;
  camera.left=-frustum*a;camera.right=frustum*a;camera.top=frustum;camera.bottom=-frustum;camera.updateProjectionMatrix();
  renderer.setSize(innerWidth,innerHeight);renderer.setPixelRatio(Math.min(devicePixelRatio,mobile?1.15:1.6));
});

progress(92,'FINALISING ALLUCO EXPERIENCE...');
requestAnimationFrame(()=>{animate();progress(100,'READY');setTimeout(()=>loader.classList.add('off'),420);});
})();
</script>
</body>
</html>'''

components.html(SITE_HTML, height=1000, scrolling=True)
