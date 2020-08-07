import cv2
import numpy as np

img = cv2.imread('images/polygon1.jpg')
edge = cv2.Canny(img, 50, 150, 3)

cv2.imshow('Edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()