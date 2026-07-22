<div align="center">

# ❓ Frequently Asked Questions (FAQ)

### Enterprise AI Tutor

Find answers to the most common questions about Enterprise AI Tutor.

---

![Version](https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge)
![FAQ](https://img.shields.io/badge/FAQ-Documentation-success?style=for-the-badge)
![Support](https://img.shields.io/badge/Support-Available-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge)

</div>

---

# 📖 Overview

This document answers frequently asked questions regarding installation, configuration, AI providers, Enterprise RAG, Voice AI, and troubleshooting.

---

# 🚀 General Questions

## 1. What is Enterprise AI Tutor?

Enterprise AI Tutor is an AI-powered learning platform that combines intelligent tutoring, Enterprise RAG, Voice AI, study planning, quizzes, coding assistance, and learning analytics into a single application.

---

## 2. Which programming language is used?

The project is built using **Python**.

---

## 3. Which framework is used?

The user interface is developed using **Streamlit**.

---

## 4. Which database is used?

The application uses **MySQL** for storing application data.

---

## 5. Which vector database is used?

The project uses **FAISS** for semantic document retrieval.

---

# 🤖 AI Providers

## 6. Which AI providers are supported?

The application supports:

- Ollama
- OpenAI
- Anthropic

---

## 7. Can I use only Ollama?

Yes.

The application supports running entirely with local Ollama models.

---

## 8. Can I switch providers?

Yes.

You can change providers directly from the application without changing the code.

---

# 📚 Enterprise RAG

## 9. What is Enterprise RAG?

Enterprise RAG retrieves relevant document content before generating an AI response, improving accuracy and reducing hallucinations.

---

## 10. Which document formats are supported?

Supported formats include:

- PDF
- DOCX
- TXT
- CSV
- Markdown

---

## 11. Which retrieval methods are available?

- Semantic Search
- Keyword Search
- Hybrid Search
- Parent-Child Retrieval
- Multi Query Retrieval
- HyDE Retrieval

---

# 🎤 Voice AI

## 12. What is Voice AI Tutor?

Voice AI Tutor allows users to interact with the AI using speech instead of typing.

---

## 13. Which speech technologies are used?

- Faster Whisper (Speech-to-Text)
- gTTS (Text-to-Speech)

---

## 14. Is voice history saved?

Yes.

Voice conversations can be stored and viewed through the Voice History module.

---

# 📊 Learning Features

## 15. Which learning tools are available?

- AI Tutor
- AI Mentor
- Quiz Generator
- Flashcards
- Notes Generator
- PDF Tutor
- Coding Tutor
- Study Planner
- Revision Planner

---

## 16. Does the application track learning progress?

Yes.

Learning Analytics provides progress tracking and usage statistics.

---

# ⚙️ Installation

## 17. How do I start the application?

```bash
streamlit run app.py
```

---

## 18. Which Python version is recommended?

Python **3.12 or later**.

---

## 19. Is MySQL required?

Yes.

MySQL is used as the primary database.

---

## 20. Is Ollama required?

Only if you plan to use local AI models.

---

# 🔒 Security

## 21. Where should API keys be stored?

Store API keys securely in the `.env` file.

---

## 22. Is API key protection supported?

Yes.

Sensitive information is managed through environment variables.

---

# 🐞 Troubleshooting

## 23. The application won't start.

Check:

- Python installation
- Virtual environment
- Dependencies
- Streamlit installation

---

## 24. MySQL connection failed.

Verify:

- MySQL service is running
- Database exists
- Credentials are correct

---

## 25. Ollama is not responding.

Start the Ollama server.

```bash
ollama serve
```

---

## 26. AI model is not available.

Ensure the required model has been downloaded.

Example:

```bash
ollama pull qwen2.5:1.5b
```

---

## 27. Why are RAG results empty?

Possible reasons:

- No documents uploaded
- Index not created
- Empty document
- Unsupported file format

---

# 📞 Support

If you still need help:

- Read the documentation
- Check the Troubleshooting Guide
- Review the project configuration
- Create a GitHub Issue

---

# 📋 Quick Summary

| Question | Answer |
|----------|--------|
| Python | 3.12+ |
| Framework | Streamlit |
| Database | MySQL |
| Vector Store | FAISS |
| AI Providers | Ollama, OpenAI, Anthropic |
| Voice AI | Faster Whisper + gTTS |

