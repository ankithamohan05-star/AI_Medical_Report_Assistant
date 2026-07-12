import streamlit as st


def show_recommendations(report):
    """
    Displays AI-generated recommendations and disclaimer.
    """

    st.header("💡 Recommendations")

    if len(report.recommendations) == 0:

        st.info("No recommendations available.")

    else:

        for recommendation in report.recommendations:

            st.success(f"✔ {recommendation}")

    st.divider()

    st.warning(report.disclaimer)

    st.divider()