import streamlit as st


def show_patient_information(report):
    """
    Displays patient information in four metric cards.
    """

    st.header("👤 Patient Information")

    patient = report.patient_information

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Name",
            patient.name
        )

    with col2:
        st.metric(
            "Age",
            patient.age
        )

    with col3:
        st.metric(
            "Gender",
            patient.gender
        )

    with col4:
        st.metric(
            "Report Date",
            patient.report_date
        )

    st.divider()