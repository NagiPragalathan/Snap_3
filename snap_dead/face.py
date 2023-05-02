import face_recognition
import os

# Define a function to load the images and encodings of all the faces in a directory
def load_faces(directory):
    # Initialize empty lists for the images and encodings
    images = []
    encodings = []
    
    # Loop through all the files in the directory
    for filename in os.listdir(directory):
        # Load the image using face_recognition
        image = face_recognition.load_image_file(os.path.join(directory, filename))
        
        # Get the face encoding using face_recognition
        encoding = face_recognition.face_encodings(image)[0]
        
        # Append the image and encoding to the lists
        images.append(image)
        encodings.append(encoding)
        
    # Return the images and encodings
    return images, encodings

# Define a function to recognize faces in an image using a list of known encodings
def recognize_faces(image, known_encodings):
    # Get the face encodings from the image using face_recognition
    face_encodings = face_recognition.face_encodings(image)
    
    # Initialize an empty list to store the recognized names
    recognized_names = []
    
    # Loop through all the face encodings in the image
    for face_encoding in face_encodings:
        # Compare the face encoding to the known encodings using face_recognition
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        
        # Get the indices of the matching encodings
        indices = [i for i, x in enumerate(matches) if x]
        
        # Initialize a variable to store the recognized name
        recognized_name = "Unknown"
        
        # If there is a match, get the name from the filename
        if indices:
            index = indices[0]
            filename = os.listdir("known_faces")[index]
            recognized_name = os.path.splitext(filename)[0]
        
        # Append the recognized name to the list
        recognized_names.append(recognized_name)
    
    # Return the recognized names
    return recognized_names

# Load the known faces
known_faces_directory = "known_faces"
known_faces_images, known_faces_encodings = load_faces(known_faces_directory)

# Load an image to recognize faces in
image = face_recognition.load_image_file("C:/Users/nagip/OneDrive/Desktop/CensorShield/snap_dead/download.jpg")

# Recognize the faces in the image
recognized_names = recognize_faces(image, known_faces_encodings)

# Print the recognized names
print(recognized_names)
