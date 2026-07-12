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


# ---------------- Generate Summary ---------------- #

def generate_summary(report_text):
    """
    Sends the extracted medical report to Gemini
    and returns a structured MedicalReport object.
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

        # Return parsed Pydantic object

        if response.parsed:

            return response.parsed

        return None

    except Exception as e:

        print("Gemini Error:", e)

        return None