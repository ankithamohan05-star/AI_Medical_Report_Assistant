from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    PageBreak,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# ------------------------------------------------ #
# Register Font
# ------------------------------------------------ #

try:
    pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
    FONT_NAME = "Arial"
except Exception:
    FONT_NAME = "Helvetica"


# ------------------------------------------------ #
# Footer
# ------------------------------------------------ #

def draw_footer(canvas, doc):

    canvas.saveState()

    canvas.setStrokeColor(colors.grey)
    canvas.line(
        40,
        35,
        555,
        35
    )

    canvas.setFont(
        FONT_NAME,
        9
    )

    canvas.drawString(
        40,
        20,
        "AI Medical Report Assistant"
    )

    canvas.drawCentredString(
        297,
        20,
        f"Page {doc.page}"
    )

    canvas.drawRightString(
        555,
        20,
        "Generated using Google Gemini AI"
    )

    canvas.restoreState()


# ------------------------------------------------ #
# PDF Generator
# ------------------------------------------------ #

def generate_pdf(report):

    buffer = BytesIO()

    doc = SimpleDocTemplate(

        buffer,

        rightMargin=45,
        leftMargin=45,

        topMargin=45,
        bottomMargin=60

    )

    styles = getSampleStyleSheet()

    # ---------------- Title ---------------- #

    title_style = styles["Heading1"]

    title_style.fontName = FONT_NAME
    title_style.fontSize = 24
    title_style.leading = 30
    title_style.alignment = TA_CENTER
    title_style.textColor = colors.darkblue

    # ---------------- Subtitle ---------------- #

    subtitle_style = styles["Heading2"]

    subtitle_style.fontName = FONT_NAME
    subtitle_style.fontSize = 15
    subtitle_style.leading = 22
    subtitle_style.alignment = TA_CENTER
    subtitle_style.textColor = colors.grey

    # ---------------- Section Heading ---------------- #

    heading_style = styles["Heading2"]

    heading_style.fontName = FONT_NAME
    heading_style.fontSize = 18
    heading_style.leading = 24
    heading_style.spaceAfter = 10
    heading_style.textColor = colors.darkblue

    # ---------------- Body ---------------- #

    body_style = styles["BodyText"]

    body_style.fontName = FONT_NAME
    body_style.fontSize = 11
    body_style.leading = 18
    body_style.spaceAfter = 8

    # ---------------- Small ---------------- #

    small_style = styles["BodyText"]

    small_style.fontName = FONT_NAME
    small_style.fontSize = 10
    small_style.leading = 15
    small_style.textColor = colors.grey

    story = []

    # ==================================================
    # COVER PAGE
    # ==================================================

    story.append(

        Spacer(
            1,
            0.8 * inch
        )

    )

    story.append(

        Paragraph(
            "AI MEDICAL REPORT ASSISTANT",
            title_style
        )

    )

    story.append(

        Spacer(
            1,
            0.15 * inch
        )

    )

    story.append(

        Paragraph(
            "AI Generated Medical Summary",
            subtitle_style
        )

    )

    story.append(

        Spacer(
            1,
            0.5 * inch
        )

    )

    story.append(

        Paragraph(
            "<b>Patient Information</b>",
            heading_style
        )

    )

    patient = report.patient_information

    story.append(
        Paragraph(
            f"<b>Name</b><br/>{patient.name}",
            body_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Age</b><br/>{patient.age}",
            body_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Gender</b><br/>{patient.gender}",
            body_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Report Date</b><br/>{patient.report_date}",
            body_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Generated On</b><br/>{datetime.now().strftime('%d %B %Y')}",
            body_style
        )
    )

    story.append(
        Spacer(
            1,
            0.5 * inch
        )
    )

    story.append(
        Paragraph(
            "<b>Prepared using</b><br/>Google Gemini AI",
            body_style
        )
    )

    story.append(
        Paragraph(
            "<b>Developed by</b><br/>Ankitha Mohan",
            body_style
        )
    )

    story.append(
        Spacer(
            1,
            0.6 * inch
        )
    )

    story.append(

        Paragraph(

            "This report summarizes laboratory findings using Artificial Intelligence."
            "<br/><br/>"
            "It is designed to help patients better understand their medical reports."
            "<br/><br/>"
            "This report must not replace professional medical advice.",

            small_style

        )

    )

    story.append(PageBreak())
    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    story.append(
        Paragraph(
            "Executive Summary",
            heading_style
        )
    )

    story.append(
        Paragraph(
            report.executive_summary,
            body_style
        )
    )

    story.append(
        Spacer(
            1,
            0.25 * inch
        )
    )

    # ==================================================
    # ABNORMAL FINDINGS
    # ==================================================

    story.append(
        Paragraph(
            "Abnormal Findings",
            heading_style
        )
    )

    if len(report.abnormal_findings) == 0:

        story.append(
            Paragraph(
                "No abnormal findings detected.",
                body_style
            )
        )

    else:

        for finding in report.abnormal_findings:

            story.append(
                Paragraph(
                    f"<b>{finding.test}</b>",
                    body_style
                )
            )

            story.append(
                Paragraph(
                    f"<b>Result:</b> {finding.result}",
                    body_style
                )
            )

            story.append(
                Paragraph(
                    f"<b>Reference Range:</b> {finding.normal_range}",
                    body_style
                )
            )

            story.append(
                Paragraph(
                    f"<b>Status:</b> {finding.status}",
                    body_style
                )
            )

            story.append(
                Paragraph(
                    f"<b>Explanation:</b> {finding.explanation}",
                    body_style
                )
            )

            story.append(
                Spacer(
                    1,
                    0.18 * inch
                )
            )

    story.append(PageBreak())

    # ==================================================
    # NORMAL FINDINGS
    # ==================================================

    story.append(
        Paragraph(
            "Normal Findings",
            heading_style
        )
    )

    if len(report.normal_findings) == 0:

        story.append(
            Paragraph(
                "No normal findings available.",
                body_style
            )
        )

    else:

        for group in report.normal_findings:

            story.append(
                Paragraph(
                    f"<b>{group.category}</b>",
                    body_style
                )
            )

            for test in group.tests:

                story.append(
                    Paragraph(
                        f"• {test}",
                        body_style
                    )
                )

            story.append(
                Spacer(
                    1,
                    0.12 * inch
                )
            )

    story.append(PageBreak())

    # ==================================================
    # RECOMMENDATIONS
    # ==================================================

    story.append(
        Paragraph(
            "Recommendations",
            heading_style
        )
    )

    for recommendation in report.recommendations:

        story.append(
            Paragraph(
                f"• {recommendation}",
                body_style
            )
        )

    story.append(
        Spacer(
            1,
            0.30 * inch
        )
    )

    # ==================================================
    # DISCLAIMER
    # ==================================================

    story.append(
        Paragraph(
            "Disclaimer",
            heading_style
        )
    )

    story.append(
        Paragraph(
            report.disclaimer,
            body_style
        )
    )

    # ==================================================
    # BUILD PDF
    # ==================================================

    doc.build(
        story,
        onFirstPage=draw_footer,
        onLaterPages=draw_footer
    )

    buffer.seek(0)

    return buffer