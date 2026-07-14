import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.ocr_reader import extract_text_from_image

from utils.gemini_helper import (
    generate_summary,
    generate_comparison_summary
)

from utils.comparison import compare_reports

from components.dashboard import show_dashboard
from components.patient_info import show_patient_information
from components.summary import show_summary
from components.findings import show_findings
from components.recommendations import show_recommendations
from components.comparison import show_comparison
from components.chat import show_chat
from components.footer import show_footer
from components.pdf_export import generate_pdf

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
except FileNotFoundError:
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
- EasyOCR
- Pydantic
- ReportLab
""")

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown("""
✅ PDF Report Upload

✅ Image Report Upload

✅ AI Medical Summary

✅ Health Dashboard

✅ Previous Report Comparison

✅ AI Chat

✅ PDF Export
""")

    st.markdown("---")

    st.subheader("👩‍💻 Developer")

    st.write("Ankitha Mohan")

    st.markdown("---")

    st.caption("Version 2.5")

# ---------------- Main Page ---------------- #

st.title("🩺 AI Medical Report Assistant")

st.write(
    "Upload a medical report as a PDF or an image and let AI explain it in simple English."
)

st.divider()

uploaded_file = st.file_uploader(
    "📂 Choose your Medical Report",
    type=["pdf", "png", "jpg", "jpeg"]
)

# ---------------- Process Current Report ---------------- #

if uploaded_file:

    st.success("✅ File uploaded successfully!")

    extension = uploaded_file.name.split(".")[-1].lower()

    with st.spinner("📄 Extracting report..."):

        if extension == "pdf":
            extracted_text = extract_text_from_pdf(uploaded_file)
        else:
            extracted_text = extract_text_from_image(uploaded_file)

    if not extracted_text.strip():

        st.error("❌ Unable to extract text from the uploaded report.")

        st.stop()

    with st.spinner("🤖 Gemini is analyzing your report..."):

        report = generate_summary(extracted_text)

    if report is None:

        st.error("❌ Failed to generate AI summary.")

        st.stop()

    # ---------------- Dashboard ---------------- #

    show_dashboard(report)

    # ---------------- Patient Information ---------------- #

    show_patient_information(report)

    # ---------------- Executive Summary ---------------- #

    show_summary(report)

    # ---------------- Findings ---------------- #

    show_findings(report)

    # ---------------- Recommendations ---------------- #

    show_recommendations(report)

    # =======================================================
    # Compare With Previous Report
    # =======================================================

    st.divider()

    st.header("📈 Compare With Previous Report (Optional)")

    st.write(
        "Track how your health markers have changed since your last medical report."
    )

    previous_file = st.file_uploader(
        "📂 Upload Previous Medical Report\n\nSupports PDF, JPG, PNG and JPEG",
        type=["pdf", "png", "jpg", "jpeg"],
        key="previous_report"
    )

    if previous_file is not None:

        if st.button("📈 Compare Reports"):

            previous_extension = previous_file.name.split(".")[-1].lower()

            with st.spinner("📄 Reading previous report..."):

                if previous_extension == "pdf":

                    previous_text = extract_text_from_pdf(previous_file)

                else:

                    previous_text = extract_text_from_image(previous_file)
            if not previous_text.strip():
                st.error("❌ Unable to extract text from the previous report.")
                st.stop()

            with st.spinner("🤖 Gemini is analyzing previous report..."):

                previous_report = generate_summary(previous_text)

            if previous_report is None:

                st.error("❌ Failed to analyze previous report.")

            else:
                
                comparison_results = compare_reports(
                    previous_report,
                    report
                )

                comparison_summary = generate_comparison_summary(
                    comparison_results
                )

                show_comparison(
                    comparison_results,
                    comparison_summary
                )

    # ---------------- AI Chat ---------------- #

    show_chat(extracted_text)

    # ---------------- PDF Download ---------------- #

    st.divider()

    st.header("📥 Export Report")

    pdf = generate_pdf(report)

    st.download_button(
        label="📄 Download AI Summary (PDF)",
        data=pdf,
        file_name="AI_Medical_Report_Summary.pdf",
        mime="application/pdf"
    )

    # ---------------- Footer ---------------- #

    show_footer(extracted_text)