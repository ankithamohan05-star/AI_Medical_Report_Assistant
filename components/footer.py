import streamlit as st


def show_footer(extracted_text):
    """
    Displays the extracted report and application footer.
    """

    st.header("📄 View Extracted Medical Report")

    with st.expander("Click to view extracted report"):

        st.text_area(
            "Extracted Text",
            extracted_text,
            height=400
        )

    st.divider()

    st.caption(
        "⚠️ This application provides AI-generated explanations and should not replace professional medical advice."
    )