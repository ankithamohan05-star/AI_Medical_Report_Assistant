# 🩺 AI Medical Report Assistant

An AI-powered web application that analyzes medical reports, explains complex laboratory results in simple language, compares reports over time, and generates personalized health insights.

Built using **Python**, **Streamlit**, **Google Gemini 2.5 Flash**, **OCR**, and **Pydantic**.

---

## ✨ Features

- 📄 Upload PDF and image-based medical reports
- 🔍 OCR support for scanned reports using EasyOCR
- 🤖 AI-generated medical report summaries
- 📊 Health Dashboard with overall health score
- ⚠️ Detection and explanation of abnormal findings
- ✅ Categorized normal findings
- 💡 Personalized health recommendations
- 📈 Compare two medical reports and track health progress
- 💬 AI chatbot to answer questions about the uploaded report
- 📥 Export AI-generated summary as a PDF

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend logic |
| Streamlit | Web application |
| Google Gemini 2.5 Flash | AI report analysis |
| EasyOCR | Text extraction from images |
| PyMuPDF | PDF text extraction |
| Pydantic | Structured data validation |
| ReportLab | PDF report generation |

---

## 📂 Project Structure

```text
AI_Medical_Report_Assistant/
│
├── assets/                 # CSS styling
├── components/             # Streamlit UI components
├── utils/                  # OCR, AI, comparison and helper functions
├── sample_reports/         # Sample reports for testing
├── screenshots/            # Project screenshots
├── app.py                  # Main application
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<ankithamohan05-star>/AI_Medical_Report_Assistant.git
```

Navigate into the project

```bash
cd AI_Medical_Report_Assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Screenshots of the application are available in the `screenshots` folder.

Example pages include:

- Health Dashboard
- Executive Summary
- Abnormal Findings
- Previous Report Comparison
- AI Chat
- PDF Export

---

## 🔮 Future Improvements

- Support reports from more laboratory formats
- Interactive trend charts for health markers
- Multi-language support
- User authentication
- Cloud database for report history

---

## 👩‍💻 Developer

**Ankitha Mohan**

Medical Electronics Engineering Student

---

## ⚠️ Disclaimer

This application provides AI-generated explanations for educational and informational purposes only. It is **not** intended to replace professional medical advice, diagnosis, or treatment.