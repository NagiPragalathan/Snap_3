import cv2
import os

# Set the image file name and the video file name
image_file = 'C:/Users/nagip/OneDrive/Desktop/CensorShield/snap_dead/download.jpg'
video_file = 'my_video.mp4'

# Read the image using OpenCV
img = cv2.imread(image_file)

# Get the dimensions of the image
height, width, channels = img.shape

# Define the codec for the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Define the video writer object
out = cv2.VideoWriter(video_file, fourcc, 10, (width, height))

# Define the number of frames to generate
num_frames = 100

# Generate the frames
for i in range(num_frames):
    # Generate a random angle for rotation
    angle = (i/num_frames)*360

    # Rotate the image by the angle
    M = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_img = cv2.warpAffine(img, M, (width, height))

    # Write the rotated image to the video writer object
    out.write(rotated_img)

    # Display the rotated image
    cv2.imshow('image', rotated_img)
    cv2.waitKey(10)

# Release the video writer object and destroy the display window
out.release()
cv2.destroyAllWindows()
