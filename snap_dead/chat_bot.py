import cv2
import threading
import time
import pyttsx3
import speech_recognition as sr
from deepface import DeepFace


def detect_emotions():
    # Initialize the OpenCV camera
    camera = cv2.VideoCapture(0)

    while True:
        # Capture an image from the camera
        ret, frame = camera.read()

        # Analyze the emotion in the captured frame
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False, silent=True)

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

    # Release the camera
    camera.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


def recognize_speech():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    while True:
        # Use the microphone as the source of audio
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # Recognize speech using Google Speech Recognition
        try:
            text = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said: " + text)
            engine.say(f"I sense that you're feeling {text}")
            engine.runAndWait()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == '__main__':
    # Create and start the threads
    emotions_thread = threading.Thread(target=detect_emotions)
    speech_thread = threading.Thread(target=recognize_speech)
    emotions_thread.start()
    speech_thread.start()

    # Wait for the threads to finish
    emotions_thread.join()
    speech_thread.join()
