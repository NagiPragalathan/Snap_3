import cv2
import pyttsx3
import speech_recognition as sr
from deepface import DeepFace
import threading

# Initialize the OpenCV camera
camera = cv2.VideoCapture(0)

# Set the camera resolution and image quality
width, height = 640, 480
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
r = sr.Recognizer()

# Use the microphone as the source of audio
with sr.Microphone() as source:
    # Define a function to recognize speech
    def recognize_speech():
        while True:
            print("Say something!")
            audio = r.listen(source)

            # Recognize speech using Google Speech Recognition
            try:
                print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
                engine.say(f"I recognize that you said {r.recognize_google(audio)}")
                engine.runAndWait()
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Define a function to analyze emotions in the captured frame
    def analyze_emotions():
        while True:
            # Capture an image from the camera
            ret, frame = camera.read()

            # Analyze the emotion in the captured frame
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

            # Get the dominant emotion from the result
            emotions = result[0].get('emotion')

            # Display the emotions on the screen
            for idx, (emotion, score) in enumerate(emotions.items()):
                text = f"{emotion}: {score:.2f}"
                cv2.putText(frame, text, (10, 30+idx*30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            # Display the captured frame
            cv2.imshow("Capture", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Create two threads to simultaneously recognize speech and analyze emotions
    speech_thread = threading.Thread(target=recognize_speech)
    emotion_thread = threading.Thread(target=analyze_emotions)

    # Start the threads
    speech_thread.start()
    emotion_thread.start()

    # Wait for the threads to finish
    speech_thread.join()
    emotion_thread.join()

# Release the camera
camera.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
