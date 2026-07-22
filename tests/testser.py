from services.speech_to_text_service import SpeechToTextService

result = SpeechToTextService.transcribe("sample.wav")

print(result)