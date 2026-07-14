import os

from dotenv import load_dotenv

from google import genai
from google.genai import types

from utils.prompts import MEDICAL_PROMPT
from utils.schemas import MedicalReport

load_dotenv()

# ---------------- Gemini Client ---------------- #

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


# ---------------- Generate Medical Summary ---------------- #

def generate_summary(report_text):
    """
    Generates a structured medical report from
    extracted report text.
    """

    prompt = f"""
{MEDICAL_PROMPT}

Medical Report

{report_text}
"""

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt,

            config=types.GenerateContentConfig(

                temperature=0.2,

                response_mime_type="application/json",

                response_schema=MedicalReport,

            ),
        )

        if response.parsed:

            return response.parsed

        return None

    except Exception as e:

        print("Gemini Error:", e)

        return None


# ---------------- Comparison Summary ---------------- #

def generate_comparison_summary(comparison_results):
    """
    Generates an AI explanation describing
    how the patient's health has changed.
    """

    if len(comparison_results) == 0:

        return (
            "No common health markers were found "
            "between the two reports."
        )

    comparison_text = ""

    for item in comparison_results:

        comparison_text += f"""

Test: {item.test}

Previous Result: {item.previous_result} {item.unit}

Current Result: {item.current_result} {item.unit}

Difference: {item.difference:+.2f} {item.unit}

Trend: {item.trend}

"""

    prompt = f"""
You are an experienced physician.

Explain the health changes between two
medical reports in very simple English.

Rules:

- Mention only the supplied tests.
- Explain whether each marker has improved,
  worsened or remained stable.
- Do not invent information.
- Keep the explanation under 200 words.
- End with one overall health summary.

Comparison Data

{comparison_text}
"""

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt,

            config=types.GenerateContentConfig(

                temperature=0.2

            ),

        )

        return response.text

    except Exception as e:

        print("Comparison Error:", e)

        return (
            "Unable to generate comparison summary."
        )