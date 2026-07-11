# 🩺 AI Medical Report Assistant

An AI-powered application that analyzes medical reports (PDF) and explains them in simple, easy-to-understand language using Google Gemini AI.

---

## 🚀 Features

- 📄 Upload Medical Report PDFs
- 🔍 Extract text using PyMuPDF
- 🤖 AI-generated medical summary
- 💡 Easy-to-understand explanations
- 🌐 Interactive Streamlit web interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini 2.5 Flash
- Google Gen AI SDK
- PyMuPDF
- python-dotenv

---

## 📂 Project Structure

```
AI_Medical_Report_Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── utils/
│   ├── pdf_reader.py
│   ├── gemini_helper.py
│   ├── prompts.py
│   └── schemas.py
│
├── uploads/
├── reports/
├── assets/
├── sample_reports/
└── screenshots/
```

---

## ✅ Current Features

- PDF Upload
- Text Extraction
- AI Medical Summary

---

## 🚧 Upcoming Features

- Structured AI Report
- Patient Information Card
- Medical Dashboard
- Health Risk Indicators
- Export to PDF
- Chat with Medical Report (RAG)
- Medical History Comparison

---

## ▶️ Installation

```bash
git clone <repository-url>

cd AI_Medical_Report_Assistant

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 👩‍💻 Developer

**Ankitha Mohan**

Medical Electronics Engineering Student

B.M.S College of Engineering

---

## 📜 License

This project is developed for learning and portfolio purposes.