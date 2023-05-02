import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Use the microphone as the source of audio
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Recognize speech using Google Speech Recognition
try:
    print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
