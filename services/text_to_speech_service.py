"""
Enterprise Text To Speech Service
"""

import os
import tempfile
import time

import pyttsx3


class TextToSpeechService:

    _engine = None

    # =====================================================
    # Engine
    # =====================================================

    @classmethod
    def get_engine(cls):

        if cls._engine is None:

            cls._engine = pyttsx3.init()

            cls._engine.setProperty("rate", 180)

            cls._engine.setProperty("volume", 1.0)

        return cls._engine

    # =====================================================
    # Speak
    # =====================================================

    @classmethod
    def speak(

            cls,

            text,

            rate=180,

            volume=1.0,

            voice_index=0

    ):

        start = time.time()

        try:

            engine = cls.get_engine()

            voices = engine.getProperty("voices")

            if voices:

                voice_index = min(

                    voice_index,

                    len(voices) - 1

                )

                engine.setProperty(

                    "voice",

                    voices[voice_index].id

                )

            engine.setProperty(

                "rate",

                rate

            )

            engine.setProperty(

                "volume",

                volume

            )

            engine.say(text)

            engine.runAndWait()

            return {

                "success": True,

                "response_time": round(

                    time.time() - start,

                    2

                )

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }

    # =====================================================
    # Save Audio
    # =====================================================

    @classmethod
    def save_audio(

            cls,

            text,

            filename=None,

            rate=180,

            volume=1.0,

            voice_index=0

    ):

        engine = cls.get_engine()

        voices = engine.getProperty("voices")

        if voices:

            voice_index = min(

                voice_index,

                len(voices) - 1

            )

            engine.setProperty(

                "voice",

                voices[voice_index].id

            )

        engine.setProperty(

            "rate",

            rate

        )

        engine.setProperty(

            "volume",

            volume

        )

        if filename is None:

            temp = tempfile.NamedTemporaryFile(

                suffix=".mp3",

                delete=False

            )

            filename = temp.name

            temp.close()

        engine.save_to_file(

            text,

            filename

        )

        engine.runAndWait()

        return filename

    # =====================================================
    # Voices
    # =====================================================

    @classmethod
    def get_voices(cls):

        engine = cls.get_engine()

        voices = engine.getProperty("voices")

        result = []

        for index, voice in enumerate(voices):

            result.append(

                {

                    "index": index,

                    "id": voice.id,

                    "name": voice.name

                }

            )

        return result

    # =====================================================
    # Delete Audio
    # =====================================================

    @staticmethod
    def delete_audio(path):

        if os.path.exists(path):

            os.remove(path)

    # =====================================================
    # Validate
    # =====================================================

    @staticmethod
    def validate(text):

        return bool(text and text.strip())