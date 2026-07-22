import speech_recognition as sr

print(sr.__version__)

r = sr.Recognizer()

print(type(r))
print(hasattr(r, "recognize_google"))
print(dir(r))