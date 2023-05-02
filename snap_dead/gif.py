from cv2 import cv2
import cvzone
import imageio

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the GIF file
gif = imageio.mimread('hello.gif')

while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)

    for (x, y, w, h) in faces:
        # Resize the GIF to match the size of the detected face
        gif_frame = cv2.resize(gif[0], (w, h))

        # Create an alpha channel for the GIF frame
        alpha = gif_frame[:, :, 3] / 255.0

        # Remove the alpha channel from the GIF frame
        gif_frame = gif_frame[:, :, :3]

        # Overlay the GIF frame on the video frame
        overlay = cv2.addWeighted(frame[y:y+h, x:x+w, :], 1-alpha, gif_frame, alpha, 0)
        frame[y:y+h, x:x+w, :] = overlay

    cv2.imshow('Snap Dude', frame)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
