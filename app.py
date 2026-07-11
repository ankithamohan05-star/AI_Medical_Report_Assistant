import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_helper import generate_summary

st.set_page_config(
    page_title="AI Medical Report Assistant",
    page_icon="🩺",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

with st.sidebar:
    st.title("🩺 AI Medical Report Assistant")

    st.markdown("---")

    st.subheader("🛠 Built With")

    st.markdown("""
- Python
- Streamlit
- Google Gemini 2.5 Flash
- PyMuPDF
    """)

    st.markdown("---")

    st.subheader("👩‍💻 Developer")

    st.write("Ankitha Mohan")

    st.markdown("---")

    st.caption("Version 1.0")

# ---------------- Main Page ---------------- #

st.title("🩺 AI Medical Report Assistant")

st.write(
    "Upload your medical report PDF and let AI explain the results in simple English."
)

st.divider()

uploaded_file = st.file_uploader(
    "📂 Choose your Medical Report (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("✅ PDF uploaded successfully!")

    extracted_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("🤖 Gemini is analyzing your report..."):

        summary = generate_summary(extracted_text)

    st.divider()

    with st.container():

        st.subheader("🤖 AI Medical Summary")

        st.write(summary)

    st.divider()

    with st.expander("📄 View Extracted Medical Report"):

        st.text_area(
            "Extracted Text",
            extracted_text,
            height=400
        )

st.divider()

st.caption(
    "⚠️ This application provides AI-generated explanations and should not replace professional medical advice."
)