import cv2

#For Black and white Image
img = cv2.imread('csk1.jpg',0)

#For Color Image
img = cv2.imread('csk1.jpg',1)

#To Double the pixels
#resized_img = cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))

#To half the pixels
#resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

#For fixed
resized_img = cv2.resize(img, (500,600))

cv2.imshow('csk', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#For the size of pixels
#print(img.shape)

#To create a image in that directory
#cv2.imwrite('Image.jpg',img)

#For the pixels of image, Generally in Numpy array
#print(img)