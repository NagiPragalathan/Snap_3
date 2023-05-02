import cv2
import  cvzone

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('C:/Users/nagip/OneDrive/Desktop/CensorShield/snap_dead/haarcascade_frontalface_default.xml')
overlay = cv2.imread('C:/Users/nagip/OneDrive/Desktop/CensorShield/snap_dead/cool.png', cv2.IMREAD_UNCHANGED)

while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)

    for (x, y, w, h) in faces:
        overlay_resize = cv2.resize(overlay, dsize=(int(w*1.5), int(h*1.5)))
        try:
            frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
        except:
            print("Filter error")

    cv2.imshow('Snap Dude', frame)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
