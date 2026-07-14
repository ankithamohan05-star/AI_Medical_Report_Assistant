import streamlit as st


def status_color(status):

    status = status.lower()

    if "critical" in status:
        return "#dc3545"

    if "high" in status:
        return "#fd7e14"

    if "low" in status:
        return "#ffc107"

    if "insufficient" in status:
        return "#ffc107"

    if "borderline" in status:
        return "#ffc107"

    return "#0d6efd"


def show_findings(report):

    # ---------------- Abnormal Findings ---------------- #

    st.header("⚠️ Abnormal Findings")

    if len(report.abnormal_findings) == 0:

        st.success("✅ No abnormal findings detected.")

    else:

        for finding in report.abnormal_findings:

            color = status_color(finding.status)

            st.markdown(
                f"""
<div class="medical-card">

<div class="finding-title">
{finding.test}
</div>

<p class="finding-value">
<b>🧪 Result:</b> {finding.result}
</p>

<p class="finding-value">
<b>📏 Reference Range:</b> {finding.normal_range}
</p>

<p class="finding-value">
<b>🚦 Status:</b>
<span style="color:{color}; font-weight:bold;">
{finding.status}
</span>
</p>

<p class="finding-value">
<b>🩺 Explanation</b>
</p>

<p>
{finding.explanation}
</p>

</div>
""",
                unsafe_allow_html=True,
            )

    st.divider()

    # ---------------- Normal Findings ---------------- #

    st.header("✅ Normal Findings")

    if len(report.normal_findings) == 0:

        st.info("No normal findings available.")

    else:

        for group in report.normal_findings:

            with st.expander(f"📂 {group.category}", expanded=False):

                for test in group.tests:

                    st.markdown(f"✅ {test}")

    st.divider()