import cv2
import numpy as np
from matplotlib import pyplot as plt

org_img = cv2.imread('images/b&w1.jpg', 0)
img = cv2.resize(org_img, (1080, 720))

#   Histogram Equalizations
#   Note: For histogram equalization open the image in black and white
#           append 0 to the cv2.imread Function
#equ = cv2.equalizeHist(img)
#image = np.hstack((img, equ))

#   Plotting the Histogram 
#hist = cv2.calcHist([img], [0], None, [256], [0, 256])
#plt.plot(hist)
#plt.show()

#   Alternate way for plotting the Histogram
#plt.hist(img.ravel(), 256, [0,256])
#plt.show()

#Thresholding
#   Sample Thresholding
#ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
#ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
#ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
#ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
#ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
'''
cv2.imshow('Original Image',img)
cv2.imshow('OriSADginal Image',thresh1)
cv2.imshow('OriginWEal Image',thresh2)
cv2.imshow('Original3 Image',thresh3)
cv2.imshow('Original zImage',thresh4)
cv2.imshow('Original SDFImage',thresh5)
'''
#   Adaptive Thresholding
#image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
#   Alternative Methord
#image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 10)
#   OTSU  Thresholding
#ret, image = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Image Pyramiding
'''
layer = img.copy()
for i in range(3):          #3 is the number of pyramids Must be Between 1 and 4
    plt.subplot(2, 2, i+1)
    layer = cv2.pyrDown(layer)
    cv2.imshow('{}'.format(i),layer)
'''
#   Background Subtraction
fgbg = cv2.createBackgroundSubtractorMOG2()

image = fgbg.apply(img)

cv2.imshow('Original Image', img)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()