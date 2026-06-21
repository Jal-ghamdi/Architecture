import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Before the Gates Open | Saudi 2034",
    page_icon="🇸🇦",
    layout="wide",
)

# Remove Streamlit's default padding/margins so the page reads as a real
# full-bleed site rather than a widget embedded in a Streamlit app.
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        iframe { display: block; }
        header[data-testid="stHeader"] { background: transparent; }
    </style>
    """,
    unsafe_allow_html=True,
)

# The page is ~23MB (embedded base64 images), which is too large to pass
# inline through components.html()'s srcdoc — browsers/Streamlit's data
# channel silently fail on payloads that big. Instead, it's served as a
# static file (see .streamlit/config.toml) and loaded via a normal URL,
# exactly like opening the file directly in a browser.
components.iframe("app/static/before_gates_open01.html", height=2200, scrolling=True)
