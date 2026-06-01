import streamlit as st
import sys
sys.path.append(".")
from utils.db      import load_bikes
from utils.ai      import get_recommendation
from utils.theme   import get_theme
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title            = "Bike Recommender",
    page_icon             = "🏍️",
    layout                = "wide",
    initial_sidebar_state = "expanded"
)

st.markdown(get_theme(), unsafe_allow_html=True)

# Fix button + form styling for this page
st.markdown("""
<style>
    /* ── Main recommend button — solid red ──────────────────────────────────── */
    .stButton>button,
    .stButton>button:focus,
    .stButton>button:active,
    .stButton>button:focus:not(:active) {
        background    : #E74C3C !important;
        color         : #FFFFFF !important;
        border        : none !important;
        border-radius : 10px !important;
        font-size     : 1rem !important;
        font-weight   : 700 !important;
        padding       : 0.8rem !important;
        box-shadow    : none !important;
        outline       : none !important;
        transition    : all 0.3s !important;
    }
    .stButton>button:hover {
        background : #C0392B !important;
        transform  : translateY(-2px) !important;
    }

    /* ── Selectbox — white bg ───────────────────────────────────────────────── */
    [data-testid="stSelectbox"] > div > div {
        background    : #FFFFFF !important;
        border        : 1px solid #E0E0E0 !important;
        border-radius : 8px !important;
        color         : #1A1A2E !important;
    }

    /* ── Slider track — red ─────────────────────────────────────────────────── */
    [data-testid="stSlider"] > div > div > div > div {
        background : #E74C3C !important;
    }

    /* ── Metric cards — white ───────────────────────────────────────────────── */
    [data-testid="stMetric"] {
        background    : #FFFFFF !important;
        border-left   : 3px solid #E74C3C !important;
        border-radius : 8px !important;
        padding       : 0.8rem 1rem !important;
        box-shadow    : 0 1px 4px rgba(0,0,0,0.08) !important;
    }
    [data-testid="stMetricLabel"] p { color: #7F8C8D !important; }
    [data-testid="stMetricValue"]   { color: #1A1A2E !important; }

/* ── Dataframe — force white ────────────────────────────────────────────── */
    [data-testid="stDataFrame"] {
        background    : #FFFFFF !important;
        border        : 1px solid #E0E0E0 !important;
        border-radius : 8px !important;
    }
    [data-testid="stDataFrame"] iframe {
        background    : #FFFFFF !important;
        color-scheme  : light !important;
    }
    .stDataFrame > div {
        background    : #FFFFFF !important;
    }

    /* ── Section labels ─────────────────────────────────────────────────────── */
    .section-label-red {
        color          : #E74C3C;
        font-size      : 0.72rem;
        font-weight    : 700;
        letter-spacing : 0.12em;
        text-transform : uppercase;
        margin-bottom  : 0.6rem;
    }
    .section-label-green {
        color          : #E74C3C;
        font-size      : 0.72rem;
        font-weight    : 700;
        letter-spacing : 0.12em;
        text-transform : uppercase;
        margin-bottom  : 0.6rem;
    }

    /* ── Result box — light red tint ────────────────────────────────────────── */
    .result-box {
        background    : #FFF5F5;
        border        : 1px solid #E74C3C;
        border-radius : 12px;
        padding       : 1.5rem 2rem;
        color         : #1A1A2E;
        line-height   : 1.9;
        font-size     : 0.92rem;
        box-shadow    : 0 2px 8px rgba(231,76,60,0.08);
    }
    .result-box h2 {
        color       : #E74C3C !important;
        font-size   : 1.1rem !important;
        margin-top  : 1.2rem !important;
    }
    .result-box strong { color: #1A1A2E !important; }
    .result-box hr     { border-color: #F0D0CC !important; }

    /* ── Form card — white ──────────────────────────────────────────────────── */
    .form-section {
        background    : #FFFFFF;
        border        : 1px solid #E0E0E0;
        border-radius : 12px;
        padding       : 1.5rem;
        box-shadow    : 0 2px 8px rgba(0,0,0,0.06);
    }

    /* ── Filter chips ───────────────────────────────────────────────────────── */
    .chip {
        background    : #FFF5F5;
        border        : 1px solid #E74C3C;
        border-radius : 20px;
        padding       : 3px 12px;
        font-size     : 0.75rem;
        color         : #E74C3C;
        display       : inline-block;
        margin        : 3px;
    }

    /* ── Alert ──────────────────────────────────────────────────────────────── */
    [data-testid="stAlert"] {
        background : #FFF5F5 !important;
        border-left: 4px solid #E74C3C !important;
        color      : #1A1A2E !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return load_bikes()

bikes_df = load_data()

# Consistent sidebar
render_sidebar(bikes_df)

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#000000,#1A1A1A);
            border:1px solid #1A1A1A; border-radius:12px;
            padding:1.5rem 2rem; margin-bottom:1.5rem;">
    <div style="font-size:1.8rem; font-weight:800; color:#FFFFFF;">
        🎯 AI <span style="color:#E74C3C;">Bike Recommender</span>
    </div>
    <div style="color:#7F8C8D; font-size:0.88rem; margin-top:0.3rem;">
        Tell us your requirements ·
        Google Gemini picks your perfect bike from 66 options ·
        Personalised for Indian buyers
    </div>
</div>
""", unsafe_allow_html=True)

# ── Form + Preview ────────────────────────────────────────────────────────────
col_form, col_preview = st.columns([1.1, 1])

with col_form:
    st.markdown('<div class="section-label-red">⚙️ Your Requirements</div>',
                unsafe_allow_html=True)

    with st.container(border=True):
        budget_range = st.slider(
            "💰 Budget Range (Rs)",
            min_value = 50000,
            max_value = 400000,
            value     = (80000, 150000),
            step      = 5000,
            format    = "Rs %d"
        )

        st.markdown(f"""
        <div style="color:#7F8C8D; font-size:0.78rem;
                    margin-top:-12px; margin-bottom:10px;">
            Selected: Rs {budget_range[0]:,} — Rs {budget_range[1]:,}
        </div>
        """, unsafe_allow_html=True)

        usage = st.selectbox("🛣️ Primary Usage", [
            "Daily City Commute",
            "Long Distance Touring",
            "Weekend Pleasure Rides",
            "First Bike — Learning",
            "Performance / Track Riding",
            "Off-road Adventure"
        ])

        fuel_pref = st.selectbox("⛽ Fuel Preference", [
            "No Preference",
            "Electric Only",
            "Petrol Only"
        ])

        priority = st.selectbox("⭐ Top Priority", [
            "Best Mileage / Range",
            "Lowest Running Cost",
            "Maximum Performance",
            "Comfortable Long Rides",
            "Best Resale Value",
            "Stylish Design",
            "Easy Maintenance"
        ])

        rider_exp = st.selectbox("🏍️ Rider Experience", [
            "Beginner",
            "Intermediate",
            "Experienced"
        ])

with col_preview:
    st.markdown('<div class="section-label-green">📊 Bikes in Your Budget</div>',
                unsafe_allow_html=True)

    # Filter preview
    filtered = bikes_df[
        (bikes_df["price_inr"] >= budget_range[0]) &
        (bikes_df["price_inr"] <= budget_range[1])
    ].copy()

    fuel_map_filter = {
        "Electric Only" : True,
        "Petrol Only"   : False,
        "No Preference" : None
    }
    fuel_val = fuel_map_filter[fuel_pref]
    if fuel_val is not None:
        filtered = filtered[filtered["is_ev"] == fuel_val]

    # Stats
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Options",  len(filtered))
    c2.metric("⚡ EV",          int(filtered["is_ev"].sum()))
    c3.metric("🔴 Petrol",      int((~filtered["is_ev"]).sum()))

    if len(filtered) > 0:
        display = filtered[[
            "name","brand","segment",
            "price_inr","fuel_type","rating"
        ]].sort_values("price_inr").reset_index(drop=True).copy()
        display.columns = ["Bike","Brand","Segment","Price (Rs)","Fuel","⭐"]
        st.dataframe(display, use_container_width=True,
                     height=300, hide_index=True)
    else:
        st.warning("No bikes found. Try adjusting your budget or fuel preference.")

    # Active filter chips
    fuel_chip = {
        "No Preference" : "⚡🔴 All",
        "Electric Only" : "⚡ EV Only",
        "Petrol Only"   : "🔴 Petrol Only"
    }
    st.markdown(f"""
    <div style="margin-top:0.8rem; display:flex; flex-wrap:wrap; gap:4px;">
        <span class="chip">Rs{budget_range[0]//1000}K–Rs{budget_range[1]//1000}K</span>
        <span class="chip">{usage}</span>
        <span class="chip">{fuel_chip[fuel_pref]}</span>
        <span class="chip">{priority}</span>
        <span class="chip">{rider_exp}</span>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── Recommend button ──────────────────────────────────────────────────────────
if st.button("🎯  Get My Perfect Bike Recommendation",
             use_container_width=True):
    if len(filtered) == 0:
        st.error("No bikes match your filters. Please adjust your budget or preferences.")
    else:
        with st.spinner("Google Gemini is analysing 66 bikes for you..."):
            fuel_clean = fuel_pref.replace(" Only", "")
            result = get_recommendation(
                budget_min = budget_range[0],
                budget_max = budget_range[1],
                usage      = usage,
                fuel_pref  = fuel_clean,
                priority   = priority,
                rider_exp  = rider_exp,
                bikes_df   = bikes_df
            )

        st.markdown("""
        <div style="color:#E74C3C; font-size:0.72rem; font-weight:700;
                    letter-spacing:0.12em; text-transform:uppercase;
                    margin:1.2rem 0 0.8rem;">
            🏆 Your Personalised Recommendations
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f'<div class="result-box">{result}</div>',
                    unsafe_allow_html=True)

        st.divider()

        st.markdown(f"""
        <div style="background:#FFFFFF; border-radius:8px;
                    padding:0.8rem 1.2rem; font-size:0.78rem;
                    color:#7F8C8D; text-align:center;">
            Based on {len(filtered)} bikes matching your criteria ·
            Prices are ex-showroom and may vary by city ·
            Always do a test ride before purchasing
        </div>
        """, unsafe_allow_html=True)