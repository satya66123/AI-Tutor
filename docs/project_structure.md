<div align="center">

# 📂 Enterprise AI Tutor Project Structure

### Complete Repository Organization & Directory Reference

A detailed guide to the project folder hierarchy, modules, services, and architecture.

---

![Version](https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-Enterprise-success?style=for-the-badge)
![Documentation](https://img.shields.io/badge/Documentation-Complete-blueviolet?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-009688?style=for-the-badge)

</div>

---

# 📖 Overview

The Enterprise AI Tutor project follows a modular, scalable, and enterprise-grade architecture. Every component is organized into dedicated directories to improve maintainability, extensibility, and readability.

---

# 📑 Project Structure

```text
AI-Tutor/
│
├── app.py
├── requirements.txt
├── README.md
│
├── config/
├── database/
├── docs/
├── logs/
├── models/
├── pages/
├── prompts/
├── services/
├── ui/
├── uploads/
├── utils/
├── vector_store/
├── static/
├── tests/
└── assets/
```

---

# 📁 Root Directory

The root directory contains the primary application entry point and project configuration files.

| File | Description |
|------|-------------|
| app.py | Main Streamlit application |
| requirements.txt | Python dependencies |
| README.md | Project overview |
| LICENSE | Project license |
| .gitignore | Git ignore configuration |
| .env | Environment variables |

---

# ⚙ config/

Stores all application configuration files.

## Responsibilities

- Environment Configuration
- AI Provider Configuration
- Database Configuration
- Application Settings
- Logging Configuration

Example

```text
config/
│
├── config.py
├── database_config.py
├── provider_config.py
├── rag_config.py
└── settings.py
```

---

# 🗄 database/

Responsible for database operations.

## Responsibilities

- Database Connection
- CRUD Operations
- Table Creation
- Query Execution
- Transaction Management

Example

```text
database/
│
├── database.py
├── models.py
├── migrations.py
├── user_repository.py
└── history_repository.py
```

---

# 📄 docs/

Contains complete project documentation.

```text
docs/
│
├── README.md
├── FEATURES.md
├── PROJECT_STRUCTURE.md
├── ARCHITECTURE.md
├── SYSTEM_DESIGN.md
├── DATABASE.md
├── RAG_ARCHITECTURE.md
├── VOICE_AI_TUTOR.md
├── PROVIDER_GUIDE.md
├── INSTALLATION.md
├── USER_GUIDE.md
├── API_DOCUMENTATION.md
├── CHANGELOG.md
├── RELEASE_NOTES.md
├── CONTRIBUTING.md
├── FAQ.md
├── TROUBLESHOOTING.md
└── SCREENSHOTS.md
```

---

# 📜 logs/

Stores application logs.

## Includes

- Application Logs
- Error Logs
- Provider Logs
- Voice Logs
- RAG Logs

Example

```text
logs/
│
├── app.log
├── error.log
├── provider.log
└── rag.log
```

---

# 🧠 models/

Contains business models.

## Examples

- User
- Conversation
- Quiz
- Flashcard
- Voice Session
- Analytics
- Learning Progress

Example

```text
models/
│
├── user.py
├── conversation.py
├── quiz.py
├── analytics.py
└── voice_session.py
```

---

# 📄 pages/

Contains all Streamlit pages.

## Core Pages

| Page | Purpose |
|------|----------|
| Dashboard | Home page |
| AI Tutor | Chat interface |
| Enterprise RAG | Document retrieval |
| Voice AI Tutor | Voice conversations |
| AI Mentor | Career guidance |
| Interview Preparation | Mock interviews |
| Quiz Generator | Quiz creation |
| Notes Generator | AI notes |
| Flashcards | Learning cards |
| PDF Tutor | PDF learning |
| Coding Tutor | Programming help |
| Revision Planner | Revision schedule |
| Learning Analytics | Statistics |
| Learning History | Session history |
| Settings | Configuration |
| About | Application information |

---

# 💬 prompts/

Contains all AI prompt templates.

## Responsibilities

- System Prompts
- User Prompts
- RAG Prompts
- Interview Prompts
- Quiz Prompts
- Voice Prompts

Example

```text
prompts/
│
├── tutor_prompt.py
├── rag_prompt.py
├── mentor_prompt.py
├── interview_prompt.py
└── quiz_prompt.py
```

---

# ⚙ services/

The heart of the application.

Contains all business logic.

## Core Services

### AI Services

- Provider Service
- Model Service
- Prompt Service
- Conversation Service

---

### RAG Services

- Embedding Service
- Search Service
- Retrieval Service
- Vector Service
- Citation Service

---

### Voice Services

- Speech To Text
- Text To Speech
- Voice Chat
- Voice History
- Voice Analytics
- Voice Session

---

### Learning Services

- Quiz Service
- Notes Service
- Flashcard Service
- Study Planner
- Revision Planner

---

### Analytics Services

- Dashboard Service
- Statistics Service
- Report Service

---

### Utility Services

- Cache Service
- Memory Service
- Logging Service
- File Service

---

# 🎨 ui/

Contains reusable UI components.

Examples

- Sidebar
- Header
- Footer
- Cards
- Buttons
- Tables
- Charts
- Theme Manager

---

# 📂 uploads/

Stores uploaded files.

Supports

- PDF
- DOCX
- TXT
- CSV
- Images
- Audio Files

---

# 🔧 utils/

Contains reusable helper functions.

Examples

- File Utilities
- Date Utilities
- Validation
- Formatters
- Export Utilities
- Common Helpers

---

# 🔍 vector_store/

Stores vector embeddings used by Enterprise RAG.

## Responsibilities

- FAISS Index
- Vector Database
- Embedding Storage
- Search Indexes
- Metadata

---

# 🎨 static/

Contains static resources.

Examples

- CSS
- JavaScript
- Icons
- Fonts

---

# 🖼 assets/

Contains project assets.

Examples

- Logo
- Banner
- Images
- Documentation Graphics

---

# ✅ tests/

Contains automated test cases.

## Test Categories

- Unit Tests
- Integration Tests
- Service Tests
- Provider Tests
- Database Tests
- UI Tests

Example

```text
tests/
│
├── test_provider.py
├── test_database.py
├── test_rag.py
├── test_voice.py
└── test_quiz.py
```

---

# 📊 Module Relationships

```text
                 Streamlit UI
                       │
          ┌────────────┼────────────┐
          │            │            │
       Pages        Components    Assets
          │
          ▼
      Business Services
          │
   ┌──────┼──────────────┐
   │      │              │
Providers  RAG        Voice AI
   │       │              │
   └───────┼──────────────┘
           ▼
      Database + FAISS
```

---

# 📈 Architecture Principles

✅ Modular Design

✅ Separation of Concerns

✅ Reusable Components

✅ Scalable Services

✅ Enterprise Architecture

✅ Provider Abstraction

✅ Service-Oriented Design

✅ Clean Folder Structure

---

# 🌟 Benefits

- Easy Maintenance
- High Scalability
- Modular Development
- Reusable Components
- Enterprise Standards
- Faster Development
- Better Testing
- Cleaner Codebase

---

# 📊 Structure Summary

| Category | Count |
|-----------|------:|
| Main Folders | 15+ |
| Documentation Files | 18 |
| Streamlit Pages | 17+ |
| Core Services | 50+ |
| AI Providers | 3 |
| Vector Store | FAISS |
| Database | MySQL |

