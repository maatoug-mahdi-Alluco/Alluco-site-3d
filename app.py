from pathlib import Path
import re

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="ALLUCO | Aluminium • Import • Export",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent

html_path = BASE_DIR / "index.html"
css_path = BASE_DIR / "styles.css"
js_path = BASE_DIR / "script.js"


if not html_path.exists():
    st.error("index.html introuvable.")
    st.stop()

if not css_path.exists():
    st.error("styles.css introuvable.")
    st.stop()

if not js_path.exists():
    st.error("script.js introuvable.")
    st.stop()


html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
js = js_path.read_text(encoding="utf-8")


# Supprimer l'ancien lien CSS externe
html = re.sub(
    r'<link[^>]*href=["\']styles\.css["\'][^>]*>',
    "",
    html,
    flags=re.IGNORECASE,
)

# Supprimer l'ancien script externe
html = re.sub(
    r'<script[^>]*src=["\']script\.js["\'][^>]*>\s*</script>',
    "",
    html,
    flags=re.IGNORECASE,
)

# Injecter directement le CSS
style_block = f"""
<style>
{css}
</style>
"""

if "</head>" in html:
    html = html.replace("</head>", style_block + "\n</head>")
else:
    html = style_block + html


# Injecter directement JavaScript
script_block = f"""
<script type="module">
{js}
</script>
"""

if "</body>" in html:
    html = html.replace("</body>", script_block + "\n</body>")
else:
    html += script_block


# Supprimer l'interface Streamlit autour du site
st.markdown(
    """
    <style>
        html, body {
            margin: 0 !important;
            padding: 0 !important;
        }

        [data-testid="stHeader"] {
            display: none !important;
        }

        [data-testid="stToolbar"] {
            display: none !important;
        }

        [data-testid="stDecoration"] {
            display: none !important;
        }

        [data-testid="stSidebar"] {
            display: none !important;
        }

        footer {
            display: none !important;
        }

        #MainMenu {
            visibility: hidden !important;
        }

        .stApp {
            margin: 0 !important;
            padding: 0 !important;
            background: #05080d;
        }

        .block-container {
            max-width: 100% !important;
            width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        [data-testid="stVerticalBlock"] {
            gap: 0 !important;
        }

        iframe {
            width: 100% !important;
            border: none !important;
            display: block !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


components.html(
    html,
    height=8000,
    scrolling=True,
)
