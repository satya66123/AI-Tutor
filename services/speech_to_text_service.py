"""
Enterprise Speech To Text Service
Supports:
- Faster Whisper
- Audio File Validation
- Language Detection
"""

import os
import time
from faster_whisper import WhisperModel


class SpeechToTextService:

    _model = None

    # =====================================================
    # Load Whisper Model
    # =====================================================

    @classmethod
    def get_model(cls):

        if cls._model is None:

            cls._model = WhisperModel(

                "base",

                device="cpu",

                compute_type="int8"

            )

        return cls._model

    # =====================================================
    # Validate Audio
    # =====================================================

    @staticmethod
    def validate_audio(audio_path):

        if not os.path.exists(audio_path):

            return False

        if os.path.getsize(audio_path) == 0:

            return False

        return True

    # =====================================================
    # Speech → Text
    # =====================================================

    @classmethod
    def transcribe(cls, audio_path):

        if not cls.validate_audio(audio_path):

            return {

                "success": False,

                "text": "",

                "language": "",

                "error": "Invalid audio file."

            }

        start = time.time()

        try:

            model = cls.get_model()

            segments, info = model.transcribe(

                audio_path,

                beam_size=5

            )

            text = ""

            for segment in segments:

                text += segment.text + " "

            return {

                "success": True,

                "text": text.strip(),

                "language": info.language,

                "duration": round(

                    time.time() - start,

                    2

                )

            }

        except Exception as e:

            return {

                "success": False,

                "text": "",

                "language": "",

                "error": str(e)

            }

    # =====================================================
    # Supported Formats
    # =====================================================

    @staticmethod
    def supported_formats():

        return [

            ".wav",

            ".mp3",

            ".m4a",

            ".ogg",

            ".flac"

        ]