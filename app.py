import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_helper import generate_summary

from components.dashboard import show_dashboard
from components.patient_info import show_patient_information
from components.summary import show_summary
from components.findings import show_findings
from components.recommendations import show_recommendations
from components.chat import show_chat
from components.footer import show_footer

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="AI Medical Report Assistant",
    page_icon="🩺",
    layout="wide"
)

# ---------------- Load CSS ---------------- #

try:
    with open("assets/style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🩺 AI Medical Report Assistant")

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.markdown("""
- Python
- Streamlit
- Google Gemini 2.5 Flash
- PyMuPDF
- Pydantic
""")

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown("""
✅ AI Medical Summary

✅ Health Dashboard

✅ AI Chat

✅ Structured Report

✅ Professional UI
""")

    st.markdown("---")

    st.subheader("👩‍💻 Developer")

    st.write("Ankitha Mohan")

    st.markdown("---")

    st.caption("Version 2.0")

# ---------------- Main Page ---------------- #

st.title("🩺 AI Medical Report Assistant")

st.write(
    "Upload your medical report PDF and let AI explain it in simple English."
)

st.divider()

uploaded_file = st.file_uploader(
    "📂 Choose your Medical Report",
    type=["pdf"]
)

# ---------------- Process PDF ---------------- #

if uploaded_file:

    st.success("✅ PDF uploaded successfully!")

    extracted_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("🤖 Gemini is analyzing your report..."):

        report = generate_summary(extracted_text)

    if report is None:

        st.error("❌ Failed to generate AI summary.")

    else:

        # Dashboard
        show_dashboard(report)

        # Patient Information
        show_patient_information(report)

        # Executive Summary
        show_summary(report)

        # Findings
        show_findings(report)

        # Recommendations
        show_recommendations(report)

        # Chat
        show_chat(extracted_text)

        # Footer
        show_footer(extracted_text)