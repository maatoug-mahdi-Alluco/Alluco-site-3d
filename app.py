from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ALLUCO | Aluminium Import Export",
    layout="wide",
    initial_sidebar_state="collapsed",
)

base = Path(__file__).parent

html = (base / "index.html").read_text(encoding="utf-8")
css = (base / "styles.css").read_text(encoding="utf-8")
js = (base / "script.js").read_text(encoding="utf-8")

html = html.replace(
    '<link rel="stylesheet" href="styles.css">',
    f"<style>{css}</style>"
)

html = html.replace(
    '<script type="module" src="script.js"></script>',
    f'<script type="module">{js}</script>'
)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    iframe {
        width: 100% !important;
        border: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(
    html,
    height=4000,
    scrolling=True,
)
