import streamlit as st


def calculate_health_score(report):
    """
    Calculates a health score based on the severity
    of abnormal findings.
    """

    score = 100

    severity_penalty = {
        "Low": 2,
        "Medium": 7,
        "High": 15,
        "Critical": 25
    }

    for finding in report.abnormal_findings:

        score -= severity_penalty.get(
            finding.severity,
            5
        )

    score = max(score, 0)

    return score


def health_status(score):

    if score >= 95:
        return "🟢 Excellent"

    elif score >= 85:
        return "🟢 Very Good"

    elif score >= 70:
        return "🟡 Good"

    elif score >= 55:
        return "🟠 Fair"

    return "🔴 Needs Attention"


def show_dashboard(report):
    """
    Displays dashboard metrics.
    """

    score = calculate_health_score(report)

    abnormal_count = len(report.abnormal_findings)

    normal_categories = len(report.normal_findings)

    recommendation_count = len(report.recommendations)

    st.header("📊 Health Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "❤️ Health Score",
            f"{score}/100"
        )

        st.caption(
            health_status(score)
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

    # ---------------- Priority Alerts ---------------- #

    priority_items = [
        finding
        for finding in report.abnormal_findings
        if finding.priority in [
            "Needs Attention",
            "Urgent"
        ]
    ]

    if priority_items:

        st.subheader("🚨 Priority Alerts")

        for finding in priority_items:

            st.warning(
                f"**{finding.test}** — {finding.priority}"
            )

        st.divider()