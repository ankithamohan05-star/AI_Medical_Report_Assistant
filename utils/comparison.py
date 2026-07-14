from utils.marker_normalizer import normalize_marker
from utils.schemas import ComparisonResult


# ------------------------------------------------ #
# Determine Trend
# ------------------------------------------------ #

def determine_trend(test_name, previous, current):
    """
    Determines whether a change is good or bad.

    Returns:
        Improved
        Worsened
        Stable
        Changed
    """

    test = test_name.lower()

    # Higher is Better
    higher_is_better = [
        "vitamin d",
        "vitamin b12",
        "hdl",
        "hemoglobin"
    ]

    # Lower is Better
    lower_is_better = [
        "tsh",
        "ldl",
        "cholesterol",
        "triglycerides",
        "glucose",
        "hba1c",
        "mch",
        "mchc",
        "mentzer",
        "rdwi"
    ]

    if abs(current - previous) < 0.0001:
        return "Stable"

    for keyword in higher_is_better:

        if keyword in test:

            if current > previous:
                return "Improved"
            else:
                return "Worsened"

    for keyword in lower_is_better:

        if keyword in test:

            if current < previous:
                return "Improved"
            else:
                return "Worsened"

    return "Changed"


# ------------------------------------------------ #
# Compare Reports
# ------------------------------------------------ #

def compare_reports(previous_report, current_report):
    """
    Compares two structured MedicalReport objects.

    Returns
    -------
    list[ComparisonResult]
    """

    comparison_results = []

    previous_tests = {

        normalize_marker(finding.test): finding

        for finding in previous_report.abnormal_findings

        if finding.numeric_result is not None

    }

    for current in current_report.abnormal_findings:

        if current.numeric_result is None:
            continue

        key = normalize_marker(current.test)

        if key not in previous_tests:
            continue

        previous = previous_tests[key]

        difference = round(
            current.numeric_result - previous.numeric_result,
            2
        )

        trend = determine_trend(
            current.test,
            previous.numeric_result,
            current.numeric_result
        )

        comparison_results.append(

            ComparisonResult(

                test=current.test,

                previous_result=previous.result,

                current_result=current.result,

                previous_numeric=previous.numeric_result,

                current_numeric=current.numeric_result,

                unit=current.unit,

                difference=difference,

                trend=trend

            )

        )

    return comparison_results