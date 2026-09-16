import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ALLUCO | Aluminium • International",
    page_icon="A",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Interface Streamlit invisible: the website occupies the full viewport.
st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"], .stApp {
        margin: 0 !important;
        padding: 0 !important;
        background: #eef3f7 !important;
        overflow: hidden !important;
      }
      [data-testid="stHeader"],
      [data-testid="stToolbar"],
      [data-testid="stDecoration"],
      [data-testid="stStatusWidget"],
      footer,
      #MainMenu { display: none !important; }
      [data-testid="stMain"] { padding: 0 !important; overflow: hidden !important; }
      [data-testid="stMainBlockContainer"], .block-container {
        max-width: 100% !important;
        width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe {
        position: fixed !important;
        inset: 0 !important;
        display: block !important;
        width: 100vw !important;
        height: 100vh !important;
        min-height: 100vh !important;
        border: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

SITE_HTML = r'''<!doctype html>
<html lang="fr" data-theme="light">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#eef3f7" />
  <meta name="description" content="ALLUCO — systèmes architecturaux en aluminium, distribution, logistique et présence internationale." />
  <title>ALLUCO | Aluminium • Systèmes • International</title>
  
  <script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<style>
:root {
  --bg: #eef3f7;
  --bg2: #f9fbfc;
  --ink: #0f1720;
  --muted: #5c6875;
  --line: rgba(15, 23, 32, .12);
  --glass: rgba(255,255,255,.72);
  --glass-strong: rgba(255,255,255,.90);
  --blue: #1167d8;
  --blue-2: #4ea1ff;
  --shadow: 0 28px 80px rgba(37,54,71,.14);
}
html[data-theme="dark"] {
  --bg: #070b10;
  --bg2: #0e141b;
  --ink: #f4f7fa;
  --muted: #97a4b1;
  --line: rgba(255,255,255,.11);
  --glass: rgba(14,20,27,.72);
  --glass-strong: rgba(10,15,21,.92);
  --blue: #3697ff;
  --blue-2: #8bc5ff;
  --shadow: 0 28px 80px rgba(0,0,0,.28);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; background: var(--bg); }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  overflow-x: hidden;
  transition: background .35s ease, color .35s ease;
}
a { color: inherit; text-decoration: none; }
button { font: inherit; }

#webgl { position: fixed; inset: 0; width: 100%; height: 100%; z-index: 0; display: block; }
.scene-wash {
  position: fixed; inset: 0; z-index: 1; pointer-events: none;
  background:
    radial-gradient(circle at 72% 42%, rgba(17,103,216,.07), transparent 32%),
    linear-gradient(90deg, color-mix(in srgb, var(--bg) 82%, transparent) 0%, transparent 45%, color-mix(in srgb, var(--bg) 10%, transparent) 100%);
}

.topbar {
  position: fixed; z-index: 50; inset: 0 0 auto 0; min-height: 78px;
  padding: 16px clamp(20px, 4vw, 62px);
  display: flex; align-items: center; justify-content: space-between; gap: 28px;
  background: color-mix(in srgb, var(--bg2) 74%, transparent);
  border-bottom: 1px solid var(--line); backdrop-filter: blur(18px);
}
.brand { display: flex; align-items: center; gap: 11px; font-weight: 850; letter-spacing: .16em; font-size: .93rem; }
.brand-mark {
  width: 34px; height: 34px; display: grid; place-items: center; color: transparent;
  background: linear-gradient(145deg, #d9e0e5, #7f8c99);
  clip-path: polygon(50% 0,100% 100%,70% 100%,50% 55%,30% 100%,0 100%);
  filter: drop-shadow(0 6px 12px rgba(15,23,32,.12));
}
.nav { display: flex; align-items: center; gap: 27px; text-transform: uppercase; letter-spacing: .12em; font-size: .72rem; font-weight: 700; color: var(--muted); }
.nav a { transition: color .2s ease; } .nav a:hover { color: var(--ink); }
.nav-contact { border: 1px solid var(--line); padding: 11px 16px; border-radius: 999px; background: var(--glass); }
.nav-actions { display: flex; align-items: center; gap: 10px; }
.theme-toggle, .menu { border: 1px solid var(--line); background: var(--glass); color: var(--ink); border-radius: 999px; cursor: pointer; }
.theme-toggle { width: 46px; height: 38px; display: grid; place-items: center; overflow: hidden; }
.theme-toggle__moon { display: none; } html[data-theme="dark"] .theme-toggle__sun { display: none; } html[data-theme="dark"] .theme-toggle__moon { display: inline; }
.menu { display: none; width: 44px; height: 38px; padding: 0 11px; }
.menu span { display:block; width: 20px; height: 1px; background: currentColor; margin: 5px 0; }

main { position: relative; z-index: 5; }
.panel {
  min-height: 100svh; padding: 124px clamp(26px, 7vw, 110px) 82px;
  display: flex; align-items: center; position: relative;
}
.align-right { justify-content: flex-end; }
.hero { min-height: 112svh; align-items: center; }
.hero-copy { width: min(720px, 72vw); position: relative; z-index: 8; }
.eyebrow, .chapter { margin: 0 0 18px; color: var(--blue); font-size: .70rem; font-weight: 800; letter-spacing: .18em; text-transform: uppercase; }
.hero h1 { margin: 0; max-width: 850px; font-size: clamp(3.6rem, 7.7vw, 8.4rem); line-height: .88; letter-spacing: -.065em; font-weight: 850; }
.hero h1 span { color: var(--blue); }
.lead { max-width: 620px; margin: 30px 0 0; font-size: clamp(1.05rem, 1.55vw, 1.35rem); line-height: 1.7; color: var(--muted); }
.hero-actions { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 34px; }
.btn { padding: 14px 20px; border-radius: 999px; font-size: .75rem; letter-spacing: .1em; text-transform: uppercase; font-weight: 800; }
.btn-primary { background: var(--ink); color: var(--bg); box-shadow: var(--shadow); }
.btn-ghost { border: 1px solid var(--line); background: var(--glass); }
.hero-stat { position: absolute; right: clamp(26px,7vw,110px); bottom: 54px; display: flex; flex-direction: column; text-align: right; gap: 5px; }
.hero-stat span { font-size: .64rem; letter-spacing: .18em; color: var(--muted); } .hero-stat b { font-size: .76rem; letter-spacing: .12em; }

.glass-card, .contact-card {
  width: min(600px, 47vw); padding: clamp(28px,4vw,50px); border: 1px solid var(--line); border-radius: 28px;
  background: linear-gradient(145deg, var(--glass-strong), var(--glass)); backdrop-filter: blur(22px);
  box-shadow: var(--shadow);
}
.glass-card h2, .contact-card h2 { margin: 0 0 22px; font-size: clamp(2.55rem,4.7vw,5rem); line-height: .98; letter-spacing: -.052em; }
.glass-card > p:not(.chapter), .contact-card > p:not(.chapter) { color: var(--muted); line-height: 1.75; font-size: 1.03rem; }
.chips { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 28px; }
.chips span { padding: 10px 12px; border-radius: 999px; border: 1px solid var(--line); color: var(--muted); font-size: .72rem; background: color-mix(in srgb, var(--glass) 82%, transparent); }
.spec-grid, .contact-grid { margin-top: 30px; display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.spec-grid div, .contact-grid div { border-top: 1px solid var(--line); padding-top: 13px; display: flex; flex-direction: column; gap: 5px; }
.spec-grid span, .contact-grid span { font-size: .62rem; letter-spacing: .13em; color: var(--muted); }
.spec-grid strong, .contact-grid strong { font-size: .82rem; }
.mini-kpis { margin-top: 28px; display: grid; grid-template-columns: repeat(4,1fr); gap: 8px; }
.mini-kpis span { padding: 12px 10px; border: 1px solid var(--line); border-radius: 14px; font-size: .72rem; color: var(--muted); }
.mini-kpis b { color: var(--blue); display: block; margin-bottom: 5px; }
.contact { justify-content: center; min-height: 108svh; }
.contact-card { width: min(900px, 86vw); text-align: center; }
.contact-grid { text-align: left; }

.flow-rail {
  position: fixed; z-index: 40; left: 50%; bottom: 20px; transform: translateX(-50%);
  width: min(680px, calc(100vw - 52px)); padding: 12px 16px 10px;
  display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px;
  border: 1px solid var(--line); border-radius: 18px; background: color-mix(in srgb, var(--bg2) 82%, transparent);
  backdrop-filter: blur(18px); box-shadow: 0 16px 50px rgba(37,54,71,.11);
}
.flow-line { position: absolute; height: 2px; left: 28px; right: 28px; top: 14px; background: var(--line); overflow: hidden; border-radius: 4px; }
.flow-line span { display: block; width: 0%; height: 100%; background: linear-gradient(90deg,var(--blue),var(--blue-2)); transition: width .15s linear; }
.flow-step { position: relative; padding-top: 10px; display: flex; flex-direction: column; align-items: center; gap: 2px; color: var(--muted); transition: color .25s ease; }
.flow-step::before { content:""; position:absolute; top:-1px; width:8px; height:8px; border-radius:50%; background:#c7d0d8; border:2px solid var(--bg2); box-shadow:0 0 0 1px var(--line); }
.flow-step.is-active { color: var(--ink); } .flow-step.is-active::before { background: var(--blue); box-shadow: 0 0 0 4px color-mix(in srgb,var(--blue) 15%, transparent); }
.flow-step b { font-size: .55rem; letter-spacing:.1em; } .flow-step span { font-size:.58rem; font-weight:800; letter-spacing:.11em; }

.loader { position: fixed; inset: 0; z-index: 100; display: grid; place-items: center; background: #eef3f7; transition: opacity .55s ease, visibility .55s ease; }
.loader.is-hidden { opacity: 0; visibility: hidden; pointer-events: none; }
.loader__box { width: min(450px, calc(100% - 50px)); }
.loader__brand { font-size: 1.35rem; font-weight: 900; letter-spacing: .23em; color: #0f1720; }
.loader__status { margin-top: 17px; font-size: .68rem; letter-spacing:.13em; color:#667381; }
.loader__track { height: 2px; margin-top: 22px; background: #d8e0e7; overflow:hidden; } .loader__track span { display:block; width:0; height:100%; background:#1167d8; transition:width .28s ease; }
.fallback { position: fixed; z-index: 60; right: 20px; bottom: 90px; padding: 14px 16px; border:1px solid var(--line); border-radius: 14px; background: var(--glass-strong); box-shadow: var(--shadow); display:flex; flex-direction:column; gap:3px; }

@media (max-width: 900px) {
  .nav { position: fixed; inset: 78px 0 auto 0; padding: 28px; background: var(--bg2); border-bottom:1px solid var(--line); display:none; flex-direction:column; align-items:flex-start; }
  .nav.is-open { display:flex; } .menu { display:block; }
  .panel { padding: 110px 22px 95px; }
  .hero-copy { width: 100%; }
  .hero h1 { font-size: clamp(3.2rem, 17vw, 6rem); }
  .glass-card, .contact-card { width: min(100%, 620px); }
  .align-right { justify-content: flex-start; }
  .flow-rail { bottom: 10px; width: calc(100vw - 20px); }
  .flow-step span { font-size:.5rem; }
  .hero-stat { display:none; }
}
@media (max-width: 560px) {
  .spec-grid, .contact-grid, .mini-kpis { grid-template-columns: 1fr; }
  .flow-step b { display:none; } .flow-rail { padding-left:8px; padding-right:8px; }
}
@media (prefers-reduced-motion: reduce) { html { scroll-behavior:auto; } *,*::before,*::after { animation:none !important; transition:none !important; } }

/* Institutional content */
.inline-cta{display:inline-flex;margin-top:22px}
.flow-rail{transition:opacity .25s ease,transform .25s ease}
.flow-rail.is-hidden{opacity:0;pointer-events:none;transform:translate(-50%,18px)}
.content-section{position:relative;z-index:12;padding:110px clamp(24px,6vw,96px);border-top:1px solid var(--line)}
.surface{background:var(--bg2)}
.surface-alt{background:color-mix(in srgb,var(--bg) 82%,white 18%)}
html[data-theme="dark"] .surface-alt{background:#0a1118}
.content-wrap{width:min(1320px,100%);margin:0 auto}
.section-kicker{margin:0 0 20px;color:var(--blue);font-size:.68rem;font-weight:850;letter-spacing:.19em;text-transform:uppercase}
.section-heading{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(280px,.85fr);gap:50px;align-items:end;margin-bottom:54px}
.section-heading.compact{grid-template-columns:1fr}
.section-heading h2,.academy-layout h2,.contact-hero h2{margin:0;font-size:clamp(2.8rem,5vw,5.8rem);line-height:.96;letter-spacing:-.055em}
.section-heading p,.academy-layout p,.contact-hero p{margin:0;color:var(--muted);font-size:1.05rem;line-height:1.75}
.stats-grid{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--line);border-radius:26px;overflow:hidden;background:var(--glass-strong);box-shadow:var(--shadow);margin-bottom:32px}
.stats-grid article{padding:30px;border-right:1px solid var(--line);border-bottom:1px solid var(--line);min-height:138px;display:flex;flex-direction:column;justify-content:space-between}.stats-grid article:nth-child(3n){border-right:0}.stats-grid article:nth-last-child(-n+3){border-bottom:0}
.stats-grid strong{font-size:clamp(2rem,3vw,3.5rem);letter-spacing:-.05em}.stats-grid span{color:var(--muted);font-size:.78rem;letter-spacing:.04em}
.three-col,.feature-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.info-card,.feature-grid article,.category-card,.tech-card,.reference-grid article,.location-grid article{border:1px solid var(--line);border-radius:22px;background:var(--glass);box-shadow:0 18px 50px rgba(40,55,70,.08)}
.info-card,.feature-grid article{padding:30px}.info-card>span,.feature-icon{display:inline-flex;min-width:42px;height:42px;align-items:center;justify-content:center;border-radius:12px;background:color-mix(in srgb,var(--blue) 12%,transparent);color:var(--blue);font-weight:850;font-size:.72rem}
.info-card h3,.feature-grid h3,.category-card h3,.tech-card h3{margin:24px 0 12px;font-size:1.4rem}.info-card p,.feature-grid p,.category-card li{color:var(--muted);line-height:1.65}
.feature-grid{grid-template-columns:repeat(3,1fr)}
.category-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}.category-card{padding:30px}.category-top{display:flex;align-items:flex-start;gap:16px}.category-top>span{color:var(--blue);font-weight:900;font-size:1.9rem}.category-top h3{margin:3px 0 0}.category-card ul{margin:24px 0 0;padding-left:18px}.category-card li+li{margin-top:9px}
.tech-compare{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px}.tech-card{padding:34px}.tech-label{margin:0;color:var(--blue);font-size:.65rem;letter-spacing:.18em;font-weight:850}.tech-card h3{font-size:2rem;margin:12px 0 24px}.tech-specs{display:grid;grid-template-columns:1fr 1fr;gap:10px}.tech-specs span{padding:12px 0;border-top:1px solid var(--line);color:var(--muted);font-size:.82rem}.tech-specs b{display:block;color:var(--ink);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px}
.reference-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.reference-grid article{padding:42px 26px;min-height:140px;display:flex;align-items:flex-end;font-weight:800;font-size:1.05rem;background:linear-gradient(145deg,color-mix(in srgb,var(--blue) 8%,var(--glass)),var(--glass))}
.location-layout{display:grid;gap:44px}.location-title{margin:0 0 18px;font-size:1.15rem}.location-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.location-grid article{padding:22px;display:flex;flex-direction:column;gap:8px}.location-grid b{font-size:.9rem}.location-grid span,.location-grid a{color:var(--muted);font-size:.78rem;line-height:1.5}.location-grid a:hover{color:var(--blue)}
.showroom-cards .info-card>span{min-width:auto;padding:0 12px}
.academy-layout{display:grid;grid-template-columns:1.2fr .8fr;gap:60px;align-items:center}.academy-layout h2{margin-bottom:24px}.academy-tags{display:flex;flex-wrap:wrap;gap:10px}.academy-tags span,.contact-types span{padding:13px 15px;border:1px solid var(--line);border-radius:999px;background:var(--glass);font-size:.76rem;font-weight:750}
.contact-section{background:linear-gradient(135deg,#0d1c2a,#101821);color:#f5f8fb}.contact-section .section-kicker{color:#67b4ff}.contact-section .contact-hero p{color:#a9b5c1}.contact-official-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:42px}.contact-official-grid>a,.contact-official-grid>div{padding:24px;border:1px solid rgba(255,255,255,.12);border-radius:18px;background:rgba(255,255,255,.055);display:flex;flex-direction:column;gap:8px}.contact-official-grid span{font-size:.62rem;letter-spacing:.13em;color:#8fa1b2;text-transform:uppercase}.contact-official-grid strong{font-size:.9rem;line-height:1.5}.contact-types{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}.contact-types span{border-color:rgba(255,255,255,.12);background:rgba(255,255,255,.05)}.footer-line{margin-top:60px;padding-top:24px;border-top:1px solid rgba(255,255,255,.12);display:flex;gap:20px;justify-content:space-between;align-items:center;color:#9cabb9;font-size:.75rem}.footer-line b{color:#fff;letter-spacing:.16em}.footer-line a{color:#67b4ff}
@media(max-width:1000px){.section-heading,.academy-layout{grid-template-columns:1fr;gap:22px}.stats-grid{grid-template-columns:repeat(2,1fr)}.stats-grid article:nth-child(3n){border-right:1px solid var(--line)}.stats-grid article:nth-child(2n){border-right:0}.stats-grid article:nth-last-child(-n+3){border-bottom:1px solid var(--line)}.stats-grid article:nth-last-child(-n+2){border-bottom:0}.three-col,.feature-grid,.location-grid{grid-template-columns:1fr 1fr}.reference-grid,.contact-official-grid{grid-template-columns:1fr 1fr}}
@media(max-width:680px){.content-section{padding:82px 20px}.stats-grid,.three-col,.feature-grid,.category-grid,.tech-compare,.reference-grid,.location-grid,.contact-official-grid{grid-template-columns:1fr}.stats-grid article{border-right:0!important;border-bottom:1px solid var(--line)!important}.stats-grid article:last-child{border-bottom:0!important}.tech-specs{grid-template-columns:1fr}.footer-line{align-items:flex-start;flex-direction:column}}
.category-note{color:var(--muted);line-height:1.65;margin:22px 0 0;font-size:.9rem}

</style>
</head>
<body>
  <div class="loader" id="loader">
    <div class="loader__box">
      <div class="loader__brand">ALLUCO</div>
      <div class="loader__status" id="loaderStatus">INITIALISATION DE LA CHAINE LOGISTIQUE...</div>
      <div class="loader__track"><span id="loaderBar"></span></div>
    </div>
  </div>

  <header class="topbar">
    <a class="brand" href="#home" aria-label="Accueil ALLUCO">
      <span class="brand-mark">A</span>
      <span>ALLUCO</span>
    </a>
    <nav class="nav" id="nav">
      <a href="#journey">Parcours</a>
      <a href="#company">Entreprise</a>
      <a href="#products">Produits</a>
      <a href="#locations">Implantations</a>
      <a href="#contact" class="nav-contact">Contact</a>
    </nav>
    <div class="nav-actions">
      <button class="theme-toggle" id="themeToggle" type="button" aria-label="Changer le thème">
        <span class="theme-toggle__sun">☀</span><span class="theme-toggle__moon">◐</span>
      </button>
      <button class="menu" id="menu" type="button" aria-label="Ouvrir le menu"><span></span><span></span></button>
    </div>
  </header>

  <canvas id="webgl" aria-hidden="true"></canvas>
  <div class="scene-wash" aria-hidden="true"></div>

  <aside class="flow-rail" id="flowRail" aria-label="Progression logistique">
    <div class="flow-line"><span id="flowProgress"></span></div>
    <div class="flow-step is-active" data-flow="0"><b>01</b><span>AIR</span></div>
    <div class="flow-step" data-flow="1"><b>02</b><span>MER</span></div>
    <div class="flow-step" data-flow="2"><b>03</b><span>PORT</span></div>
    <div class="flow-step" data-flow="3"><b>04</b><span>DEPOT</span></div>
    <div class="flow-step" data-flow="4"><b>05</b><span>ALU</span></div>
  </aside>

  <main>
    <section class="panel hero" id="home" data-scene="0">
      <div class="hero-copy">
        <p class="eyebrow">TUNISIE • ALUMINIUM • INTERNATIONAL</p>
        <h1>ALLUCO.<br><span>L'ALUMINIUM EN MOUVEMENT.</span></h1>
        <p class="lead">Une expérience 3D qui relie approvisionnement, transport, manutention, stockage et systèmes aluminium dans une seule chaîne visuelle.</p>
        <div class="hero-actions">
          <a href="#journey" class="btn btn-primary">Explorer le parcours</a>
          <a href="#products" class="btn btn-ghost">Voir les systèmes</a>
        </div>
      </div>
      <div class="hero-stat">
        <span>ALLUCO</span>
        <b>SYSTEMES ARCHITECTURAUX • DISTRIBUTION • INTERNATIONAL</b>
      </div>
    </section>

    <section class="panel" id="journey" data-scene="1">
      <article class="glass-card left-card">
        <p class="chapter">01 — SOURCING & CONNEXIONS</p>
        <h2>Des partenaires.<br>Un réseau connecté.</h2>
        <p>L'animation aérienne représente la coordination internationale des flux, des partenaires et des approvisionnements.</p>
        <div class="chips"><span>Partenaires</span><span>Approvisionnement</span><span>International</span></div>
      </article>
    </section>

    <section class="panel align-right" id="sea" data-scene="2">
      <article class="glass-card">
        <p class="chapter">02 — LOGISTIQUE MARITIME</p>
        <h2>Le conteneur avance.<br>La chaîne continue.</h2>
        <p>Le navire porte-conteneurs illustre les livraisons internationales et le transport coordonné des produits aluminium.</p>
        <div class="chips"><span>Navire cargo</span><span>Conteneurs</span><span>Routes maritimes</span></div>
      </article>
    </section>

    <section class="panel" id="port" data-scene="3">
      <article class="glass-card left-card">
        <p class="chapter">03 — OPERATIONS PORTUAIRES</p>
        <h2>Arrivée.<br>Déchargement. Transfert.</h2>
        <p>Le port relie transport maritime et distribution terrestre avec grue, conteneur et camion sur une même séquence animée.</p>
        <div class="chips"><span>Grue</span><span>Déchargement</span><span>Transport</span></div>
      </article>
    </section>

    <section class="panel align-right" id="warehouse" data-scene="4">
      <article class="glass-card">
        <p class="chapter">04 — STOCK & DISTRIBUTION</p>
        <h2>Forklift. Racks.<br>Disponibilité.</h2>
        <p>Le chariot élévateur réceptionne, déplace et range les charges dans un environnement de stockage industriel.</p>
        <div class="chips"><span>Forklift</span><span>Stockage</span><span>Distribution</span></div>
      </article>
    </section>

    <section class="panel" id="aluminium" data-scene="5">
      <article class="glass-card left-card">
        <p class="chapter">05 — SYSTEMES ALUMINIUM</p>
        <h2>La matière devient<br>solution architecturale.</h2>
        <p>La scène finale met l'accent sur les profilés et les systèmes aluminium destinés aux projets résidentiels, tertiaires et architecturaux.</p>
        <div class="spec-grid">
          <div><span>GAMMES</span><strong>Premium & Square</strong></div>
          <div><span>INDOOR</span><strong>8 produits</strong></div>
          <div><span>OUTDOOR</span><strong>2 produits</strong></div>
          <div><span>PORTE / FENETRE</span><strong>8 systèmes</strong></div>
        </div>
      </article>
    </section>

    <section class="panel align-right" id="network" data-scene="6">
      <article class="glass-card">
        <p class="chapter">06 — RESEAU CONNECTE</p>
        <h2>Industrie.<br>Logistique. Marché.</h2>
        <p>La chaîne 3D relie les étapes physiques à un réseau commercial et industriel présent en Tunisie et à l'international.</p>
        <div class="mini-kpis"><span><b>01</b> Concevoir</span><span><b>02</b> Produire</span><span><b>03</b> Distribuer</span><span><b>04</b> Accompagner</span></div>
      </article>
    </section>

    <section class="panel align-right" id="future" data-scene="7">
      <article class="glass-card">
        <p class="chapter">07 — ALLUCO</p>
        <h2>Innovation aluminium.<br>Présence internationale.</h2>
        <p>Découvrez ci-dessous les données institutionnelles, produits, implantations et coordonnées publiques d'ALLUCO.</p>
        <a class="btn btn-primary inline-cta" href="#company">Découvrir ALLUCO</a>
      </article>
    </section>

    <section class="content-section surface" id="company">
      <div class="content-wrap">
        <p class="section-kicker">ENTREPRISE</p>
        <div class="section-heading">
          <h2>ALLUCO en bref</h2>
          <p>Fondée en 2008 et intégrée au groupe Demco, ALLUCO développe des systèmes architecturaux en aluminium et accompagne des projets exigeants avec une approche orientée innovation, performance et service client.</p>
        </div>
        <div class="stats-grid">
          <article><strong>2008</strong><span>Année de fondation</span></article>
          <article><strong>11 750 m²</strong><span>Parc industriel annoncé</span></article>
          <article><strong>350 t/mois</strong><span>Capacité de production annoncée</span></article>
          <article><strong>600+</strong><span>Filières / profils développés</span></article>
          <article><strong>450+</strong><span>Teintes et finitions</span></article>
          <article><strong>10 ans</strong><span>Garantie annoncée sur traitements de surface</span></article>
        </div>
        <div class="three-col">
          <article class="info-card"><span>01</span><h3>Qualité & Innovation</h3><p>Investissement en R&D, conception 3D et outils techniques pour développer des solutions performantes et durables.</p></article>
          <article class="info-card"><span>02</span><h3>Satisfaction Client</h3><p>Conseil, accompagnement technique et commercial, suivi des commandes et assistance logistique.</p></article>
          <article class="info-card"><span>03</span><h3>Expertise & Performance</h3><p>Processus industriel, traitements de surface, gestion du stock et distribution internationale structurée.</p></article>
        </div>
      </div>
    </section>

    <section class="content-section surface-alt" id="industrial">
      <div class="content-wrap">
        <p class="section-kicker">CAPACITES INDUSTRIELLES</p>
        <div class="section-heading compact"><h2>Production, finition et logistique</h2></div>
        <div class="feature-grid">
          <article><div class="feature-icon">01</div><h3>Traitement de surface</h3><p>Laquage, polymérisation et fixation de poudre, avec ligne de laquage robotisée pour des finitions homogènes.</p></article>
          <article><div class="feature-icon">02</div><h3>Finitions</h3><p>Palette annoncée de plus de 450 teintes et effets, incluant bois, givré, anodisé et satiné.</p></article>
          <article><div class="feature-icon">03</div><h3>Logistique</h3><p>Stock stratégique de profilés et accessoires, expéditions organisées et livraisons internationales par conteneurs.</p></article>
          <article><div class="feature-icon">04</div><h3>Durabilité</h3><p>Optimisation des performances énergétiques, technologies à impact environnemental réduit et investissement continu en R&D.</p></article>
          <article><div class="feature-icon">05</div><h3>Hygiène</h3><p>Le site officiel mentionne des traitements antibactériens pour poignées et surfaces destinées aux environnements exigeants.</p></article>
          <article><div class="feature-icon">06</div><h3>Certifications</h3><p>ALLUCO présente notamment CSTB et Istituto Giordano parmi ses références de certification.</p></article>
        </div>
      </div>
    </section>

    <section class="content-section surface" id="products">
      <div class="content-wrap">
        <p class="section-kicker">PRODUITS</p>
        <div class="section-heading">
          <h2>21 références affichées dans 4 familles</h2>
          <p>Le catalogue public ALLUCO organise ses solutions autour des systèmes porte-fenêtre, de l'indoor, de l'outdoor et des garde-corps / clôtures.</p>
        </div>

        <div class="category-grid">
          <article class="category-card">
            <div class="category-top"><span>08</span><h3>Systèmes Porte - Fenêtre</h3></div>
            <ul>
              <li>ALTO 15400 — Coulissant à Levage</li>
              <li>KLIMA 7400 — Série Battante</li>
              <li>OIKOS 4700 — Battant Minimaliste</li>
              <li>Prima 6300</li>
              <li>SUPRA 6000 — Battant à Ouvrant Caché</li>
              <li>Série Froide Square HS 50</li>
              <li>Square 40 — Série Battante</li>
              <li>Square 67 — Série Coulissante</li>
            </ul>
          </article>
          <article class="category-card">
            <div class="category-top"><span>08</span><h3>Indoor</h3></div>
            <ul>
              <li>Dressing Alluco</li>
              <li>Paroi de Douche — Parolit by Alluco</li>
              <li>Porte Accordéon</li>
              <li>Porte coulissante</li>
              <li>Portes Intérieures en Verre</li>
              <li>Portes Pivots</li>
              <li>Séparation bureau</li>
              <li>VEROLIT — Verrières Intérieures</li>
            </ul>
          </article>
          <article class="category-card">
            <div class="category-top"><span>02</span><h3>Outdoor</h3></div>
            <ul><li>Lames de Volets Roulants</li><li>Pergola Azore</li></ul>
          </article>
          <article class="category-card">
            <div class="category-top"><span>03</span><h3>Garde-corps & Clôture</h3></div>
            <p class="category-note">Le catalogue public comptabilise 3 références. Parmi les références identifiées : </p><ul><li>Garde Corps — BlendLine</li><li>Portails & Clôtures</li></ul>
          </article>
        </div>

        <div class="tech-compare">
          <article class="tech-card">
            <p class="tech-label">ALLUCO PREMIUM</p><h3>KLIMA 7400</h3>
            <div class="tech-specs">
              <span><b>Uw</b> 1.13 W/m²K</span><span><b>Dormant</b> 74 mm</span><span><b>Ouvrant</b> 83 mm</span><span><b>Vitrage</b> jusqu'à 40 mm</span><span><b>Air</b> Classe 4</span><span><b>Eau</b> 7A</span><span><b>Vent</b> C4</span><span><b>Acoustique</b> jusqu'à 43 dB</span><span><b>Effraction</b> RC3</span><span><b>Feu</b> EW30 / EI30</span>
            </div>
          </article>
          <article class="tech-card">
            <p class="tech-label">ALLUCO PREMIUM</p><h3>SUPRA 6000</h3>
            <div class="tech-specs">
              <span><b>Uw</b> 1.32 W/m²K</span><span><b>Dormant</b> 60 mm</span><span><b>Ouvrant</b> 69 mm</span><span><b>Vitrage</b> jusqu'à 35 mm</span><span><b>Air</b> Classe 4</span><span><b>Eau</b> 9A</span><span><b>Vent</b> C5</span><span><b>Acoustique</b> jusqu'à 26 dB</span><span><b>Effraction</b> RC2</span><span><b>Feu</b> EW30 / EI30</span>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="content-section surface-alt" id="references">
      <div class="content-wrap">
        <p class="section-kicker">REFERENCES</p>
        <div class="section-heading"><h2>Projets présentés par ALLUCO</h2><p>Le portfolio public met en avant différents projets résidentiels et architecturaux.</p></div>
        <div class="reference-grid"><article>Luxury Palace</article><article>Résidence ALMA</article><article>Résidence Diar el Bhar 2</article><article>Résidence Ennadhour</article></div>
      </div>
    </section>

    <section class="content-section surface" id="locations">
      <div class="content-wrap">
        <p class="section-kicker">NORTH AFRICA & INTERNATIONAL</p>
        <div class="section-heading"><h2>Showrooms et implantations</h2><p>Le réseau public ALLUCO couvre plusieurs marchés en Afrique du Nord, en Afrique et en Europe.</p></div>
        <div class="location-layout">
          <div>
            <h3 class="location-title">Showrooms</h3>
            <div class="location-grid">
              <article><b>Tunisie — Moknine</b><span>Zone industrielle, 5050 Moknine</span><a href="tel:+21670284140">+216 70 284 140</a></article>
              <article><b>Tunisie — Soukra</b><span>64 BIS Av. Fattouma Bourguiba, Tunis</span><a href="tel:+21670284142">+216 70 284 142</a></article>
              <article><b>Égypte — Giza</b><span>6th of October City, A1, Gouvernorat de Gizeh</span><a href="tel:+201112444096">+20 111 244 4096</a></article>
              <article><b>Libye — Janzour</b><span>Al-Sarraj, Route des Bestiaux, près de la mosquée Ibrahim Al-Khalil</span><a href="tel:+218918563438">+218 91 856 3438</a></article>
              <article><b>Algérie — Oran</b><span>700, Boulevard Wahrani Boumediene</span><a href="tel:+213550513412">+213 550 513 412</a></article>
              <article><b>Guinée — Conakry</b><span>H87Q+2GQ, Minière, Conakry</span><a href="tel:+224620711010">+224 620 71 10 10</a></article>
              <article><b>Malte — Attard</b><span>1, Tariq Hal Warda, Attard ATD 1400</span><span>Showroom</span></article>
            </div>
          </div>
          <div>
            <h3 class="location-title">R&D, distribution et fabrication</h3>
            <div class="location-grid compact-locations">
              <article><b>Belgique — Mouscron</b><span>1, Rue de l'Échauffourée, Risquons-Tout Business Center, B-7700 Mouscron</span><a href="tel:+3256480601">+32 (0)56 480 601</a><a href="tel:+3256558008">+32 (0)56 558 008</a></article>
              <article><b>Tunisie — Moknine</b><span>Zone industrielle, 5050 Moknine</span><a href="tel:+21670284140">+216 70 284 140</a><a href="tel:+21670284177">+216 70 284 177</a></article>
              <article><b>Égypte — Giza</b><span>Groupe e², 3ème Industrielle, Sami Saad, Atelier A1</span><a href="tel:+201112444096">+20 111 244 4096</a></article>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="content-section surface-alt" id="showrooms">
      <div class="content-wrap">
        <p class="section-kicker">SHOWROOMS</p>
        <div class="section-heading compact"><h2>Conseil et accompagnement</h2></div>
        <div class="three-col showroom-cards">
          <article class="info-card"><span>90 m²</span><h3>Soukra</h3><p>Espace d'exposition annoncé de 90 m², destiné aux professionnels et particuliers, avec conseil technique et commercial, devis, suivi de commande et assistance logistique.</p></article>
          <article class="info-card"><span>740 m²</span><h3>Moknine</h3><p>Showroom annoncé de 740 m² avec gammes produits, conseils, devis, suivi des commandes, assistance logistique et espace de réunion.</p></article>
          <article class="info-card"><span>190 m²</span><h3>Égypte</h3><p>Espace annoncé de 190 m² pour professionnels et particuliers, avec accompagnement local de la conception à la réalisation.</p></article>
        </div>
      </div>
    </section>

    <section class="content-section surface" id="academy">
      <div class="content-wrap academy-layout">
        <div><p class="section-kicker">ALLUCO ACADEMIE</p><h2>Formation & entrepreneuriat</h2><p>ALLUCO Académie se présente comme un parcours de formation pratique en menuiserie aluminium. Le programme vise l'acquisition d'un savoir-faire professionnel et l'accompagnement des meilleurs talents vers l'entrepreneuriat et l'ouverture de showrooms.</p></div>
        <div class="academy-tags"><span>Formation pratique</span><span>Menuiserie aluminium</span><span>Accompagnement</span><span>Entrepreneuriat</span></div>
      </div>
    </section>

    <section class="content-section contact-section" id="contact">
      <div class="content-wrap">
        <p class="section-kicker">CONTACT</p>
        <div class="contact-hero"><h2>Parlons de votre projet aluminium.</h2><p>Coordonnées publiques ALLUCO.</p></div>
        <div class="contact-official-grid">
          <a href="mailto:info@alluco.com"><span>Email</span><strong>info@alluco.com</strong></a>
          <a href="tel:+21670284142"><span>Soukra</span><strong>+216 70 284 142</strong></a>
          <a href="tel:+21670284140"><span>Moknine</span><strong>+216 70 284 140</strong></a>
          <div><span>Adresse Soukra</span><strong>64 BIS Av. Fattouma Bourguiba, Tunis</strong></div>
        </div>
        <div class="contact-types"><span>Architecte</span><span>Particulier</span><span>Fabricant</span></div>
        <div class="footer-line"><b>ALLUCO</b><span>L'aluminium au service de l'innovation et du design durable.</span><a href="https://alluco.com/" target="_blank" rel="noreferrer">alluco.com ↗</a></div>
      </div>
    </section>
  </main>

  <div class="fallback" id="fallback" hidden><strong>3D indisponible</strong><span>Le contenu ALLUCO reste accessible.</span></div>
  
<script>
(() => {
  'use strict';

  const $ = (s) => document.querySelector(s);
  const $$ = (s) => [...document.querySelectorAll(s)];
  const html = document.documentElement;
  const loader = $('#loader');
  const loaderStatus = $('#loaderStatus');
  const loaderBar = $('#loaderBar');
  const fallback = $('#fallback');
  const canvas = $('#webgl');
  const flowProgress = $('#flowProgress');
  const flowRail = $('#flowRail');
  const institutionalStart = $('#company');
  const flowSteps = $$('.flow-step');
  const sections = $$('[data-scene]');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobile = matchMedia('(max-width: 900px)').matches;

  const progress = (n, text) => {
    loaderBar.style.width = `${n}%`;
    if (text) loaderStatus.textContent = text;
  };

  progress(18, 'CONNEXION DU RESEAU ALLUCO...');

  $('#menu').addEventListener('click', () => $('#nav').classList.toggle('is-open'));
  $$('#nav a').forEach(a => a.addEventListener('click', () => $('#nav').classList.remove('is-open')));

  const storedTheme = localStorage.getItem('alluco-theme');
  if (storedTheme === 'dark') html.dataset.theme = 'dark';
  $('#themeToggle').addEventListener('click', () => {
    html.dataset.theme = html.dataset.theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('alluco-theme', html.dataset.theme);
    if (window.__allucoTheme3D) window.__allucoTheme3D(html.dataset.theme);
  });

  function webglOK() {
    try {
      const c = document.createElement('canvas');
      return !!(window.WebGLRenderingContext && (c.getContext('webgl2') || c.getContext('webgl')));
    } catch (_) { return false; }
  }

  if (!window.THREE || !webglOK()) {
    fallback.hidden = false;
    canvas.style.display = 'none';
    progress(100, 'PRET');
    setTimeout(() => loader.classList.add('is-hidden'), 350);
    return;
  }

  progress(35, 'CHARGEMENT AIR, MER & PORT...');

  const THREE = window.THREE;
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(40, innerWidth / innerHeight, .1, 650);
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: !mobile, powerPreference: 'high-performance' });
  renderer.setSize(innerWidth, innerHeight);
  renderer.setPixelRatio(Math.min(devicePixelRatio, mobile ? 1.25 : 1.7));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.15;
  renderer.shadowMap.enabled = !mobile;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const world = new THREE.Group();
  scene.add(world);

  const COLORS = {
    lightBg: 0xeef3f7,
    darkBg: 0x070b10,
    aluminum: 0xb9c2c9,
    aluminumLight: 0xe6ebef,
    steel: 0x65717c,
    charcoal: 0x26313b,
    blue: 0x1167d8,
    blueLight: 0x50a7ff,
    orange: 0xe79135,
    glass: 0xa9d6f5,
    tire: 0x151a1f,
    floorLight: 0xdfe6eb,
    floorDark: 0x111820,
    sea: 0x71a7c9,
  };

  const mat = {
    aluminum: new THREE.MeshStandardMaterial({ color: COLORS.aluminum, metalness: .9, roughness: .28 }),
    aluminumLight: new THREE.MeshStandardMaterial({ color: COLORS.aluminumLight, metalness: .7, roughness: .32 }),
    steel: new THREE.MeshStandardMaterial({ color: COLORS.steel, metalness: .75, roughness: .38 }),
    charcoal: new THREE.MeshStandardMaterial({ color: COLORS.charcoal, metalness: .55, roughness: .48 }),
    blue: new THREE.MeshStandardMaterial({ color: COLORS.blue, metalness: .5, roughness: .27, emissive: 0x082c5b, emissiveIntensity: .18 }),
    blueLight: new THREE.MeshStandardMaterial({ color: COLORS.blueLight, metalness: .4, roughness: .25 }),
    orange: new THREE.MeshStandardMaterial({ color: COLORS.orange, metalness: .35, roughness: .4 }),
    glass: new THREE.MeshPhysicalMaterial({ color: COLORS.glass, metalness: 0, roughness: .08, transmission: .45, transparent: true, opacity: .55 }),
    tire: new THREE.MeshStandardMaterial({ color: COLORS.tire, roughness: .78 }),
    wood: new THREE.MeshStandardMaterial({ color: 0xa57a52, roughness: .7 }),
  };

  const ambient = new THREE.HemisphereLight(0xffffff, 0x9ba8b2, 2.8);
  scene.add(ambient);
  const sun = new THREE.DirectionalLight(0xffffff, 4.5);
  sun.position.set(30, 35, 18);
  sun.castShadow = !mobile;
  sun.shadow.mapSize.set(1024, 1024);
  scene.add(sun);
  const fill = new THREE.DirectionalLight(0xaacfff, 2.0);
  fill.position.set(-20, 12, -20);
  scene.add(fill);

  const floorMat = new THREE.MeshStandardMaterial({ color: COLORS.floorLight, roughness: .88, metalness: .08 });
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(240, 90), floorMat);
  floor.rotation.x = -Math.PI / 2;
  floor.position.set(80, -2.1, 0);
  floor.receiveShadow = !mobile;
  world.add(floor);

  const grid = new THREE.GridHelper(240, 90, 0xb2c0ca, 0xcbd5dc);
  grid.position.set(80, -2.04, 0);
  grid.material.transparent = true;
  grid.material.opacity = .4;
  world.add(grid);

  function box(group, size, pos, material = mat.aluminum, rot = [0,0,0]) {
    const m = new THREE.Mesh(new THREE.BoxGeometry(...size), material);
    m.position.set(...pos); m.rotation.set(...rot); m.castShadow = !mobile; m.receiveShadow = !mobile; group.add(m); return m;
  }
  function cyl(group, r, depth, pos, material = mat.aluminum, rot = [0,0,0], segments = 24) {
    const m = new THREE.Mesh(new THREE.CylinderGeometry(r, r, depth, segments), material);
    m.position.set(...pos); m.rotation.set(...rot); m.castShadow = !mobile; group.add(m); return m;
  }
  function wheel(group, pos, r=.46) { return cyl(group, r, .28, pos, mat.tire, [0,0,Math.PI/2], 20); }
  function container(group, pos, colorMat = mat.blue, scale=1) {
    const g = new THREE.Group(); g.position.set(...pos); g.scale.setScalar(scale); group.add(g);
    box(g,[3.3,1.55,1.55],[0,0,0],colorMat);
    for(let i=-1.25;i<=1.25;i+=.5) box(g,[.045,1.35,1.58],[i,0,.01],mat.aluminum);
    box(g,[3.34,.06,1.60],[0,.72,0],mat.aluminum);
    return g;
  }

  // Continuous route line linking all logistics scenes.
  const routePoints = [
    new THREE.Vector3(-5,-1.55,0), new THREE.Vector3(8,-1.55,0), new THREE.Vector3(26,-1.55,0),
    new THREE.Vector3(43,-1.55,0), new THREE.Vector3(60,-1.55,0), new THREE.Vector3(79,-1.55,0),
    new THREE.Vector3(99,-1.55,0), new THREE.Vector3(121,-1.55,0), new THREE.Vector3(145,-1.55,0)
  ];
  const routeCurve = new THREE.CatmullRomCurve3(routePoints);
  const routeTube = new THREE.Mesh(
    new THREE.TubeGeometry(routeCurve, 220, .055, 8, false),
    new THREE.MeshBasicMaterial({ color: COLORS.blue, transparent: true, opacity: .62 })
  );
  world.add(routeTube);
  const cargoTokens = Array.from({length:6}, (_,i) => {
    const t = new THREE.Mesh(new THREE.SphereGeometry(.13,12,12), new THREE.MeshBasicMaterial({color: i%2 ? COLORS.blueLight : COLORS.blue}));
    world.add(t); return t;
  });

  // AIRPLANE
  const plane = new THREE.Group(); plane.position.set(3,7.3,0); world.add(plane);
  cyl(plane,.72,7.8,[0,0,0],mat.aluminumLight,[0,0,Math.PI/2],28);
  const nose = new THREE.Mesh(new THREE.ConeGeometry(.73,1.65,28),mat.aluminumLight); nose.rotation.z = -Math.PI/2; nose.position.x = 4.72; plane.add(nose);
  const tailCone = new THREE.Mesh(new THREE.ConeGeometry(.64,1.35,24),mat.aluminum); tailCone.rotation.z = Math.PI/2; tailCone.position.x = -4.55; plane.add(tailCone);
  box(plane,[3.8,.16,10.8],[.2,0,0],mat.aluminumLight,[0,0,.02]);
  box(plane,[1.55,2.15,.16],[-3.25,1.0,0],mat.blue,[0,0,-.18]);
  box(plane,[1.65,.12,4.2],[-3.35,.62,0],mat.aluminum);
  [-2.25,2.25].forEach(z => { cyl(plane,.43,1.25,[.6,-.65,z],mat.steel,[Math.PI/2,0,0],20); cyl(plane,.30,1.32,[.6,-.65,z],mat.charcoal,[Math.PI/2,0,0],20); });
  box(plane,[1.6,.18,.72],[2.4,.05,0],mat.blue);

  // SHIP WITH CONTAINERS
  const seaGroup = new THREE.Group(); seaGroup.position.set(35,-.2,0); world.add(seaGroup);
  const sea = new THREE.Mesh(new THREE.PlaneGeometry(30,18), new THREE.MeshStandardMaterial({color:COLORS.sea,roughness:.28,metalness:.15,transparent:true,opacity:.56}));
  sea.rotation.x=-Math.PI/2; sea.position.y=-1.35; seaGroup.add(sea);
  const ship = new THREE.Group(); seaGroup.add(ship);
  box(ship,[15,1.5,4.3],[0,-.45,0],mat.charcoal);
  const bow = new THREE.Mesh(new THREE.ConeGeometry(2.15,4.8,4),mat.charcoal); bow.rotation.z=Math.PI/2; bow.rotation.y=Math.PI/4; bow.position.set(8.35,-.45,0); ship.add(bow);
  box(ship,[3.0,3.5,3.2],[-5.3,1.55,0],mat.aluminumLight); box(ship,[2.3,.9,2.7],[-5.3,3.7,0],mat.glass);
  const shipContainers=[]; let cc=0;
  [-2.6,-.1,2.4].forEach(x => [-1.15,1.15].forEach(z => {
    shipContainers.push(container(ship,[x,.8,z], cc++%3===0?mat.blue:mat.aluminum, .68));
    shipContainers.push(container(ship,[x,1.9,z], cc++%4===0?mat.blueLight:mat.steel, .68));
  }));

  // PORT + CRANE
  const port = new THREE.Group(); port.position.set(65,0,0); world.add(port);
  box(port,[24,.28,13],[0,-1.9,0],mat.steel);
  const crane = new THREE.Group(); port.add(crane);
  [-4.3,4.3].forEach(x => box(crane,[.42,9,.42],[x,2.6,0],mat.blue));
  box(crane,[9.2,.48,.48],[0,7.0,0],mat.blue); box(crane,[12,.28,.28],[1.3,6.4,0],mat.steel);
  const trolley = box(crane,[1.05,.55,.9],[1.2,6.05,0],mat.charcoal);
  const cable = box(crane,[.06,4.0,.06],[1.2,3.85,0],mat.steel);
  const craneCargo = container(crane,[1.2,1.65,0],mat.blue,.82);
  // truck waiting at port
  const truck = new THREE.Group(); truck.position.set(-7,-.72,3.3); port.add(truck);
  box(truck,[4.8,.45,2.2],[0,0,0],mat.steel); box(truck,[2.2,2.25,2.1],[-2.6,.8,0],mat.aluminumLight); box(truck,[1.7,.75,1.75],[-2.55,1.2,0],mat.glass);
  wheel(truck,[-2.7,-.42,1.15]); wheel(truck,[-2.7,-.42,-1.15]); wheel(truck,[1.4,-.42,1.15]); wheel(truck,[1.4,-.42,-1.15]);
  const truckContainer = container(truck,[.85,1.05,0],mat.blue,.78);

  // WAREHOUSE + FORKLIFT
  const wh = new THREE.Group(); wh.position.set(94,0,0); world.add(wh);
  box(wh,[23,.22,13],[0,-1.95,0],mat.aluminum);
  for (const side of [-1,1]) for (let i=0;i<5;i++) {
    const x=-8+i*4;
    box(wh,[.18,6,.18],[x,.8,side*4.2],mat.steel);
    for(let h=0;h<4;h++) box(wh,[3.7,.12,1.9],[x+1.7,-1.35+h*1.65,side*4.2],mat.steel);
    for(let h=0;h<3;h++) box(wh,[1.25,.45,1.2],[x+1.7,-1.0+h*1.65,side*4.2],h%2?mat.blue:mat.aluminumLight);
  }
  const forklift = new THREE.Group(); forklift.position.set(-3,-.88,0); wh.add(forklift);
  box(forklift,[2.2,1.25,1.7],[0,0,0],mat.orange); box(forklift,[1.1,1.1,1.55],[-.55,.85,0],mat.glass);
  box(forklift,[.18,3.4,.18],[1.0,.9,.62],mat.steel); box(forklift,[.18,3.4,.18],[1.0,.9,-.62],mat.steel);
  box(forklift,[2.25,.10,.10],[2.05,-.42,.55],mat.steel); box(forklift,[2.25,.10,.10],[2.05,-.42,-.55],mat.steel);
  wheel(forklift,[-.65,-.75,.92],.48); wheel(forklift,[-.65,-.75,-.92],.48); wheel(forklift,[.75,-.75,.92],.38); wheel(forklift,[.75,-.75,-.92],.38);
  const pallet = new THREE.Group(); pallet.position.set(3.0,-.22,0); forklift.add(pallet);
  box(pallet,[2.9,.16,1.55],[0,0,0],mat.wood); for(let i=0;i<7;i++) box(pallet,[2.6,.10,.12],[0,.18+i*.16,-.52+(i%3)*.52],mat.aluminumLight);

  // ALUMINIUM PROFILE DISPLAY
  const alum = new THREE.Group(); alum.position.set(124,0,0); world.add(alum);
  for(let i=0;i<10;i++) {
    const y=-1.25+(i%5)*.54; const z=-1.5+Math.floor(i/5)*3.0;
    box(alum,[12,.26,.26],[0,y,z],mat.aluminumLight,[0,.05*(i%2),0]);
  }
  const profile = new THREE.Group(); profile.position.set(2.5,2.4,0); alum.add(profile);
  const outer = box(profile,[4.2,4.2,5.5],[0,0,0],mat.aluminumLight);
  const cavityMat = new THREE.MeshStandardMaterial({color:0x6c7780,metalness:.25,roughness:.7});
  box(profile,[3.1,3.1,5.7],[0,0,0],cavityMat); box(profile,[.34,3.8,5.9],[0,0,0],mat.aluminumLight); box(profile,[3.8,.34,5.9],[0,0,0],mat.aluminumLight);

  // FINAL CONNECTED NETWORK
  const network = new THREE.Group(); network.position.set(151,0,0); world.add(network);
  const ringMat = new THREE.MeshBasicMaterial({color:COLORS.blue,transparent:true,opacity:.35});
  for(let i=0;i<6;i++) { const r=new THREE.Mesh(new THREE.TorusGeometry(2.8+i*.65,.035,8,80),ringMat.clone()); r.rotation.set(Math.PI/2+i*.12,i*.18,i*.08); network.add(r); }
  const nodes=[]; for(let i=0;i<18;i++) { const a=i/18*Math.PI*2; const n=new THREE.Mesh(new THREE.SphereGeometry(.10,12,12),new THREE.MeshBasicMaterial({color:i%3?COLORS.blueLight:COLORS.blue})); n.position.set(Math.cos(a)*(4.2+i%3*.5),Math.sin(a*1.7)*2.1,Math.sin(a)*(4.2+i%3*.5)); network.add(n); nodes.push(n); }

  const cameraStops = [
    {pos:[16,8.5,23], target:[7,1,0]},
    {pos:[13,8.5,18], target:[3,5.3,0]},
    {pos:[48,7.0,18], target:[35,0,0]},
    {pos:[78,7.2,17], target:[65,1.2,0]},
    {pos:[108,6.5,18], target:[94,0,0]},
    {pos:[139,6.8,18], target:[124,.8,0]},
    {pos:[164,7.5,17], target:[151,0,0]},
    {pos:[171,8,21], target:[156,0,0]},
  ];

  const wantedPos = new THREE.Vector3(...cameraStops[0].pos);
  const wantedTarget = new THREE.Vector3(...cameraStops[0].target);
  camera.position.copy(wantedPos); camera.lookAt(wantedTarget);

  function theme3D(theme) {
    const dark = theme === 'dark';
    scene.background = new THREE.Color(dark ? COLORS.darkBg : COLORS.lightBg);
    scene.fog = new THREE.FogExp2(dark ? COLORS.darkBg : COLORS.lightBg, mobile ? .020 : .013);
    floorMat.color.setHex(dark ? COLORS.floorDark : COLORS.floorLight);
    grid.material.color.setHex(dark ? 0x263643 : 0xb8c4cc);
    ambient.groundColor.setHex(dark ? 0x111820 : 0x9ba8b2);
    renderer.toneMappingExposure = dark ? 1.28 : 1.05;
  }
  window.__allucoTheme3D = theme3D;
  theme3D(html.dataset.theme || 'light');

  function scrollInfo() {
    const y = scrollY + innerHeight * .5;
    let idx = 0, local = 0;
    for(let i=0;i<sections.length;i++) {
      const a=sections[i].offsetTop;
      const b=i<sections.length-1?sections[i+1].offsetTop:document.documentElement.scrollHeight;
      if(y>=a && y<b) { idx=i; local=THREE.MathUtils.clamp((y-a)/Math.max(1,b-a),0,1); break; }
    }
    const max=Math.max(1,document.documentElement.scrollHeight-innerHeight);
    return {idx,local,total:THREE.MathUtils.clamp(scrollY/max,0,1)};
  }

  let currentScene=0;
  function updateScrollUI(idx,total) {
    currentScene=idx;
    const storyEnd = institutionalStart ? Math.max(1, institutionalStart.offsetTop - innerHeight) : Math.max(1, document.documentElement.scrollHeight - innerHeight);
    const storyProgress = THREE.MathUtils.clamp(scrollY / storyEnd, 0, 1);
    flowProgress.style.width=`${Math.min(100,storyProgress*100)}%`;
    const flowIndex=Math.min(4,Math.max(0,idx-1));
    flowSteps.forEach((s,i)=>s.classList.toggle('is-active',i<=flowIndex));
    if (flowRail && institutionalStart) flowRail.classList.toggle('is-hidden', scrollY > institutionalStart.offsetTop - innerHeight * .72);
  }

  const tempA=new THREE.Vector3(), tempB=new THREE.Vector3();
  function updateCamera() {
    const s=scrollInfo(); updateScrollUI(s.idx,s.total);
    const a=cameraStops[s.idx], b=cameraStops[Math.min(s.idx+1,cameraStops.length-1)];
    const t=reduced?0:s.local*s.local*(3-2*s.local);
    tempA.set(...a.pos).lerp(tempB.set(...b.pos),t);
    wantedPos.copy(tempA);
    tempA.set(...a.target).lerp(tempB.set(...b.target),t); wantedTarget.copy(tempA);
    camera.position.lerp(wantedPos,reduced?1:.075);
    camera.lookAt(wantedTarget);
  }

  const clock=new THREE.Clock();
  function animate() {
    const t=clock.getElapsedTime();
    updateCamera();
    if(!reduced) {
      // All movements share the same phase to feel like one connected operation.
      const phase=t*.55;
      plane.position.x=3+Math.sin(phase)*1.2; plane.position.y=7.3+Math.sin(phase*1.35)*.25; plane.rotation.z=Math.sin(phase*.7)*.025;
      ship.position.x=Math.sin(phase*.55)*.55; ship.position.y=Math.sin(phase*.9)*.10; ship.rotation.z=Math.sin(phase*.7)*.012;
      const lift=(Math.sin(phase*1.15)+1)*.5; craneCargo.position.y=1.25+lift*2.9; cable.scale.y=.45+(1-lift)*.8; cable.position.y=4.5-lift*1.3;
      trolley.position.x=1.2+Math.sin(phase*.65)*1.8; craneCargo.position.x=trolley.position.x; cable.position.x=trolley.position.x;
      forklift.position.x=-3+Math.sin(phase*.95)*3.4; forklift.rotation.y=Math.sin(phase*.48)*.025;
      profile.rotation.y=t*.18;
      network.rotation.y=t*.08;
      cargoTokens.forEach((token,i)=>{ const p=(t*.035+i/cargoTokens.length)%1; token.position.copy(routeCurve.getPointAt(p)); token.position.y+=.22; });
      // Gentle visual response from the currently visited scene.
      const pulse=1+Math.sin(t*2)*.025;
      if(currentScene===1) plane.scale.setScalar(pulse);
      else plane.scale.setScalar(1);
      if(currentScene===2) ship.scale.setScalar(pulse); else ship.scale.setScalar(1);
      if(currentScene===4) forklift.scale.setScalar(pulse); else forklift.scale.setScalar(1);
    }
    renderer.render(scene,camera);
    requestAnimationFrame(animate);
  }

  addEventListener('resize',()=>{
    camera.aspect=innerWidth/innerHeight; camera.updateProjectionMatrix();
    renderer.setSize(innerWidth,innerHeight); renderer.setPixelRatio(Math.min(devicePixelRatio,mobile?1.25:1.7));
  });

  progress(76, 'CONNEXION PORT, FORKLIFT & DEPOT...');
  requestAnimationFrame(()=>{
    animate();
    progress(100, 'PRET');
    setTimeout(()=>loader.classList.add('is-hidden'),420);
  });
})();

</script>
</body>
</html>
'''

components.html(SITE_HTML, height=1000, scrolling=True)
