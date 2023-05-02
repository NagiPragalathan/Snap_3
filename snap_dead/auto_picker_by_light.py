import cv2

# Set the camera resolution and image quality
width, height = 640, 480
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

# Initialize the OpenCV camera
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while True:
    # Capture an image from the camera
    ret, frame = camera.read()
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Compute the variance of the grayscale image
    var = cv2.Laplacian(gray, cv2.CV_64F).var()
    
    # If the image quality is good enough, save it to a file
    if var > 40:
        # Save the image to a file
        file_path = 'file.jpg'
        cv2.imwrite(file_path, frame, encode_param)
        print("Image captured successfully!")
        break
    
    print(var)
    # If the image quality is not good enough, display a message and try again
    cv2.putText(frame, "Please adjust your look", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.imshow("Capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
camera.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
