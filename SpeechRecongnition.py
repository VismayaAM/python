import speech_recognition as sr
AUDIO_FILE=("Vismaya1.wav")
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio =r.record(source)
try:
    print("audio file contains"+r.recognize_google(audio))
    print()
except sr.UnknownValueError:
    print("Google speech recognition couldnot understand audio")
except sr.RequestError:
    print("couldn't get the result form google speech recognition")
    