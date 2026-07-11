import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_summary(report_text):

    prompt = f"""
You are an experienced medical AI assistant.

Analyze the following medical report.

Explain everything in simple English.

Your response must contain:

1. Patient Information
2. Executive Summary
3. Abnormal Findings
4. Normal Findings
5. Recommendations
6. Disclaimer

Medical Report:

{report_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text