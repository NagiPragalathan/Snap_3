import cv2
from deepface import DeepFace

# Initialize the OpenCV camera
camera = cv2.VideoCapture(0)

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

# Release the camera
camera.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
