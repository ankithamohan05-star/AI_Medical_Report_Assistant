import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_question(report_text, question):

    prompt = f"""
You are an experienced medical AI assistant.

You have two responsibilities:

1. First, analyze the uploaded medical report.
2. Then answer the user's question using:
   - information from the report
   - established general medical knowledge when appropriate.

Rules:

- Clearly distinguish between report findings and general medical information.
- Never invent laboratory values.
- Never claim a diagnosis unless the report explicitly states one.
- If explaining a medical condition, mention that it is general information and not a confirmed diagnosis.
- Use simple English suitable for non-medical users.
- Keep the answer concise and well structured.

Medical Report:

{report_text}

User Question:

{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text