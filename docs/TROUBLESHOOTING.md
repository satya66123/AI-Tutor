<div align="center">

# 🩺 Troubleshooting Guide

### Enterprise AI Tutor

Solutions for common installation, configuration, and runtime issues.

---

![Version](https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge)
![Support](https://img.shields.io/badge/Support-Troubleshooting-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)
![Documentation](https://img.shields.io/badge/Documentation-Complete-blueviolet?style=for-the-badge)

</div>

---

# 📖 Overview

This guide provides solutions for common issues that may occur while installing, configuring, or using Enterprise AI Tutor.

---

# 📋 Common Issues

| Issue | Solution |
|--------|----------|
| Python Not Found | Install Python and add it to PATH |
| Streamlit Not Installed | Install using pip |
| MySQL Connection Failed | Verify database configuration |
| Ollama Not Running | Start the Ollama server |
| OpenAI API Error | Check API key |
| Anthropic API Error | Verify API key |
| Voice AI Not Working | Install speech dependencies |
| RAG Search Empty | Index documents again |

---

# 🐍 Python Issues

## Problem

Python command not recognized.

### Solution

Check Python installation.

```bash
python --version
```

If Python is not installed, download and install Python 3.12 or later.

---

# 📦 Dependency Issues

## Problem

Package not found.

### Solution

Install all dependencies.

```bash
pip install -r requirements.txt
```

Upgrade pip if needed.

```bash
python -m pip install --upgrade pip
```

---

# 🎨 Streamlit Issues

## Problem

Streamlit command not found.

### Solution

Install Streamlit.

```bash
pip install streamlit
```

Verify installation.

```bash
streamlit --version
```

Run the application.

```bash
streamlit run app.py
```

---

# 🗄️ MySQL Issues

## Problem

Unable to connect to MySQL.

### Verify

- MySQL Server is running
- Database exists
- Username is correct
- Password is correct
- Port is correct

Example configuration

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=ai_tutor
```

---

# 🤖 Ollama Issues

## Problem

Ollama is not responding.

### Solution

Start Ollama.

```bash
ollama serve
```

Verify installation.

```bash
ollama list
```

Download a model.

```bash
ollama pull qwen2.5:1.5b
```

---

# 🌐 OpenAI Issues

## Problem

Authentication Error

### Solution

Verify API key.

```env
OPENAI_API_KEY=your_api_key
```

Restart the application after updating the key.

---

# 🧠 Anthropic Issues

## Problem

Claude API Error

### Solution

Verify the API key.

```env
ANTHROPIC_API_KEY=your_api_key
```

---

# 📚 Enterprise RAG Issues

## Problem

No response from RAG.

### Check

- Document uploaded
- Text extracted successfully
- Embeddings generated
- FAISS index created

Re-index the document if necessary.

---

# 📄 Document Upload Issues

Supported formats:

- PDF
- DOCX
- TXT
- CSV
- Markdown

Avoid corrupted or password-protected files.

---

# 🔍 FAISS Issues

## Problem

No search results.

### Solution

- Rebuild the vector index
- Verify embeddings
- Upload documents again

---

# 🎤 Voice AI Issues

## Problem

Speech is not recognized.

### Verify

- Microphone permission
- Audio quality
- Speech dependencies
- Input device

---

## Problem

Audio does not play.

### Solution

- Check speaker volume
- Verify generated audio file
- Restart the application

---

# 💬 AI Response Issues

## Problem

Slow responses.

### Possible Causes

- Large document
- Slow internet connection
- Large AI model
- High server load

---

## Problem

No AI response.

### Verify

- Provider selected
- Model available
- API key configured
- Ollama running

---

# ⚙️ Configuration Issues

Verify your `.env` file.

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=ai_tutor

OPENAI_API_KEY=

ANTHROPIC_API_KEY=

OLLAMA_HOST=http://localhost:11434
```

---

# 📝 Log Files

Check logs for detailed error information.

```text
logs/

app.log

error.log

provider.log

rag.log
```

---

# 🔄 Reset Application

If issues persist:

1. Delete temporary files
2. Reinstall dependencies
3. Restart MySQL
4. Restart Ollama
5. Restart Streamlit

---

# 📋 Troubleshooting Checklist

| Check | Status |
|--------|:------:|
| Python Installed | ✅ |
| Dependencies Installed | ✅ |
| Streamlit Running | ✅ |
| MySQL Running | ✅ |
| Ollama Running | ✅ |
| API Keys Configured | ✅ |
| Documents Indexed | ✅ |

---

# 📞 Need More Help?

If the issue continues:

- Review the installation guide
- Check application logs
- Verify your configuration
- Create a GitHub issue with the error details

