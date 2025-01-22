import streamlit as st
import ollama
from PIL import Image
from config.settings import APP_CONFIG, COMPANY_INFO, THEME


def load_css():
    st.markdown(f"""
        <style>
            :root {{
                --primary-color: {THEME['colors']['primary']};
                --primary-hover-color: {THEME['colors']['primary_hover']};
                --background-color: {THEME['colors']['background']};
                --card-bg-color: {THEME['colors']['card_bg']};
                --border-color: {THEME['colors']['border']};
                --text-color: {THEME['colors']['text']};
                --text-secondary-color: {THEME['colors']['text_secondary']};
                --text-muted-color: {THEME['colors']['text_muted']};
            }}
        </style>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(**APP_CONFIG)
    load_css()

    # Header
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

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### Upload Invoice")
        uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg', 'pdf'])

        if uploaded_file:
            try:
                image = Image.open(uploaded_file)
                st.image(image, use_column_width=True)
                process_button = st.button("Process Invoice 🔍", use_container_width=True)
            except Exception:
                st.error("Error loading image. Please try again.")

    with col2:
        st.markdown("### Analysis Results")
        if 'ocr_result' in st.session_state:
            st.markdown("<div class='results-card'>", unsafe_allow_html=True)
            st.markdown(st.session_state['ocr_result'])
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("👆 Upload an invoice to see the analysis results here")

    if uploaded_file and process_button:
        with st.spinner("Processing your invoice..."):
            try:
                response = ollama.chat(
                    model='llama3.2-vision',
                    messages=[{
                        'role': 'user',
                        'content': """Extract and format the following in clear markdown:
                            - Invoice number and date
                            - Company details
                            - Items and amounts
                            - Total and taxes
                            - Payment terms""",
                        'images': [uploaded_file.getvalue()]
                    }]
                )
                st.session_state['ocr_result'] = response.message.content
                st.rerun()
            except Exception:
                st.error("Processing failed. Please try again.")

    st.markdown(f"""
        <div class='footer' style='text-align: center;'>
            {COMPANY_INFO['copyright']}
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()