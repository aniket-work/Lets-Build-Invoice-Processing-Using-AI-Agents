from PIL import Image
from config.settings import UPLOAD_CONFIG
import streamlit as st

def render_upload_section():
    st.markdown("### Upload Invoice")
    uploaded_file = st.file_uploader(
        "",
        type=UPLOAD_CONFIG['allowed_types'],
        help=UPLOAD_CONFIG['help_text']
    )

    if uploaded_file:
        try:
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True)
            process_button = st.button("Process Invoice 🔍", use_container_width=True)
            return uploaded_file, process_button
        except Exception:
            st.error("Error loading image. Please try again.")

    return None, None