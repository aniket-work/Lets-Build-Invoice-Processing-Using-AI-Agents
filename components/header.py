import streamlit as st
from config.settings import COMPANY_INFO

def render_header():
    st.markdown(f"""
        <div class='custom-header'>
            <h1 style='text-align: center; font-size: 2.5rem; margin-bottom: 0.5rem;'>
                📄 {COMPANY_INFO['name']}
            </h1>
            <p style='text-align: center; color: var(--text-muted-color); font-size: 1.1rem;'>
                {COMPANY_INFO['tagline']}
            </p>
        </div>
    """, unsafe_allow_html=True)