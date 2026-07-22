<div align="center">

# 🎤 Voice AI Tutor

### Enterprise AI Tutor

![Version](https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge)
![Voice AI](https://img.shields.io/badge/Voice-AI-success?style=for-the-badge)
![Whisper](https://img.shields.io/badge/Faster-Whisper-orange?style=for-the-badge)
![gTTS](https://img.shields.io/badge/gTTS-Text_To_Speech-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

</div>

---

# 📖 Overview

The Voice AI Tutor enables users to interact with the AI using natural speech. It converts spoken input into text, processes the request using the selected AI provider, and returns both text and synthesized speech.

---

# 🎯 Features

- 🎤 Speech-to-Text
- 🔊 Text-to-Speech
- 💬 Voice Conversations
- 📚 Enterprise RAG Support
- 🤖 Multiple AI Providers
- 📊 Voice Analytics
- 📝 Voice History
- 🗂 Session Management

---

# 🏗️ Architecture

```text
User Speech
      │
      ▼
Speech-to-Text
      │
      ▼
AI Tutor / RAG
      │
      ▼
AI Response
      │
      ▼
Text-to-Speech
      │
      ▼
Audio Output
```

---

# ⚙️ Workflow

```text
Record Voice

↓

Speech-to-Text

↓

Generate AI Response

↓

Convert to Speech

↓

Play Audio
```

---

# 📂 Main Components

| Component | Purpose |
|-----------|---------|
| SpeechToTextService | Converts speech into text |
| TextToSpeechService | Converts text into speech |
| VoiceChatService | Manages conversations |
| VoiceSessionService | Handles voice sessions |
| VoiceHistoryService | Stores conversation history |
| VoiceAnalyticsService | Tracks voice usage |

---

# 🎤 Speech-to-Text

Converts spoken audio into text using Faster Whisper.

### Features

- Fast transcription
- High accuracy
- Local processing
- Multi-language support

---

# 🔊 Text-to-Speech

Converts AI-generated text into audio.

### Features

- Natural voice output
- Fast audio generation
- Easy playback

---

# 💬 Voice Chat

Supports complete voice conversations.

### Features

- Ask questions by voice
- Receive spoken responses
- Context-aware conversations
- Multi-turn interactions

---

# 📚 Enterprise RAG Integration

Voice AI works seamlessly with Enterprise RAG.

```text
Voice Question

↓

Speech-to-Text

↓

Enterprise RAG

↓

Relevant Documents

↓

AI Response

↓

Text-to-Speech
```

---

# 🤖 AI Providers

Supported providers:

- Ollama
- OpenAI
- Anthropic

---

# 📊 Voice Analytics

Tracks:

- Total Sessions
- Voice Requests
- Response Time
- Conversation Duration
- Daily Usage

---

# 📝 Voice History

Stores:

- User Questions
- AI Responses
- Session Time
- Selected Provider
- Selected Model

---

# 🔒 Security

- Local audio processing (where applicable)
- Secure API communication
- Session management
- Error handling

---

# 🚀 Advantages

- Hands-free learning
- Faster interaction
- Natural conversations
- Accessibility support
- Improved user experience

---

# 📊 Summary

| Feature | Status |
|----------|--------|
| Speech-to-Text | ✅ |
| Text-to-Speech | ✅ |
| Voice Chat | ✅ |
| Voice History | ✅ |
| Voice Analytics | ✅ |
| Enterprise RAG | ✅ |

