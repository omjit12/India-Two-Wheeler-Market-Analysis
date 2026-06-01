import streamlit as st
import sys
sys.path.append("streamlit_app")
from utils.theme   import get_theme
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title            = "India Bike Market Analysis",
    page_icon             = "🏍️",
    layout                = "wide",
    initial_sidebar_state = "expanded"
)

st.markdown(get_theme(), unsafe_allow_html=True)
render_sidebar()

# ── Hero section ──────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#000000,#1A1A1A);
            border:1px solid #1A1A1A; border-radius:14px;
            padding:2.5rem 3rem; margin-bottom:2rem;">
    <div style="font-size:2.8rem; font-weight:900; color:#FFFFFF;
                letter-spacing:-1px; line-height:1.1;">
        🏍️ Indian Bike Market
        <span style="color:#2ECC71;">Analysis</span>
    </div>
    <div style="color:#BDC3C7; font-size:1rem; margin-top:0.5rem;">
        Comprehensive Two-Wheeler Market Intelligence · 2019–2023 ·
        Powered by Google Gemini AI
    </div>
</div>
""", unsafe_allow_html=True)

# ── Stats row ─────────────────────────────────────────────────────────────────
stats = [
    ("144M",  "Total Units Sold",  "#2ECC71"),
    ("66",    "Bikes Analysed",    "#3498DB"),
    ("10.6%", "EV Market Share",   "#2ECC71"),
    ("18",    "Brands Covered",    "#E74C3C"),
    ("7,827", "Customer Reviews",  "#3498DB"),
]

cols = st.columns(5)
for col, (val, label, color) in zip(cols, stats):
    col.markdown(f"""
    <div style="background:#FFFFFF; border-left:4px solid {color};
                border-radius:10px; padding:1rem 1.2rem;
                text-align:center;
                box-shadow:0 2px 8px rgba(0,0,0,0.08);">
        <div style="font-size:1.8rem; font-weight:800;
                    color:{color}; line-height:1.1;">{val}</div>
        <div style="font-size:0.78rem; color:#7F8C8D;
                    margin-top:4px;">{label}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Feature cards ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="color:#E74C3C; font-size:0.75rem; font-weight:700;
            letter-spacing:0.12em; text-transform:uppercase;
            margin-bottom:1rem;">
    Choose a Feature
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background:#FFFFFF; border:1px solid #2ECC71;
                border-radius:14px; padding:2rem; height:220px;
                box-shadow:0 2px 8px rgba(0,0,0,0.06);">
        <div style="font-size:2.5rem; margin-bottom:0.8rem;">🤖</div>
        <div style="font-size:1.3rem; font-weight:800;
                    color:#2ECC71; margin-bottom:0.5rem;">
            AI Market Analyst
        </div>
        <div style="color:#5D6D7E; font-size:0.88rem; line-height:1.6;">
            Ask anything about India's two-wheeler market.
            Get instant AI-powered insights backed by real sales data,
            specs and market trends from 2019 to 2023.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.page_link("pages/01_chatbot.py", label="🤖  Open AI Market Analyst →")

with col2:
    st.markdown("""
    <div style="background:#FFFFFF; border:1px solid #E74C3C;
                border-radius:14px; padding:2rem; height:220px;
                box-shadow:0 2px 8px rgba(0,0,0,0.06);">
        <div style="font-size:2.5rem; margin-bottom:0.8rem;">🎯</div>
        <div style="font-size:1.3rem; font-weight:800;
                    color:#E74C3C; margin-bottom:0.5rem;">
            Bike Recommender
        </div>
        <div style="color:#5D6D7E; font-size:0.88rem; line-height:1.6;">
            Tell us your budget, usage and priorities.
            Google Gemini analyses 66 bikes and picks your
            perfect top 3 with detailed reasoning.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.page_link("pages/02_recommend.py", label="🎯  Open Bike Recommender →")

st.divider()

# ── Key insights ──────────────────────────────────────────────────────────────
st.markdown("""
<div style="color:#E74C3C; font-size:0.75rem; font-weight:700;
            letter-spacing:0.12em; text-transform:uppercase;
            margin-bottom:1rem;">
    Key Market Insights
</div>
""", unsafe_allow_html=True)

insights = [
    ("🏆", "Hero MotoCorp",    "Controls 32% of India's market",         "#2ECC71"),
    ("⚡", "EV Growth",        "0% → 10.6% in just 4 years",             "#3498DB"),
    ("💰", "EV Running Cost",  "Rs 0.2/km vs Rs 1.6–3.5/km petrol",      "#E74C3C"),
    ("🛵", "Top Seller",       "Hero Splendor Plus — 19M units",          "#2ECC71"),
    ("📍", "EV Leader State",  "Maharashtra with 37K registrations",      "#3498DB"),
    ("🔋", "Best EV Range",    "Ultraviolette F77 — 307km",               "#E74C3C"),
]

cols = st.columns(6)
for col, (icon, title, desc, color) in zip(cols, insights):
    col.markdown(f"""
    <div style="background:#FFFFFF; border-radius:10px;
                padding:1rem; text-align:center;
                border-top:3px solid {color};
                box-shadow:0 2px 8px rgba(0,0,0,0.06);
                height:120px;">
        <div style="font-size:1.5rem;">{icon}</div>
        <div style="color:{color}; font-size:0.78rem;
                    font-weight:700; margin:4px 0;">{title}</div>
        <div style="color:#7F8C8D; font-size:0.72rem;
                    line-height:1.4;">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
