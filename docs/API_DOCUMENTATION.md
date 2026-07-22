<div align="center">

# 📡 API Documentation

### Enterprise AI Tutor

Complete Service & API Documentation

---

![Version](https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge)
![API](https://img.shields.io/badge/API-Documentation-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

</div>

---

# 📖 Overview

This document describes the core services, methods, and APIs used throughout the Enterprise AI Tutor application.

---

# 🏗️ API Architecture

```text
User

↓

Streamlit Pages

↓

Business Services

↓

AI Providers

↓

Database / FAISS
```

---

# 📂 Core Services

| Service | Purpose |
|----------|----------|
| ProviderService | AI Provider Management |
| ChatService | AI Conversations |
| RAGService | Document Retrieval |
| VoiceService | Voice Processing |
| QuizService | Quiz Generation |
| NotesService | Notes Generation |
| AnalyticsService | Learning Analytics |

---

# 🤖 Provider Service

Handles communication with AI providers.

### Main Methods

```python
generate_response()

list_models()

validate_provider()

health_check()
```

---

# 💬 Chat Service

Handles AI conversations.

### Main Methods

```python
send_message()

get_history()

clear_history()

save_chat()
```

---

# 📚 RAG Service

Provides document-based question answering.

### Main Methods

```python
index_document()

search_documents()

retrieve_chunks()

generate_answer()
```

---

# 🎤 Voice Service

Handles speech processing.

### Main Methods

```python
speech_to_text()

text_to_speech()

voice_chat()

save_session()
```

---

# 📝 Quiz Service

Quiz generation and evaluation.

### Main Methods

```python
generate_quiz()

submit_quiz()

calculate_score()
```

---

# 📒 Notes Service

Creates AI-generated notes.

### Main Methods

```python
generate_notes()

summarize()

export_notes()
```

---

# 📈 Analytics Service

Tracks user learning progress.

### Main Methods

```python
track_usage()

generate_report()

learning_statistics()
```

---

# 🗄️ Database Operations

```python
create()

read()

update()

delete()
```

---

# 📂 Supported File Types

| File Type | Supported |
|-----------|:---------:|
| PDF | ✅ |
| DOCX | ✅ |
| TXT | ✅ |
| CSV | ✅ |
| Markdown | ✅ |

---

# 🔒 Security

- Environment Variables
- Secure API Keys
- Input Validation
- Error Handling
- Logging

---

# 📊 API Summary

| Category | Count |
|-----------|------:|
| Core Services | 7 |
| AI Providers | 3 |
| Database | MySQL |
| Vector Store | FAISS |

