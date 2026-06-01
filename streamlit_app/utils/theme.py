def get_theme():
    return """
<style>
    /* ── Hide Streamlit defaults ───────────────────────────────────────────── */
    #MainMenu  { visibility: hidden; }
    footer     { visibility: hidden; }

    /* Hide default Streamlit page switcher */
    [data-testid="stSidebarNav"]          { display: none !important; }
    [data-testid="stSidebarNavItems"]     { display: none !important; }
    [data-testid="stSidebarNavSeparator"] { display: none !important; }

    /* ── Main background — white ───────────────────────────────────────────── */
    .stApp                 { background-color: #F8F9FA; }
    .main .block-container { padding-top: 1.5rem; }

    /* ── Sidebar — black ───────────────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background-color : #000000;
        border-right     : 2px solid #2ECC71;
        min-width        : 260px !important;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div {
        color: #FFFFFF;
    }

    [data-testid="stSidebar"] a {
        color          : #BDC3C7 !important;
        font-size      : 0.9rem !important;
        padding        : 0.4rem 0.8rem !important;
        border-radius  : 6px !important;
        display        : block !important;
        transition     : all 0.2s !important;
        text-decoration: none !important;
        margin-bottom  : 0.2rem !important;
    }

    [data-testid="stSidebar"] a:hover {
        color      : #2ECC71 !important;
        background : #1A1A1A !important;
    }

    /* ── Typography — dark text on white bg ───────────────────────────────── */
    h1, h2, h3 { color: #1A1A2E !important; }
    p          { color: #2C3E50; }

    /* ── Divider ───────────────────────────────────────────────────────────── */
    hr {
        border-color: #E0E0E0 !important;
        opacity: 1 !important;
    }

    /* ── Global button ─────────────────────────────────────────────────────── */
    .stButton>button {
        background    : #FFFFFF;
        color         : #2C3E50;
        border        : 1px solid #BDC3C7;
        border-radius : 8px;
        font-weight   : 600;
        transition    : all 0.3s;
        width         : 100%;
    }

    .stButton>button:hover {
        border-color : #E74C3C;
        color        : #E74C3C;
    }

    .stButton>button:focus,
    .stButton>button:active,
    .stButton>button:focus:not(:active) {
        box-shadow : none !important;
        outline    : none !important;
    }

    /* ── Metrics ───────────────────────────────────────────────────────────── */
    [data-testid="stMetric"] {
        background    : #FFFFFF;
        border-left   : 3px solid #2ECC71;
        border-radius : 8px;
        padding       : 0.8rem 1rem;
        box-shadow    : 0 1px 4px rgba(0,0,0,0.08);
    }

    [data-testid="stMetricLabel"] p { color: #7F8C8D !important; }
    [data-testid="stMetricValue"]   { color: #1A1A2E !important; }

    /* ── Dataframe ─────────────────────────────────────────────────────────── */
    [data-testid="stDataFrame"] {
        background    : #FFFFFF;
        border-radius : 8px;
        border        : 1px solid #E0E0E0;
        box-shadow    : 0 1px 4px rgba(0,0,0,0.06);
    }

    /* ── Chat messages ─────────────────────────────────────────────────────── */
    [data-testid="stChatMessage"] {
        background    : #FFFFFF;
        border-radius : 10px;
        border        : 1px solid #E0E0E0;
        margin-bottom : 0.5rem;
        box-shadow    : 0 1px 3px rgba(0,0,0,0.06);
    }

    /* ── Text input ────────────────────────────────────────────────────────── */
    .stTextInput input {
        background    : #FFFFFF !important;
        color         : #1A1A2E !important;
        border        : 1px solid #E0E0E0 !important;
        border-radius : 8px !important;
    }
</style>
"""
