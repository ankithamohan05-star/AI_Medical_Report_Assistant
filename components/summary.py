import streamlit as st


def show_summary(report):
    """
    Displays the AI-generated executive summary.
    """

    st.header("📋 Executive Summary")

    st.info(report.executive_summary)

    st.divider()