import cv2

org_img = cv2.imread('csk3.jpg',1)
img = cv2.resize(org_img,(800,800))
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,225,0), thickness=3)

cv2.imshow('csk',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#To print the type of faces and the faces
#print(type(faces))
print(faces)