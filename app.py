import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ALLUCO | Aluminium Logistics World",
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
    overflow: hidden !important;
    background: #eef2ee !important;
}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"], footer, #MainMenu { display: none !important; }
[data-testid="stMain"], [data-testid="stMainBlockContainer"], .block-container {
    padding: 0 !important; margin: 0 !important; max-width: 100% !important; width: 100% !important;
}
[data-testid="stVerticalBlock"] { gap: 0 !important; }
iframe {
    position: fixed !important; inset: 0 !important; width: 100vw !important; height: 100vh !important;
    min-height: 100vh !important; border: 0 !important; display: block !important;
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
<meta name="theme-color" content="#eef2ee" />
<title>ALLUCO | Aluminium Logistics World</title>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<style>
:root{
  --bg:#eef2ee; --paper:#f7f8f5; --ink:#16191c; --muted:#666f73; --line:rgba(22,25,28,.12);
  --blue:#1670b8; --blue2:#67a9dc; --glass:rgba(247,248,245,.82); --shadow:0 24px 70px rgba(40,50,53,.13);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;overflow-x:hidden}
a{color:inherit;text-decoration:none}button{font:inherit}
#webgl{position:fixed;inset:0;width:100%;height:100%;display:block;z-index:0}
.world-wash{position:fixed;inset:0;z-index:1;pointer-events:none;background:linear-gradient(90deg,rgba(238,242,238,.30),transparent 30%,transparent 78%,rgba(238,242,238,.16))}
.loader{position:fixed;inset:0;z-index:500;background:#eef2ee;display:grid;place-items:center;transition:opacity .5s,visibility .5s}
.loader.off{opacity:0;visibility:hidden;pointer-events:none}
.loader-box{width:min(410px,calc(100% - 44px))}.loader-brand{font-size:1.2rem;font-weight:950;letter-spacing:.2em}.loader-copy{margin-top:14px;color:#75807c;font-size:.62rem;letter-spacing:.14em;text-transform:uppercase}
.loader-line{height:2px;background:#d8ded9;margin-top:20px;overflow:hidden}.loader-line span{display:block;width:0;height:100%;background:var(--blue);transition:width .22s}
.topbar{position:fixed;left:0;right:0;top:0;height:68px;z-index:80;padding:0 clamp(20px,3.6vw,58px);display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);background:rgba(247,248,245,.74);backdrop-filter:blur(18px)}
.brand{display:flex;align-items:center;gap:10px;font-weight:930;letter-spacing:.17em;font-size:.82rem}.brand-symbol{width:31px;height:31px;border:1px solid rgba(22,25,28,.14);display:grid;place-items:center;background:linear-gradient(145deg,#fff,#c3cbd0);font-size:.72rem;color:var(--blue);font-weight:950}
.nav{display:flex;align-items:center;gap:8px}.nav a{padding:9px 12px;border-radius:999px;font-size:.62rem;text-transform:uppercase;letter-spacing:.12em;font-weight:800;color:#657074;transition:.2s}.nav a:hover,.nav a.active{background:#fff;color:#171a1d;box-shadow:0 6px 22px rgba(40,50,53,.08)}
.nav .contact{border:1px solid var(--line);background:rgba(255,255,255,.55)}
.menu{display:none;border:0;background:transparent;padding:8px}.menu span{display:block;width:20px;height:1px;background:#1b1f21;margin:5px 0}
main{position:relative;z-index:4}
.chapter{height:100svh;min-height:720px;position:relative;pointer-events:none}
.chapter-card{position:absolute;left:clamp(22px,4.6vw,76px);bottom:clamp(64px,8vh,110px);width:min(360px,calc(100vw - 44px));padding:22px 22px 20px;background:rgba(247,248,245,.88);border:1px solid rgba(22,25,28,.10);box-shadow:var(--shadow);backdrop-filter:blur(18px);pointer-events:auto}
.chapter-card .kicker{margin:0 0 12px;font-size:.57rem;letter-spacing:.19em;color:var(--blue);font-weight:900;text-transform:uppercase}.chapter-card h1,.chapter-card h2{margin:0;font-size:clamp(2.1rem,3.7vw,4.1rem);line-height:.92;letter-spacing:-.055em;font-weight:670}.chapter-card h1 strong,.chapter-card h2 strong{font-weight:900}.chapter-card p{margin:16px 0 0;color:var(--muted);font-size:.82rem;line-height:1.62;max-width:315px}.actions{margin-top:18px;display:flex;gap:7px;flex-wrap:wrap}.pill{pointer-events:auto;padding:9px 12px;border-radius:999px;border:1px solid var(--line);background:#fff;font-size:.58rem;letter-spacing:.10em;text-transform:uppercase;font-weight:850}.pill.primary{background:var(--blue);color:#fff;border-color:var(--blue)}
.scene-title{position:fixed;right:clamp(22px,3.5vw,55px);top:88px;z-index:30;text-align:right;pointer-events:none}.scene-title span{display:block;font-size:.52rem;letter-spacing:.18em;color:#82908d;text-transform:uppercase}.scene-title strong{display:block;margin-top:4px;font-size:.76rem;letter-spacing:.08em}
.progress{position:fixed;right:clamp(20px,2.2vw,36px);bottom:28px;z-index:45;display:flex;flex-direction:column;gap:7px}.progress button{width:9px;height:9px;padding:0;border-radius:50%;border:1px solid rgba(22,25,28,.28);background:rgba(255,255,255,.7);cursor:pointer;transition:.25s}.progress button.on{background:var(--blue);border-color:var(--blue);box-shadow:0 0 0 5px rgba(22,112,184,.10)}
.bottom-tools{position:fixed;left:clamp(22px,4.6vw,76px);bottom:22px;z-index:48;display:flex;gap:6px}.bottom-tools button{width:34px;height:34px;border-radius:50%;border:1px solid var(--line);background:rgba(247,248,245,.82);backdrop-filter:blur(14px);display:grid;place-items:center;color:#687274;font-size:.67rem;cursor:pointer}.bottom-tools button:hover{background:#fff;color:var(--blue)}
.metric{position:fixed;left:clamp(22px,4.6vw,76px);top:88px;z-index:25;padding:9px 11px;border:1px solid var(--line);background:rgba(247,248,245,.74);backdrop-filter:blur(14px);font-size:.55rem;letter-spacing:.12em;text-transform:uppercase;color:#65706d}
.content{position:relative;z-index:10;background:#f7f8f5;border-top:1px solid var(--line);padding:110px clamp(22px,5vw,82px)}
.content-wrap{width:min(1240px,100%);margin:auto}.section-kicker{margin:0 0 18px;color:var(--blue);font-size:.61rem;letter-spacing:.19em;text-transform:uppercase;font-weight:900}.section-head{display:grid;grid-template-columns:1.15fr .85fr;gap:50px;align-items:end;margin-bottom:44px}.section-head h2{margin:0;font-size:clamp(2.7rem,5vw,5.5rem);line-height:.94;letter-spacing:-.055em}.section-head p{margin:0;color:var(--muted);line-height:1.72}.stats{display:grid;grid-template-columns:repeat(3,1fr);border-left:1px solid var(--line);border-top:1px solid var(--line)}.stats article{padding:26px;min-height:125px;background:#fff;border-right:1px solid var(--line);border-bottom:1px solid var(--line);display:flex;flex-direction:column;justify-content:space-between}.stats strong{font-size:clamp(1.9rem,3vw,3.2rem);letter-spacing:-.05em}.stats span{color:var(--muted);font-size:.73rem}.catalog{display:grid;grid-template-columns:repeat(2,1fr);border-top:1px solid var(--line);border-left:1px solid var(--line)}.catalog article{background:#fff;padding:28px;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}.catalog h3{margin:0 0 12px;font-size:1.25rem}.catalog p,.catalog li{color:var(--muted);line-height:1.62}.catalog ul{margin:12px 0 0;padding-left:18px}.contact-section{background:#151b20;color:#f3f6f7}.contact-section .section-kicker{color:#78b6e4}.contact-section .section-head p{color:#a5b0b7}.contact-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(255,255,255,.12);margin-top:30px}.contact-grid>*{padding:22px;background:#151b20;display:flex;flex-direction:column;gap:6px}.contact-grid span{font-size:.55rem;letter-spacing:.12em;color:#82929d;text-transform:uppercase}.contact-grid strong{font-size:.86rem}.footer{display:flex;justify-content:space-between;gap:20px;margin-top:50px;padding-top:20px;border-top:1px solid rgba(255,255,255,.12);color:#94a2ac;font-size:.7rem}.footer b{color:#fff;letter-spacing:.15em}
@media(max-width:900px){.nav{position:fixed;top:68px;left:0;right:0;display:none;flex-direction:column;align-items:flex-start;background:#f7f8f5;padding:18px;border-bottom:1px solid var(--line)}.nav.open{display:flex}.menu{display:block}.chapter-card{bottom:74px}.scene-title,.metric{display:none}.section-head{grid-template-columns:1fr;gap:20px}.stats{grid-template-columns:1fr 1fr}.contact-grid{grid-template-columns:1fr 1fr}.chapter{min-height:640px}}
@media(max-width:560px){.stats,.catalog,.contact-grid{grid-template-columns:1fr}.chapter-card h1,.chapter-card h2{font-size:2.35rem}.bottom-tools{display:none}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
</style>
</head>
<body>
<div class="loader" id="loader"><div class="loader-box"><div class="loader-brand">ALLUCO</div><div class="loader-copy" id="loaderText">Building connected logistics world...</div><div class="loader-line"><span id="loaderBar"></span></div></div></div>
<header class="topbar">
  <a href="#overview" class="brand"><span class="brand-symbol">A</span><span>ALLUCO</span></a>
  <nav class="nav" id="nav"><a href="#overview">World</a><a href="#road">Logistics</a><a href="#warehouse">Stock</a><a href="#products">Aluminium</a><a href="#company">Company</a><a href="#contact" class="contact">Contact</a></nav>
  <button class="menu" id="menu" aria-label="Menu"><span></span><span></span></button>
</header>
<canvas id="webgl"></canvas><div class="world-wash"></div>
<div class="scene-title"><span id="sceneIndex">01 / 07</span><strong id="sceneName">CONNECTED WORLD</strong></div>
<div class="metric" id="metric">ALLUCO • TUNISIA • INTERNATIONAL</div>
<div class="progress" id="progress">
  <button data-go="overview" class="on"></button><button data-go="airport"></button><button data-go="road"></button><button data-go="port"></button><button data-go="warehouse"></button><button data-go="aluminium"></button><button data-go="hq"></button>
</div>
<div class="bottom-tools"><button title="Overview" data-go="overview">01</button><button title="Port" data-go="port">03</button><button title="Warehouse" data-go="warehouse">05</button></div>
<main>
<section class="chapter" id="overview" data-scene="0"><article class="chapter-card"><p class="kicker">ALLUCO • ALUMINIUM • LOGISTICS</p><h1>One world.<br><strong>One connected flow.</strong></h1><p>A continuous miniature logistics landscape linking international sourcing, transport, port handling, stock and aluminium systems.</p><div class="actions"><a class="pill primary" href="#airport">Explore the world</a><a class="pill" href="#company">About ALLUCO</a></div></article></section>
<section class="chapter" id="airport" data-scene="1"><article class="chapter-card"><p class="kicker">01 • INTERNATIONAL SOURCING</p><h2>Global routes.<br><strong>Local precision.</strong></h2><p>The journey begins with suppliers, air links and international freight moving toward the Tunisian market.</p></article></section>
<section class="chapter" id="road" data-scene="2"><article class="chapter-card"><p class="kicker">02 • ALLUCO ROAD FLEET</p><h2>The brand<br><strong>in motion.</strong></h2><p>ALLUCO-branded trucks move through the same landscape, connecting terminal, port, warehouse and distribution routes.</p></article></section>
<section class="chapter" id="port" data-scene="3"><article class="chapter-card"><p class="kicker">03 • MARITIME LOGISTICS</p><h2>Port. Cargo.<br><strong>Containers.</strong></h2><p>Gantry cranes, stacked cargo and a container vessel form the maritime layer of the supply chain.</p></article></section>
<section class="chapter" id="warehouse" data-scene="4"><article class="chapter-card"><p class="kicker">04 • ALLUCO WAREHOUSE</p><h2>Receive. Store.<br><strong>Prepare.</strong></h2><p>An open warehouse scene reveals racks, aluminium stock, handling zones and a forklift working inside the same world.</p></article></section>
<section class="chapter" id="aluminium" data-scene="5"><article class="chapter-card"><p class="kicker">05 • ALUMINIUM SYSTEMS</p><h2>From logistics<br><strong>to architecture.</strong></h2><p>The camera ends on the material itself: aluminium profiles and systems ready for architectural applications.</p></article></section>
<section class="chapter" id="hq" data-scene="6"><article class="chapter-card"><p class="kicker">06 • ALLUCO NETWORK</p><h2>Industry.<br><strong>Service. Innovation.</strong></h2><p>The logistics world resolves around ALLUCO as a connected industrial and commercial hub.</p><div class="actions"><a class="pill primary" href="#products">Discover systems</a></div></article></section>

<section class="content" id="company"><div class="content-wrap"><p class="section-kicker">ALLUCO</p><div class="section-head"><h2>Aluminium systems with an industrial backbone.</h2><p>Corporate presentation, product systems, logistics and contact information can live beneath the immersive experience without interrupting the 3D journey.</p></div><div class="stats"><article><strong>2008</strong><span>Foundation</span></article><article><strong>11,750 m²</strong><span>Industrial site announced</span></article><article><strong>350 t/month</strong><span>Production capacity announced</span></article><article><strong>600+</strong><span>Profiles / dies developed</span></article><article><strong>450+</strong><span>Colours and finishes</span></article><article><strong>10 years</strong><span>Surface-treatment warranty announced</span></article></div></div></section>
<section class="content" id="products"><div class="content-wrap"><p class="section-kicker">PRODUCT SYSTEMS</p><div class="section-head"><h2>Architectural aluminium by application.</h2><p>A clean catalogue layer for ALLUCO systems, technical references and future 2D / 3D product files.</p></div><div class="catalog"><article><h3>Door & Window Systems</h3><ul><li>ALTO 15400</li><li>KLIMA 7400</li><li>OIKOS 4700</li><li>Prima 6300</li><li>SUPRA 6000</li><li>Square 40 / Square 67</li></ul></article><article><h3>Indoor</h3><ul><li>Dressing Alluco</li><li>Parolit shower partition</li><li>Folding & sliding doors</li><li>Glass interior doors</li><li>Pivot doors</li><li>VEROLIT interior glazing</li></ul></article><article><h3>Outdoor</h3><ul><li>Roller shutter slats</li><li>Pergola Azore</li></ul></article><article><h3>Guardrails & Fencing</h3><ul><li>BlendLine guardrail</li><li>Gates & fencing</li></ul></article></div></div></section>
<section class="content contact-section" id="contact"><div class="content-wrap"><p class="section-kicker">CONTACT</p><div class="section-head"><h2>Build the next aluminium project.</h2><p>Public ALLUCO contact information.</p></div><div class="contact-grid"><a href="mailto:info@alluco.com"><span>Email</span><strong>info@alluco.com</strong></a><a href="tel:+21670284142"><span>Soukra</span><strong>+216 70 284 142</strong></a><a href="tel:+21670284140"><span>Moknine</span><strong>+216 70 284 140</strong></a><div><span>Soukra</span><strong>64 BIS Av. Fattouma Bourguiba, Tunis</strong></div></div><div class="footer"><b>ALLUCO</b><span>Aluminium • Systems • Logistics • International</span></div></div></section>
</main>
<script>
(()=>{
'use strict';
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const loader=$('#loader'),loaderBar=$('#loaderBar'),loaderText=$('#loaderText'),canvas=$('#webgl');
const sections=$$('[data-scene]'), progressBtns=$$('#progress button'), navLinks=$$('#nav a');
const sceneIndex=$('#sceneIndex'),sceneName=$('#sceneName');
const mobile=matchMedia('(max-width:900px)').matches, reduced=matchMedia('(prefers-reduced-motion:reduce)').matches;
$('#menu').addEventListener('click',()=>$('#nav').classList.toggle('open'));
navLinks.forEach(a=>a.addEventListener('click',()=>$('#nav').classList.remove('open')));
$$('[data-go]').forEach(b=>b.addEventListener('click',()=>{const el=document.getElementById(b.dataset.go);if(el)el.scrollIntoView({behavior:'smooth'})}));
function load(n,t){loaderBar.style.width=n+'%';if(t)loaderText.textContent=t} load(12,'Preparing isometric world...');
function webglOK(){try{const c=document.createElement('canvas');return !!(window.WebGLRenderingContext&&(c.getContext('webgl2')||c.getContext('webgl')))}catch(e){return false}}
if(!window.THREE||!webglOK()){load(100,'3D unavailable');setTimeout(()=>loader.classList.add('off'),350);return}
const THREE=window.THREE;
const scene=new THREE.Scene(); scene.background=new THREE.Color(0xeef2ee); scene.fog=new THREE.FogExp2(0xeef2ee,mobile?.011:.0072);
const aspect=innerWidth/innerHeight, frustum=58;
const camera=new THREE.OrthographicCamera(-frustum*aspect/2,frustum*aspect/2,frustum/2,-frustum/2,.1,600);
const renderer=new THREE.WebGLRenderer({canvas,antialias:!mobile,powerPreference:'high-performance'});
renderer.setSize(innerWidth,innerHeight);renderer.setPixelRatio(Math.min(devicePixelRatio,mobile?1.15:1.55));renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.02;renderer.shadowMap.enabled=!mobile;renderer.shadowMap.type=THREE.PCFSoftShadowMap;
scene.add(new THREE.HemisphereLight(0xffffff,0xb9c0b9,2.7));
const sun=new THREE.DirectionalLight(0xffffff,3.7);sun.position.set(40,65,35);sun.castShadow=!mobile;sun.shadow.mapSize.set(1536,1536);sun.shadow.camera.left=-110;sun.shadow.camera.right=110;sun.shadow.camera.top=90;sun.shadow.camera.bottom=-90;scene.add(sun);
const fill=new THREE.DirectionalLight(0xcbe7ff,1.0);fill.position.set(-45,24,-35);scene.add(fill);
const world=new THREE.Group();scene.add(world);
const C={bg:0xeef2ee,white:0xf9faf6,concrete:0xe2e5e1,road:0xcfd3cf,road2:0xb6bdb9,graphite:0x2c3439,deep:0x151b20,steel:0x7b878c,alu:0xbec7cc,alu2:0xe8ecec,blue:0x1670b8,blue2:0x6eaddb,green:0x89b8a8,grass:0xdce6dd,sea:0xa7ccd8,wood:0xa37b55,glass:0xb9dae4,yellow:0xd9aa4f};
const M={white:new THREE.MeshStandardMaterial({color:C.white,roughness:.76,metalness:.03}),concrete:new THREE.MeshStandardMaterial({color:C.concrete,roughness:.9}),road:new THREE.MeshStandardMaterial({color:C.road,roughness:.95}),graphite:new THREE.MeshStandardMaterial({color:C.graphite,roughness:.48,metalness:.42}),deep:new THREE.MeshStandardMaterial({color:C.deep,roughness:.56,metalness:.35}),steel:new THREE.MeshStandardMaterial({color:C.steel,roughness:.42,metalness:.72}),alu:new THREE.MeshStandardMaterial({color:C.alu,roughness:.28,metalness:.9}),alu2:new THREE.MeshStandardMaterial({color:C.alu2,roughness:.3,metalness:.75}),blue:new THREE.MeshStandardMaterial({color:C.blue,roughness:.32,metalness:.35}),green:new THREE.MeshStandardMaterial({color:C.green,roughness:.83}),grass:new THREE.MeshStandardMaterial({color:C.grass,roughness:1}),wood:new THREE.MeshStandardMaterial({color:C.wood,roughness:.76}),yellow:new THREE.MeshStandardMaterial({color:C.yellow,roughness:.5}),glass:new THREE.MeshPhysicalMaterial({color:C.glass,roughness:.08,transmission:.25,transparent:true,opacity:.62})};
function mesh(g,geo,mat,pos=[0,0,0],rot=[0,0,0],cast=true){const m=new THREE.Mesh(geo,mat);m.position.set(...pos);m.rotation.set(...rot);m.castShadow=cast&&!mobile;m.receiveShadow=!mobile;g.add(m);return m}
function box(g,s,p,mat=M.alu,r=[0,0,0]){return mesh(g,new THREE.BoxGeometry(...s),mat,p,r)}
function cyl(g,r,d,p,mat=M.alu,rot=[0,0,0],seg=20){return mesh(g,new THREE.CylinderGeometry(r,r,d,seg),mat,p,rot)}
function textMat(text,bg='#1670b8',fg='#fff',sub=''){const c=document.createElement('canvas');c.width=1024;c.height=256;const x=c.getContext('2d');x.fillStyle=bg;x.fillRect(0,0,c.width,c.height);x.fillStyle=fg;x.textAlign='center';x.textBaseline='middle';x.font='900 108px Arial';x.fillText(text,512,108);if(sub){x.font='600 29px Arial';x.globalAlpha=.86;x.fillText(sub,512,194)}const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=8;return new THREE.MeshStandardMaterial({map:t,roughness:.4,metalness:.12})}
const allucoBlue=textMat('ALLUCO','#1670b8','#ffffff','ALUMINIUM SYSTEMS');const allucoWhite=textMat('ALLUCO','#f9faf6','#1670b8','ALUMINIUM SYSTEMS');
// terrain tiles
mesh(world,new THREE.PlaneGeometry(180,130),M.grass,[10,-2.5,0],[-Math.PI/2,0,0],false);
box(world,[58,.12,40],[-48,-2.42,19],M.white);box(world,[50,.12,38],[44,-2.42,-28],M.white);box(world,[42,.12,32],[38,-2.42,29],M.white);box(world,[34,.12,28],[-8,-2.42,-30],M.white);
// roads as flattened tubes
function roadCurve(points,width=2.7){const curve=new THREE.CatmullRomCurve3(points.map(p=>new THREE.Vector3(p[0],-2.34,p[1])),false,'catmullrom',.35);const geo=new THREE.TubeGeometry(curve,Math.max(80,points.length*24),width,8,false);const m=mesh(world,geo,M.road,[0,0,0],[0,0,0],false);m.scale.y=.035;return curve}
const mainRoad=roadCurve([[-68,28],[-56,22],[-42,22],[-28,15],[-14,9],[1,11],[16,8],[30,2],[43,1],[57,7],[68,17],[81,20],[96,13],[112,6],[128,4]],2.2);
roadCurve([[-14,9],[-18,-4],[-12,-16],[1,-26],[17,-34],[36,-37],[53,-34]],1.8);
roadCurve([[57,7],[55,20],[64,31],[79,38],[95,40]],1.75);
const winding=roadCurve([[-66,-28],[-58,-35],[-47,-32],[-42,-22],[-51,-15],[-63,-18],[-69,-11]],1.7);
// lane centers
function laneLine(points){const curve=new THREE.CatmullRomCurve3(points.map(p=>new THREE.Vector3(p[0],-2.24,p[1])),false,'catmullrom',.35);const geo=new THREE.TubeGeometry(curve,90,.06,5,false);const mm=new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:.5});const m=mesh(world,geo,mm,[0,0,0],[0,0,0],false);m.scale.y=.06}
laneLine([[-68,28],[-56,22],[-42,22],[-28,15],[-14,9],[1,11],[16,8],[30,2],[43,1],[57,7],[68,17],[81,20],[96,13],[112,6],[128,4]]);
function tree(x,z,s=1){const g=new THREE.Group();g.position.set(x,-2.1,z);world.add(g);cyl(g,.09,1.2,[0,.3,0],M.wood);const crown=mesh(g,new THREE.IcosahedronGeometry(.75*s,1),M.green,[0,1.25,0]);crown.scale.y=1.35}
for(let i=0;i<82;i++){const x=-76+Math.random()*210,z=-50+Math.random()*100;if(Math.abs(z-9)<5&&x>-65&&x<130)continue;tree(x,z,.55+Math.random()*.5)}
function building(x,z,w,d,h,accent=false){const g=new THREE.Group();g.position.set(x,-2.32,z);world.add(g);box(g,[w,h,d],[0,h/2,0],M.white);box(g,[w+.12,.18,d+.12],[0,h+.09,0],accent?M.blue:M.graphite);for(let wx=-w*.35;wx<=w*.35;wx+=2.2)box(g,[.9,.48,.05],[wx,h*.62,d/2+.03],M.glass);return g}
building(-4,23,18,11,7,true);building(-25,31,10,8,5,false);building(75,-3,14,9,7,false);building(99,28,12,9,8,true);
// airport
const airport=new THREE.Group();airport.position.set(-46,0,21);world.add(airport);box(airport,[36,.12,28],[0,-2.34,0],M.white);box(airport,[21,4.2,6],[3,-.2,7],M.white);box(airport,[21,.18,6.2],[3,2.0,7],M.graphite);box(airport,[19,1.0,.06],[3,.55,10.05],M.glass);for(let i=-12;i<=12;i+=6)box(airport,[.17,3.7,.17],[i,-.4,-4],M.steel);
function aircraft(scale=.62){const g=new THREE.Group();g.scale.setScalar(scale);cyl(g,.5,7.0,[0,0,0],M.alu2,[0,0,Math.PI/2],24);mesh(g,new THREE.ConeGeometry(.53,1.3,24),M.alu2,[4.15,0,0],[0,0,-Math.PI/2]);box(g,[3.0,.1,9.0],[.1,0,0],M.alu2);box(g,[1.2,1.45,.11],[-3.0,.68,0],M.blue,[0,0,-.12]);box(g,[1.3,.08,3.8],[-3.0,.3,0],M.alu2);return g}
const plane1=aircraft(.76);plane1.position.set(-50,-.92,15);world.add(plane1);const plane2=aircraft(.56);plane2.position.set(-37,-1.02,12);plane2.rotation.y=.12;world.add(plane2);const plane3=aircraft(.50);plane3.position.set(-38,-1.05,30);plane3.rotation.y=-.08;world.add(plane3);
// trucks
function wheel(g,p,r=.34){return cyl(g,r,.2,p,M.deep,[0,0,Math.PI/2],18)}
function truck(){const g=new THREE.Group();box(g,[2.05,1.72,1.72],[-2.75,.63,0],M.white);box(g,[1.3,.58,1.48],[-2.75,.95,0],M.glass);box(g,[.9,.32,1.78],[-1.75,.08,0],M.graphite);box(g,[5.3,2.02,1.82],[1.45,.77,0],M.white);mesh(g,new THREE.PlaneGeometry(4.7,1.13),allucoBlue,[1.45,1.0,.92],[0,0,0],false);mesh(g,new THREE.PlaneGeometry(4.7,1.13),allucoBlue,[1.45,1.0,-.92],[0,Math.PI,0],false);[-2.8,-1.65,1.95,3.0].forEach(x=>[.91,-.91].forEach(z=>wheel(g,[x,-.2,z],x>1?.30:.36)));return g}
const trucks=[];for(let i=0;i<9;i++){const g=truck();g.scale.setScalar(.68);world.add(g);trucks.push({g,offset:i/9,speed:.0085+(i%3)*.0012})}
// distribution yard / rail impression
const railZone=new THREE.Group();railZone.position.set(18,-.05,-4);world.add(railZone);box(railZone,[34,.12,18],[0,-2.32,0],M.white);
for(let r=-5;r<=5;r+=5){box(railZone,[31,.08,.13],[0,-2.18,r],M.graphite);box(railZone,[31,.04,.04],[0,-2.11,r+.32],M.steel);box(railZone,[31,.04,.04],[0,-2.11,r-.32],M.steel)}
const gantry=new THREE.Group();gantry.position.set(4,0,0);railZone.add(gantry);[-7,7].forEach(x=>box(gantry,[.42,10,.42],[x,2.4,0],M.blue));box(gantry,[15,.55,.55],[0,7.2,0],M.blue);box(gantry,[15,.28,6.5],[0,6.6,0],M.blue);
for(let i=0;i<7;i++){const tg=truck();tg.scale.setScalar(.55);tg.position.set(-10+i*4.3,-1.1,(i%2?3:-3));railZone.add(tg)}
// port and sea
const port=new THREE.Group();port.position.set(46,0,-34);world.add(port);mesh(world,new THREE.PlaneGeometry(55,34),new THREE.MeshStandardMaterial({color:C.sea,roughness:.28,metalness:.04,transparent:true,opacity:.66}),[52,-2.33,-48],[-Math.PI/2,0,0],false);box(port,[40,.16,17],[0,-2.31,3],M.white);
function container(g,p,mat=M.graphite,s=.75){const q=new THREE.Group();q.position.set(...p);q.scale.setScalar(s);g.add(q);box(q,[3.0,1.4,1.35],[0,0,0],mat);for(let x=-1.2;x<=1.2;x+=.46)box(q,[.035,1.18,1.37],[x,0,0],M.steel);return q}
for(let x=-16;x<=9;x+=3.3)for(let z=-3;z<=7;z+=2.9){if(Math.random()>.23){container(port,[x,-1.1,z],Math.random()>.82?M.blue:M.graphite,.72);if(Math.random()>.55)container(port,[x,-.1,z],Math.random()>.88?M.blue:M.steel,.72)}}
function portCrane(x,z,s=1){const g=new THREE.Group();g.position.set(x,0,z);g.scale.setScalar(s);port.add(g);[-4,4].forEach(px=>box(g,[.30,9,.30],[px,2.5,0],M.graphite));box(g,[8.6,.34,.34],[0,6.95,0],M.graphite);box(g,[11,.20,.20],[1.1,6.35,0],M.steel);return g}
portCrane(12,1,1.0);portCrane(3,1,.9);portCrane(-6,1,.78);
const ship=new THREE.Group();ship.position.set(54,-.58,-48);world.add(ship);const hs=new THREE.Shape();hs.moveTo(-10,-.8);hs.lineTo(7.6,-.8);hs.lineTo(9.7,-.05);hs.lineTo(7.7,1.05);hs.lineTo(-8.4,1.05);hs.lineTo(-10,.18);hs.closePath();const hg=new THREE.ExtrudeGeometry(hs,{depth:4.7,bevelEnabled:true,bevelSize:.10,bevelThickness:.10,bevelSegments:2});hg.translate(0,0,-2.35);mesh(ship,hg,M.deep);box(ship,[14,.28,4.8],[-.5,1.25,0],M.steel);box(ship,[2.8,3.5,3.2],[-6.7,2.9,0],M.white);box(ship,[2.1,.85,2.7],[-6.7,4.0,0],M.glass);let ci=0;[-3.7,-.4,2.9].forEach(x=>[-1.25,0,1.25].forEach(z=>{container(ship,[x,2.05,z],ci++%6===0?M.blue:M.graphite,.62);if(x<1||Math.abs(z)<.2)container(ship,[x,3.0,z],ci++%7===0?M.blue:M.steel,.62)}));
// warehouse
const wh=new THREE.Group();wh.position.set(84,0,38);world.add(wh);box(wh,[32,.16,24],[0,-2.31,0],M.white);for(let x=-15;x<=15;x+=7.5){box(wh,[.18,8,.18],[x,1.65,-10.4],M.steel);box(wh,[.18,8,.18],[x,1.65,10.4],M.steel)}box(wh,[32,.25,24],[0,5.7,0],new THREE.MeshStandardMaterial({color:0xe8eae7,transparent:true,opacity:.80,roughness:.75}));box(wh,[32,3,.28],[0,3.7,-10.5],M.white);mesh(wh,new THREE.PlaneGeometry(11,2.0),allucoBlue,[0,4.05,-10.66],[0,Math.PI,0],false);
for(const side of[-1,1])for(let i=0;i<5;i++){const x=-12+i*5.5;for(let h=0;h<4;h++){box(wh,[4.7,.11,1.6],[x+2,-1.22+h*1.45,side*6.0],M.steel);if(h<3){box(wh,[1.35,.45,1.08],[x+1.0,-.92+h*1.45,side*6.0],M.alu2);box(wh,[1.35,.45,1.08],[x+2.9,-.92+h*1.45,side*6.0],i%2?M.graphite:M.blue)}}}
const forklift=new THREE.Group();forklift.position.set(-6,-1.0,0);wh.add(forklift);box(forklift,[2.0,1.05,1.55],[0,0,0],M.graphite);box(forklift,[.95,.88,1.4],[-.42,.73,0],M.glass);box(forklift,[.12,3.0,.12],[.95,.8,.5],M.steel);box(forklift,[.12,3.0,.12],[.95,.8,-.5],M.steel);box(forklift,[2.0,.08,.08],[1.9,-.4,.44],M.steel);box(forklift,[2.0,.08,.08],[1.9,-.4,-.44],M.steel);[[-.6,.8],[-.6,-.8],[.65,.8],[.65,-.8]].forEach((p,i)=>wheel(forklift,[p[0],-.64,p[1]],i<2?.40:.31));box(forklift,[.45,.2,1.5],[-.78,.24,0],M.blue);const pal=new THREE.Group();pal.position.set(2.6,-.14,0);forklift.add(pal);box(pal,[2.35,.10,1.3],[0,0,0],M.wood);for(let i=0;i<9;i++)box(pal,[2.2,.08,.09],[0,.15+i*.10,-.45+(i%3)*.45],M.alu2);
// aluminium profiles
const alu=new THREE.Group();alu.position.set(120,0,5);world.add(alu);for(let i=0;i<18;i++)box(alu,[12,.18,.18],[-1,-1.35+(i%9)*.30,-1.6+Math.floor(i/9)*3.2],M.alu2);const profile=new THREE.Group();profile.position.set(3.0,2.1,0);alu.add(profile);const sh=new THREE.Shape();sh.moveTo(-2,-2);sh.lineTo(2,-2);sh.lineTo(2,2);sh.lineTo(-2,2);sh.closePath();const hole=new THREE.Path();hole.moveTo(-1.4,-1.4);hole.lineTo(-1.4,1.4);hole.lineTo(1.4,1.4);hole.lineTo(1.4,-1.4);hole.closePath();sh.holes.push(hole);const pg=new THREE.ExtrudeGeometry(sh,{depth:5.3,bevelEnabled:true,bevelSize:.05,bevelThickness:.05,bevelSegments:2});pg.translate(0,0,-2.65);mesh(profile,pg,M.alu2);box(profile,[.22,3.5,5.45],[0,0,0],M.alu);box(profile,[3.5,.22,5.45],[0,0,0],M.alu);
// HQ / office landmark
const hq=new THREE.Group();hq.position.set(103,0,-23);world.add(hq);box(hq,[18,10,12],[0,2.5,0],M.white);box(hq,[18,.35,12],[0,7.7,0],M.blue);for(let y=0;y<4;y++)for(let x=-6;x<=6;x+=3)box(hq,[2.1,.9,.06],[x,-.2+y*1.9,6.03],y%2?M.glass:M.graphite);mesh(hq,new THREE.PlaneGeometry(8,1.65),allucoWhite,[0,5.5,6.05],[0,0,0],false);
// markers
function marker(x,z){const g=new THREE.Group();g.position.set(x,-2.1,z);world.add(g);mesh(g,new THREE.RingGeometry(.38,.55,32),new THREE.MeshBasicMaterial({color:C.blue,side:THREE.DoubleSide,transparent:true,opacity:.72}),[0,0,0],[-Math.PI/2,0,0],false);return g}marker(-46,21);marker(2,10);marker(46,-34);marker(84,38);marker(120,5);marker(103,-23);
// Camera state. Keep same isometric angle and pan/zoom through the world.
const sceneNames=['CONNECTED WORLD','INTERNATIONAL SOURCING','ALLUCO ROAD FLEET','MARITIME LOGISTICS','ALLUCO WAREHOUSE','ALUMINIUM SYSTEMS','ALLUCO NETWORK'];
const stops=[
 {target:[20,0,0],zoom:.74},
 {target:[-45,0,20],zoom:1.30},
 {target:[4,0,7],zoom:1.24},
 {target:[48,0,-34],zoom:1.20},
 {target:[84,0,37],zoom:1.26},
 {target:[120,0,5],zoom:1.42},
 {target:[103,0,-22],zoom:1.26},
];
const isoDir=new THREE.Vector3(1.15,1.05,1.15).normalize();let wantTarget=new THREE.Vector3(...stops[0].target),currentTarget=wantTarget.clone(),wantZoom=stops[0].zoom;camera.zoom=wantZoom;camera.updateProjectionMatrix();
function setCameraFromTarget(t){camera.position.copy(t).addScaledVector(isoDir,95);camera.lookAt(t)}setCameraFromTarget(currentTarget);
function state(){const y=scrollY+innerHeight*.48;let idx=0,local=0;for(let i=0;i<sections.length;i++){const a=sections[i].offsetTop,b=i<sections.length-1?sections[i+1].offsetTop:document.documentElement.scrollHeight;if(y>=a&&y<b){idx=i;local=THREE.MathUtils.clamp((y-a)/Math.max(1,b-a),0,1);break}}return{idx,local}}
const T1=new THREE.Vector3(),T2=new THREE.Vector3();let currentScene=0;
function updateCamera(){const s=state();currentScene=s.idx;const a=stops[s.idx]||stops.at(-1),b=stops[Math.min(s.idx+1,stops.length-1)],t=reduced?0:s.local*s.local*(3-2*s.local);wantTarget.copy(T1.set(...a.target).lerp(T2.set(...b.target),t));wantZoom=THREE.MathUtils.lerp(a.zoom,b.zoom,t);currentTarget.lerp(wantTarget,reduced?1:.07);camera.zoom=THREE.MathUtils.lerp(camera.zoom,wantZoom,reduced?1:.06);camera.updateProjectionMatrix();setCameraFromTarget(currentTarget);progressBtns.forEach((btn,i)=>btn.classList.toggle('on',i===s.idx));sceneIndex.textContent=String(s.idx+1).padStart(2,'0')+' / 07';sceneName.textContent=sceneNames[s.idx]||sceneNames.at(-1);navLinks.forEach(a=>{const id=a.getAttribute('href')?.slice(1);a.classList.toggle('active',id&&id===sections[s.idx]?.id)});forklift.position.x=-6+(s.idx===4?s.local*8:0);profile.rotation.y=(s.idx===5?s.local*.8:0)}
const clock=new THREE.Clock();
function animate(){const t=clock.getElapsedTime();updateCamera();if(!reduced){trucks.forEach((o,i)=>{const u=(t*o.speed+o.offset)%1,p=mainRoad.getPointAt(u),tan=mainRoad.getTangentAt(u);o.g.position.copy(p);o.g.position.y=-1.56;o.g.rotation.y=-Math.atan2(tan.z,tan.x)});plane1.position.x=-50+Math.sin(t*.12)*1.2;ship.position.x=54+Math.sin(t*.16)*.3;ship.position.y=-.58+Math.sin(t*.45)*.03;forklift.position.z=Math.sin(t*.35)*.18;profile.rotation.z=Math.sin(t*.2)*.015}renderer.render(scene,camera);requestAnimationFrame(animate)}
addEventListener('resize',()=>{const a=innerWidth/innerHeight;camera.left=-frustum*a/2;camera.right=frustum*a/2;camera.top=frustum/2;camera.bottom=-frustum/2;camera.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight);renderer.setPixelRatio(Math.min(devicePixelRatio,mobile?1.15:1.55))});
load(76,'Linking road, port, warehouse and aluminium...');requestAnimationFrame(()=>{animate();load(100,'Ready');setTimeout(()=>loader.classList.add('off'),430)});
})();
</script>
</body>
</html>'''

components.html(SITE_HTML, height=1000, scrolling=True)
