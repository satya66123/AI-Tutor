<div align="center">

# 🗄️ Database Documentation

### Enterprise AI Tutor

![Version](https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge)
![Database](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

</div>

---

# 📖 Overview

Enterprise AI Tutor uses **MySQL** as the primary relational database to store user information, learning history, AI conversations, voice sessions, analytics, and application settings.

---

# 🏗️ Database Architecture

```text
Application

↓

Database Service

↓

MySQL Database

↓

Tables
```

---

# 📂 Main Tables

| Table | Purpose |
|--------|----------|
| users | User information |
| conversations | AI chat history |
| voice_sessions | Voice conversations |
| quizzes | Quiz records |
| flashcards | Flashcard data |
| notes | AI generated notes |
| study_plans | Study schedules |
| analytics | Learning statistics |
| settings | User preferences |

---

# 👤 Users Table

Stores registered user information.

Example Fields

- id
- username
- email
- password
- created_at

---

# 💬 Conversations Table

Stores AI chat history.

Example Fields

- id
- user_id
- question
- answer
- provider
- model
- timestamp

---

# 🎤 Voice Sessions Table

Stores voice learning sessions.

Example Fields

- id
- user_id
- transcript
- response
- duration
- created_at

---

# 📝 Quiz Table

Stores generated quizzes.

Example Fields

- id
- topic
- difficulty
- score
- created_at

---

# 📒 Notes Table

Stores AI-generated notes.

Example Fields

- id
- title
- content
- created_at

---

# 📅 Study Plans Table

Stores study schedules.

Example Fields

- id
- subject
- schedule
- progress

---

# 📊 Analytics Table

Stores learning analytics.

Example Fields

- id
- study_time
- quizzes_completed
- ai_usage
- voice_usage

---

# ⚙️ Settings Table

Stores user preferences.

Example Fields

- Theme
- Preferred AI Provider
- Default Model
- Language

---

# 🔄 Database Flow

```text
User

↓

Application

↓

Database Service

↓

MySQL

↓

Data Returned
```

---

# 🔒 Security

- Environment Variables
- Parameterized Queries
- Input Validation
- Secure Connections
- Error Handling

---

# 📊 Summary

| Database | MySQL |
|-----------|--------|
| Tables | 8+ |
| ORM | SQLAlchemy (Optional) |
| Purpose | Application Data Storage |

