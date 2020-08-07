import cv2
import time

video = cv2.VideoCapture(0)             #1 for external camera 2 and 3 if many cameras
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')     #xlm file
a = 1

while True:
    a += 1
    check, frame = video.read()
    print(frame)

    #To Convert image to gray
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('capturing',frame)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3)

    for x,y,w,h in faces:
        img = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 5)

    cv2.imshow('face',img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#Total number of Frames
print(a)            
video.release()
cv2.destroyAllWindows()