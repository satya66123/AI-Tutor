"""
Enterprise Voice Chat Service
"""

import time

from pages.rag.rag_service import RAGService

from services.speech_to_text_service import SpeechToTextService
from services.text_to_speech_service import TextToSpeechService
import tempfile
import os

from services.voice_session_service import VoiceSessionService
from services.voice_history_service import VoiceHistoryService
from services.voice_analytics_service import VoiceAnalyticsService

from models.voice_models import VoiceAnalytics


class VoiceChatService:
    """
    Enterprise Voice Chat Service
    """

    @staticmethod
    def chat(
            audio_file,
            provider,
            model,
            search_type,
            top_k,
            language="en",
            speak_response=True
    ):

        # ---------------------------------------------
        # Create Voice Session
        # ---------------------------------------------

        session_id = VoiceSessionService.create_session(

            provider=provider,

            model=model,

            language=language

        )

        session_start = time.time()

        try:

            # Save UploadedFile to temporary file
            suffix = os.path.splitext(audio_file.name)[1]

            with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
            ) as tmp:

                tmp.write(audio_file.getbuffer())

                audio_path = tmp.name

            try:

                stt_result = SpeechToTextService.transcribe(audio_path)

            finally:

                if os.path.exists(audio_path):
                    os.remove(audio_path)

            # ---------------------------------------------
            # Speech To Text
            # ---------------------------------------------

            if not stt_result["success"]:
                VoiceSessionService.update_status(
                    session_id,
                    "FAILED"
                )

                return {
                    "success": False,
                    "message": stt_result["error"],
                    "session_id": session_id
                }

            transcript = stt_result["text"]

            if not transcript.strip():
                VoiceSessionService.update_status(
                    session_id,
                    "FAILED"
                )

                return {
                    "success": False,
                    "message": "Unable to recognize speech.",
                    "session_id": session_id
                }

            # ---------------------------------------------
            # Ask Enterprise RAG
            # ---------------------------------------------

            result = RAGService.ask(

                question=transcript,

                model=model,

                search_type=search_type,

                top_k=top_k

            )

            answer = result["answer"]

            # ---------------------------------------------
            # Text To Speech
            # ---------------------------------------------

            audio_response = None

            if speak_response:

                audio_response = TextToSpeechService.save_audio(

                    answer

                )

            # ---------------------------------------------
            # Save History
            # ---------------------------------------------

            VoiceHistoryService.save(

                session_id=session_id,

                transcript=transcript,

                ai_response=answer,

                provider=provider,

                model=model,

                language=language

            )

            # ---------------------------------------------
            # Update Session
            # ---------------------------------------------

            VoiceSessionService.increment_messages(

                session_id

            )

            duration = round(

                time.time() - session_start,

                2

            )

            VoiceSessionService.update_duration(

                session_id,

                duration

            )

            VoiceSessionService.complete_session(

                session_id

            )

            # ---------------------------------------------
            # Save Analytics
            # ---------------------------------------------

            analytics = VoiceAnalytics(

                session_id=session_id,

                total_duration=duration,

                speaking_duration=duration,

                ai_duration=result["response_time"],

                total_messages=1,

                average_response_time=result["response_time"],

                provider=provider,

                model=model

            )

            VoiceAnalyticsService.save(

                analytics

            )

            # ---------------------------------------------
            # Return Result
            # ---------------------------------------------

            return {

                "success": True,

                "session_id": session_id,

                "question": transcript,

                "answer": answer,

                "audio_file": audio_response,

                "sources": result["sources"],

                "parents": result["parents"],

                "citations": result["citations"],

                "token_usage": result["token_usage"],

                "response_time": result["response_time"],

                "search_type": result["search_type"]

            }

        except Exception as e:

            VoiceSessionService.update_status(

                session_id,

                "FAILED"

            )

            return {

                "success": False,

                "session_id": session_id,

                "message": str(e)

            }

    @classmethod
    def end_session(cls, voice_session_id):
        pass