import streamlit as st


def show_findings(report):
    """
    Displays abnormal and normal findings.
    """

    # ---------------- Abnormal Findings ---------------- #

    st.header("⚠️ Abnormal Findings")

    if len(report.abnormal_findings) == 0:

        st.success("🎉 No abnormal findings detected.")

    else:

        for finding in report.abnormal_findings:

            with st.container():

                st.error(f"🔴 {finding.test}")

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Result:** {finding.result}")

                with col2:
                    st.write(f"**Status:** {finding.status}")

                st.write(f"**Normal Range:** {finding.normal_range}")

                st.write(f"**Explanation:**")

                st.info(finding.explanation)

                st.markdown("---")

    st.divider()

    # ---------------- Normal Findings ---------------- #

    st.header("✅ Normal Findings")

    if len(report.normal_findings) == 0:

        st.warning("No normal findings available.")

    else:

        for group in report.normal_findings:

            with st.expander(f"📂 {group.category}", expanded=False):

                for test in group.tests:

                    st.write(f"✅ {test}")

    st.divider()