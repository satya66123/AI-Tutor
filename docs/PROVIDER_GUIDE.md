<div align="center">

# 🤖 AI Provider Guide

### Enterprise AI Tutor

![Version](https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge)
![Providers](https://img.shields.io/badge/AI-Providers-success?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-412991?style=for-the-badge&logo=openai)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-D97706?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

</div>

---

# 📖 Overview

Enterprise AI Tutor supports multiple AI providers through a unified provider interface. This allows users to switch between providers without changing the application workflow.

---

# 🎯 Supported Providers

| Provider | Type | Status |
|----------|------|--------|
| Ollama | Local LLM | ✅ |
| OpenAI | Cloud AI | ✅ |
| Anthropic | Cloud AI | ✅ |

---

# 🏗️ Provider Architecture

```text
Application

↓

Provider Manager

↓

Provider Factory

↓

Base Provider

↓

Ollama
OpenAI
Anthropic
```

---

# 📂 Provider Components

```text
providers/

├── base_provider.py
├── ollama_provider.py
├── openai_provider.py
├── anthropic_provider.py
├── provider_factory.py
└── provider_manager.py
```

---

# ⚙️ Base Provider

The Base Provider defines a common interface for all AI providers.

### Responsibilities

- Generate Response
- List Models
- Validate Configuration
- Handle Errors
- Standardize Responses

---

# 🦙 Ollama Provider

Ollama enables local AI inference.

## Features

- Local execution
- Offline support
- Privacy focused
- Multiple local models
- Fast inference

### Example Models

- qwen2.5:1.5b
- gemma2:2b
- llama3
- llama3.1
- mistral
- phi3

---

# 🧠 OpenAI Provider

OpenAI provides cloud-based GPT models.

## Features

- GPT Models
- Advanced reasoning
- Large context support
- Reliable API

---

# 🤖 Anthropic Provider

Anthropic provides Claude models.

## Features

- Claude Models
- Long-context conversations
- Enterprise capabilities
- Safe AI responses

---

# 🔄 Provider Selection Flow

```text
User

↓

Select Provider

↓

Provider Manager

↓

Provider Factory

↓

Selected Provider

↓

Generate Response
```

---

# ⚙️ Provider Configuration

Configure providers using environment variables.

### Example

```env
OPENAI_API_KEY=your_key

ANTHROPIC_API_KEY=your_key

OLLAMA_HOST=http://localhost:11434
```

---

# 📊 Provider Comparison

| Feature | Ollama | OpenAI | Anthropic |
|----------|:------:|:------:|:---------:|
| Local Models | ✅ | ❌ | ❌ |
| Internet Required | ❌ | ✅ | ✅ |
| Offline Usage | ✅ | ❌ | ❌ |
| Privacy | High | Medium | Medium |
| Easy Setup | ✅ | ✅ | ✅ |

---

# 🚀 Advantages

- Unified Interface
- Easy Provider Switching
- Extensible Design
- Multiple Model Support
- Enterprise Architecture

---

# 🔒 Security

- API Key Protection
- Environment Variables
- Provider Validation
- Exception Handling

---

# 📊 Summary

| Category | Details |
|-----------|---------|
| Providers | 3 |
| Architecture | Provider Pattern |
| Local AI | Ollama |
| Cloud AI | OpenAI, Anthropic |
| Configuration | Environment Variables |
