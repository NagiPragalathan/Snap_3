import cv2
import os
import numpy as np
# Path to the training dataset
dataset_path = 'dataset'

# Load the face recognition model
face_model = cv2.face.LBPHFaceRecognizer_create()

# Function to extract the training data and labels
def get_training_data(dataset_path):
    training_data = []
    labels = []
    for name in os.listdir(dataset_path):
        if not os.path.isdir(os.path.join(dataset_path, name)):
            continue
        for img_name in os.listdir(os.path.join(dataset_path, name)):
            img_path = os.path.join(dataset_path, name, img_name)
            img = cv2.imread(img_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            training_data.append(gray)
            labels.append(int(name))
    return training_data, labels

# Train the face recognition model
def train_face_recognition():
    training_data, labels = get_training_data(dataset_path)
    face_model.train(training_data, np.array(labels))

# Detect the face and return the corresponding name
def recognize_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('C:/Users/nagip/OneDrive/Desktop/CensorShield/snap_dead/haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (100, 100))
        label, confidence = face_model.predict(roi_gray)
        if confidence < 100:
            return str(label)
    return None

# Train the face recognition model
train_face_recognition()

# Load the video
cap = cv2.VideoCapture('video.mp4')

# Loop through the video frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    name = recognize_face(frame)
    if name:
        cv2.putText(frame, name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
