import streamlit as st
import sys
import time
sys.path.append(".")
from utils.db      import load_bikes, load_sales
from utils.ai      import get_data_context, ask_gemini
from utils.theme   import get_theme
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title            = "AI Market Analyst",
    page_icon             = "🏍️",
    layout                = "wide",
    initial_sidebar_state = "expanded"
)

st.markdown(get_theme(), unsafe_allow_html=True)

st.markdown("""
<style>
    /* ── Suggested question buttons ─────────────────────────────────────────── */
    div[data-testid="stColumn"] div[data-testid="stButton"] button,
    div[data-testid="stColumn"] div[data-testid="stButton"] button:focus,
    div[data-testid="stColumn"] div[data-testid="stButton"] button:active,
    div[data-testid="stColumn"] div[data-testid="stButton"] button:visited,
    div[data-testid="stColumn"] div[data-testid="stButton"] button:focus:not(:active) {
        background    : #1E1E2E !important;
        color         : #FFFFFF !important;
        border        : 1.5px solid #E74C3C !important;
        border-radius : 8px !important;
        font-size     : 0.85rem !important;
        font-weight   : 500 !important;
        white-space   : normal !important;
        height        : auto !important;
        min-height    : 55px !important;
        line-height   : 1.5 !important;
        box-shadow    : none !important;
        outline       : none !important;
        transition    : all 0.2s !important;
    }
    div[data-testid="stColumn"] div[data-testid="stButton"] button:hover {
        background    : #E74C3C !important;
        color         : #FFFFFF !important;
        border        : 1.5px solid #E74C3C !important;
        box-shadow    : none !important;
    }

    /* ── Clear button ───────────────────────────────────────────────────────── */
    div[data-testid="stHorizontalBlock"] > div:last-child div[data-testid="stButton"] button,
    div[data-testid="stHorizontalBlock"] > div:last-child div[data-testid="stButton"] button:focus,
    div[data-testid="stHorizontalBlock"] > div:last-child div[data-testid="stButton"] button:active {
        background    : transparent !important;
        color         : #E74C3C !important;
        border        : 1px solid #E74C3C !important;
        border-radius : 6px !important;
        min-height    : 36px !important;
        font-size     : 0.82rem !important;
        box-shadow    : none !important;
    }
    div[data-testid="stHorizontalBlock"] > div:last-child div[data-testid="stButton"] button:hover {
        background    : #E74C3C !important;
        color         : #FFFFFF !important;
    }

    /* ── Radio ──────────────────────────────────────────────────────────────── */
    [data-testid="stRadio"] label p {
        color     : #BDC3C7 !important;
        font-size : 0.88rem !important;
    }

    /* ── Chat input — single red border, white bg ───────────────────────────── */
    div[data-testid="stChatInput"],
    div[data-testid="stChatInput"] > div,
    div[data-testid="stChatInput"] > div > div,
    div[data-testid="stChatInput"] textarea,
    div[data-testid="stChatInput"] input,
    div[data-testid="stChatInput"] > div > div > div {
        border        : none !important;
        border-bottom : none !important;
        border-top    : none !important;
        border-left   : none !important;
        border-right  : none !important;
        box-shadow    : none !important;
        outline       : none !important;
    }
    div[data-testid="stChatInput"] > div {
        border        : 1.5px solid #E74C3C !important;
        border-radius : 12px !important;
        background    : #FFFFFF !important;
    }
    div[data-testid="stChatInput"] textarea {
    background-color : #FFFFFF !important;
    color            : #000000 !important;
    caret-color      : #000000 !important;
    }
    /* Placeholder */
    div[data-testid="stChatInput"] textarea::placeholder {
        color: #666666 !important;
        opacity: 1 !important;
    }
    div[data-testid="stChatInput"]:focus-within > div {
        border-color : #E74C3C !important;
        box-shadow   : 0 0 0 2px rgba(231,76,60,0.12) !important;
    }

    /* ── Chat bottom bar — white ─────────────────────────────────────────────── */
    [data-testid="stBottom"] {
        background : #F8F9FA !important;
        border-top : 1px solid #E0E0E0 !important;
    }
    [data-testid="stBottom"] > div {
        background : #F8F9FA !important;
    }

    /* ── Section labels — red ───────────────────────────────────────────────── */
    .section-label {
        color          : #E74C3C;
        font-size      : 0.72rem;
        font-weight    : 700;
        letter-spacing : 0.12em;
        text-transform : uppercase;
        margin-bottom  : 0.6rem;
    }

    /* ── Empty state ────────────────────────────────────────────────────────── */
    .empty-state {
        text-align : center;
        padding    : 4rem 2rem;
    }
    .empty-state .icon  { font-size: 3.5rem; margin-bottom: 1rem; }
    .empty-state .title { font-size: 1.1rem; color: #718096; margin-bottom: 0.5rem; }
    .empty-state .sub   { font-size: 0.85rem; color: #4A5568; line-height: 1.7; }
</style>
""", unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    return load_bikes(), load_sales()

with st.spinner("Loading market data..."):
    bikes_df, sales_df = load_data()
    context = get_data_context(bikes_df, sales_df)

render_sidebar(bikes_df)

# ── Page header — red border ──────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#000000,#1A1A1A);
            border:1px solid #1A1A1A; border-radius:12px;
            padding:1.5rem 2rem; margin-bottom:1.5rem;">
    <div style="font-size:1.8rem; font-weight:800; color:#FFFFFF;">
        🤖 AI <span style="color:#E74C3C;">Market Analyst</span>
    </div>
    <div style="color:#7F8C8D; font-size:0.88rem; margin-top:0.3rem;">
        Ask anything about India's two-wheeler market ·
        Powered by Google Gemini ·
        Data: 66 bikes · 2019–2023 · 3,936 sales records
    </div>
</div>
""", unsafe_allow_html=True)

# ── Topic + Suggested Questions ───────────────────────────────────────────────
questions_map = {
    "All Topics": [
        "Which bike has the best value for money under Rs 1 lakh?",
        "Is the EV market ready to challenge petrol bikes?",
        "Which brand dominates India's bike market and why?",
    ],
    "EV Analysis": [
        "Which EV scooter has the best real-world range under Rs 1.5L?",
        "Compare Ola S1 Pro vs Ather 450X — which is better?",
        "At current growth rate when will EVs outsell petrol bikes?",
    ],
    "Sales & Market": [
        "How did COVID impact two-wheeler sales in 2020?",
        "Which month sees the highest bike sales in India?",
        "How much did the market recover post COVID by 2022?",
    ],
    "Brand Insights": [
        "Why is Hero MotoCorp still the market leader in 2023?",
        "Which legacy brand has the strongest EV lineup?",
        "Is Royal Enfield growing or losing market share?",
    ],
    "Segment Analysis": [
        "Which segment is growing the fastest in 2023?",
        "Why does the commuter segment dominate India's market?",
        "Is the premium bike segment growing in India?",
    ],
    "Specs & Performance": [
        "Which petrol bike gives the most power per rupee?",
        "What is the most fuel efficient bike under Rs 80,000?",
        "Which EV has the best range to price ratio?",
    ],
    "Price & Value": [
        "Is an EV actually cheaper than petrol over 5 years?",
        "What is the sweet spot price for a daily commuter?",
        "Which bikes offer best resale value in India?",
    ],
}

col_left, col_right = st.columns([1, 3])

with col_left:
    st.markdown('<div class="section-label">🔍 Filter by Topic</div>',
                unsafe_allow_html=True)
    topic = st.radio("", list(questions_map.keys()),
                     label_visibility="collapsed")

with col_right:
    st.markdown('<div class="section-label">💡 Suggested Questions</div>',
                unsafe_allow_html=True)
    suggested = questions_map[topic]
    q_cols    = st.columns(3)
    for i, q in enumerate(suggested):
        if q_cols[i].button(q, key=f"sq_{topic}_{i}",
                            use_container_width=True):
            st.session_state["prefill"] = q

st.divider()

# ── Chat area ─────────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

col_title, col_clear = st.columns([6, 1])
with col_title:
    st.markdown('<div class="section-label">💬 Conversation</div>',
                unsafe_allow_html=True)
with col_clear:
    if st.button("🗑️ Clear", key="clear_chat",
                 use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Empty state
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="empty-state">
        <div class="icon">🏍️</div>
        <div class="title">Start a conversation</div>
        <div class="sub">
            Click a suggested question above or type your own below.<br>
            Ask about sales trends, EV vs petrol, brand analysis,
            specs, pricing — anything about India's bike market.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Chat input ────────────────────────────────────────────────────────────────
user_input = st.chat_input("Ask about India's bike market...")

if "prefill" in st.session_state:
    user_input = st.session_state.pop("prefill")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Analysing market data..."):
            response = ask_gemini(user_input, context)
        placeholder = st.empty()
        displayed   = ""
        for char in response:
            displayed += char
            placeholder.markdown(displayed)
            time.sleep(0.005)

    st.session_state.messages.append({
        "role"   : "assistant",
        "content": response
    })
