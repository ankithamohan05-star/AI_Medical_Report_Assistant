import streamlit as st


def trend_icon(trend):

    trend = trend.lower()

    if trend == "improved":
        return "🟢 Improved"

    if trend == "worsened":
        return "🔴 Worsened"

    if trend == "stable":
        return "🔵 Stable"

    return "🟡 Changed"


def show_comparison(comparison_results, comparison_summary):

    st.divider()

    st.header("📈 Health Progress")

    if len(comparison_results) == 0:

        st.info(
            "No common health markers were found between the two reports."
        )

        return

    for result in comparison_results:

        st.markdown(
            f"""
<div class="medical-card">

<div class="finding-title">
{result.test}
</div>

<p class="finding-value">
<b>📄 Previous Report:</b> {result.previous_result} {result.unit}
</p>

<p class="finding-value">
<b>📄 Current Report:</b> {result.current_result} {result.unit}
</p>

<p class="finding-value">
<b>📊 Difference:</b> {result.difference:+.2f} {result.unit}
</p>

<p class="finding-value">
<b>📈 Trend:</b> {trend_icon(result.trend)}
</p>

</div>
""",
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("🤖 AI Comparison Summary")

    st.info(comparison_summary)