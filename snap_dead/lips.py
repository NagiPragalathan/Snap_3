import cv2
import dlib
import numpy as np

# Load the face detector from dlib
detector = dlib.get_frontal_face_detector()

# Load the landmark predictor from dlib
predictor = dlib.shape_predictor('C:/Users/nagip/OneDrive/Desktop/CensorShield/snap_dead/shape_predictor_68_face_landmarks.dat')

# Load the input image
image = cv2.imread('C:/Users/nagip/OneDrive/Desktop/CensorShield/snap_dead/download.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect the faces in the grayscale image
faces = detector(gray)

# Get the facial landmarks for the detected faces
for face in faces:
    landmarks = predictor(gray, face)

    # Get the coordinates of the lips
    lips = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(48, 68)])

    # Draw the lips on the image
    cv2.polylines(image, [lips], True, (0, 0, 255), 2)

# Display the image with the lips detected
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
