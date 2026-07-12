import streamlit as st


def show_dashboard(report):
    """
    Displays the health dashboard metrics.
    """

    abnormal_count = len(report.abnormal_findings)
    normal_categories = len(report.normal_findings)
    recommendation_count = len(report.recommendations)

    # Demo health score calculation
    health_score = max(100 - abnormal_count * 5, 60)

    st.header("📊 Health Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "❤️ Health Score",
            f"{health_score}/100"
        )

    with col2:
        st.metric(
            "⚠️ Abnormal Findings",
            abnormal_count
        )

    with col3:
        st.metric(
            "✅ Normal Categories",
            normal_categories
        )

    with col4:
        st.metric(
            "💡 Recommendations",
            recommendation_count
        )

    st.divider()