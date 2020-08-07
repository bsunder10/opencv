import cv2

#Original Images
org_img1 = cv2.imread('images/csk1.jpg')
org_img2 = cv2.imread('images/msd1.jpg')
#Resized Images
img1 = cv2.resize(org_img1, (800,800))
img2 = cv2.resize(org_img2, (800,800))

#Adding the Images
#image = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
#Subtracting the Images
#image = cv2.subtract(img1, img2)
#Bitwise AND
#image = cv2.bitwise_and(img1, img2)
#Bitwise OR
#image = cv2.bitwise_or(img1, img2)
#Bitwise XOR
#image = cv2.bitwise_xor(img1, img2)
#Bitwise NOT
image = cv2.bitwise_not(img1)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()