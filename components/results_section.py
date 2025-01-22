import streamlit as st
def render_results_section():
    st.markdown("### Analysis Results")
    if 'ocr_result' in st.session_state:
        st.markdown("<div class='results-card'>", unsafe_allow_html=True)
        st.markdown(st.session_state['ocr_result'])
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("👆 Upload an invoice to see the analysis results here")