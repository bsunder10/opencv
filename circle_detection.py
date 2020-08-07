import cv2
import numpy as np

img = cv2.imread('images/circle.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (3,3))

#Circle Detection
detected_circle = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50,param2= 30, minRadius=1, maxRadius=40)

if detected_circle is not None:
    detected_circle = np.uint16(np.around(detected_circle))
    for pt in detected_circle[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        cv2.circle(img, (a,b), r, (0,255,0), 3)

        #For Center of circle
        cv2.circle(img, (a,b), 1,(255,0,1), 3)

    cv2.imshow('show', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()