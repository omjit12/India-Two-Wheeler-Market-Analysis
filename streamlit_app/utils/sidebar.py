import streamlit as st

def render_sidebar(bikes_df=None):
    with st.sidebar:

        # ── Logo ──────────────────────────────────────────────────────────────
        st.markdown("""
        <div style="text-align:center; padding:0.2rem 0;
                    border-bottom:1px solid #2ECC71; margin-bottom:0.5rem;">
            <div style="font-size:1.8rem;">🏍️</div>
            <div style="color:#FFFFFF; font-weight:800;
                        font-size:1.05rem; letter-spacing:0.5px;">
                India Bike Market
            </div>
            <div style="color:#7F8C8D; font-size:0.72rem; margin-top:2px;">
                Two-Wheeler Analysis 2019–2023
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Navigation ────────────────────────────────────────────────────────
        st.markdown("""
        <div style="color:#2ECC71; font-size:0.72rem; font-weight:700;
                    letter-spacing:0.12em; text-transform:uppercase;
                    margin-bottom:0.6rem; padding-left:0.3rem;">
            Navigation
        </div>
        """, unsafe_allow_html=True)

        st.page_link("app.py",                label="🏠   Home")
        st.page_link("pages/01_chatbot.py",   label="🤖   AI Market Analyst")
        st.page_link("pages/02_recommend.py", label="🎯   Bike Recommender")

        # ── Quick Stats ───────────────────────────────────────────────────────
        if bikes_df is not None:
            st.markdown("""
            <div style="color:#2ECC71; font-size:0.72rem; font-weight:700;
                        letter-spacing:0.12em; text-transform:uppercase;
                        margin-top:1.2rem; margin-bottom:0.6rem;
                        padding-left:0.3rem; border-top:1px solid #2C3E50;
                        padding-top:1.2rem;">
                Market Snapshot
            </div>
            """, unsafe_allow_html=True)

            stats = [
                ("#3498DB", "Total Bikes",      len(bikes_df)),
                ("#3498DB", "Brands",           bikes_df['brand'].nunique()),
                ("#F39C12", "Segments",         bikes_df['segment'].nunique()),
                ("#2ECC71", "EV Market Share",  "10.6%"),
                ("#F39C12", "Years Covered",    "2019–2023"),
                ("#FFFFFF", "Total Sales",      "144M units"),
            ]

            for color, label, value in stats:
                st.markdown(f"""
                <div style="display:flex; justify-content:space-between;
                            align-items:center; padding:0.25rem 0.3rem;
                            border-bottom:1px solid #2C3E50;
                            font-size:0.82rem;">
                    <span style="color:#BDC3C7; display:flex;
                                 align-items:center; gap:8px;">
                        <span style="width:7px; height:7px; border-radius:50%;
                                     background:{color}; display:inline-block;
                                     flex-shrink:0;"></span>
                        {label}
                    </span>
                    <span style="color:{color}; font-weight:700;
                                 font-size:0.85rem;">{value}</span>
                </div>
                """, unsafe_allow_html=True)

