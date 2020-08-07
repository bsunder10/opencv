import cv2
import numpy as np

org_img = cv2.imread('images/b&w1.jpg')
img = cv2.resize(org_img, (1080,720))

#Note: All the Numbers used in it shoud be odd Numbers 
#       Should not use Even numbers

#Erode
#kernal =np.ones((5,5), np.uint8) 
#image = cv2.erode(img, kernal)

#Blur
#   Gaussian Blur
#image = cv2.GaussianBlur(img ,(9,9,), 0) #Numbers should be odd
#   Median Blur
#image = cv2.medianBlur(img,5)   
#   Bilateral Blur
#image = cv2.bilateralFilter(img, 9, 25, 75)

#Border
#image = cv2.copyMakeBorder(img, 5,5,6,4,cv2.BORDER_CONSTANT)
#   Border with Reflect
#image = cv2.copyMakeBorder(img, 15,15,15,15, cv2.BORDER_REFLECT)

#Scaling
#   GrayScaling Image
#image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#   Resizeing Image
#image = cv2.resize(img, (500,500))
#   Rotate
#(rows, cols) = img.shape[:2]
#m = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
#image = cv2.warpAffine(img, m, (cols, rows))
#   Transform for [50, 100]
#(rows, cols) = img.shape[:2]
#m = np.float32([[1,0,50], [0,1,100]])
#image = cv2.warpAffine(img, m, (rows, cols))
#   Edging
#image = cv2.Canny(img, 100, 200)

#Errosion and Dilation
kernal = np.ones((5,5), np.uint8)
img_erosion = cv2.erode(img, kernal, iterations=1)
img_dilation = cv2.dilate(img, kernal, iterations=1)
cv2.imshow('Image',img_erosion)
cv2.imshow('Original', img_dilation)

#cv2.imshow('Image',image)
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()