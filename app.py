import streamlit as st
from pathlib import Path

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
        .block-container, .stMainBlockContainer {
            padding: 0 !important;
            max-width: 100% !important;
        }
        iframe { display: block; }
        header[data-testid="stHeader"], .stAppHeader {
            background: transparent;
            height: 0rem;
            min-height: 0rem;
        }
        div[data-testid="stToolbar"] { display: none; }
        div[data-testid="stDecoration"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "before_gates_open01.html"
st.iframe(html_path, height=2200)
