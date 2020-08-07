import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/polygon1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
cornor = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
cornor = np.int0(cornor)

for i in cornor:
    x, y = i.ravel()
    cv2.circle(img, (x,y), 1, (0,255,0), 2)

plt.imshow(img), plt.show()
'''

#For Harris Corner
gray = np.float32(gray)
dest = cv2.cornerHarris(gray, 2, 5, 0.07)
dest = cv2.dilate(dest, None)

img[dest>0.01 * dest.max()] = [0,0,255]
cv2.imshow('Image', gray)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()