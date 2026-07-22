<div align="center">

# 🛠️ Installation Guide

### Enterprise AI Tutor

Quick Setup Guide for Windows, Linux, and macOS

---

![Version](https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge&logo=streamlit)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

</div>

---

# 📖 Overview

This guide explains how to install and configure the Enterprise AI Tutor project on your local machine.

---

# ✅ Prerequisites

Install the following software before running the project.

| Software | Version |
|-----------|---------|
| Python | 3.12+ |
| Git | Latest |
| MySQL | 8.0+ |
| Ollama | Latest |

---

# 📥 Clone Repository

```bash
git clone https://github.com/satya66123/AI-Tutor.git

cd AI-Tutor
```

---

# 🐍 Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ Configure MySQL

Create a new database.

```sql
CREATE DATABASE ai_tutor;
```

Update your database configuration.

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=ai_tutor
```

---

# 🤖 Configure AI Providers

Edit the **.env** file.

```env
OPENAI_API_KEY=

ANTHROPIC_API_KEY=

OLLAMA_HOST=http://localhost:11434
```

---

# 🦙 Install Ollama

Download and install Ollama.

Start the Ollama server.

```bash
ollama serve
```

Download a model.

Example:

```bash
ollama pull qwen2.5:1.5b
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🌐 Open in Browser

```
http://localhost:8501
```

---

# 📂 Project Structure

```text
AI-Tutor/

├── app.py
├── config/
├── database/
├── pages/
├── services/
├── utils/
├── uploads/
├── docs/
└── requirements.txt
```

---

# ✅ Verify Installation

Check the following:

- Application starts successfully
- MySQL connection works
- Ollama is running
- AI providers are available
- Streamlit dashboard opens

---

# ❗ Common Issues

### MySQL Connection Error

- Verify MySQL is running
- Check database credentials
- Ensure database exists

---

### Ollama Not Running

```bash
ollama serve
```

---

### Missing Python Package

```bash
pip install -r requirements.txt
```

---

### Streamlit Not Found

```bash
pip install streamlit
```

---

# 📋 Installation Checklist

| Task | Status |
|------|:------:|
| Python Installed | ✅ |
| Virtual Environment Created | ✅ |
| Dependencies Installed | ✅ |
| MySQL Configured | ✅ |
| Ollama Installed | ✅ |
| Environment Variables Added | ✅ |
| Application Running | ✅ |

---

# 🎉 Installation Complete

You are now ready to use **Enterprise AI Tutor**.

Continue with the **USER_GUIDE.md** to learn how to use the application.

