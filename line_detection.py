import cv2
import numpy as np

org_img = cv2.imread('images/line1.jpg')
img = cv2.resize(org_img,(1080,650))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150, apertureSize =3)
#Returns the r and theta
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

#To print the lines in list
#print(lines)

if lines is not None:
    for i in range(len(lines)):
        for r, theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)

            x0 = a*r
            y0 = b*r

            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2)

    cv2.imshow('adsf', img)
    cv2.waitKey(0)    
else:
    print('could not find any line')
#To create a image in that directory
#cv2.imwrite('Image.jpg',img)
cv2.destroyAllWindows()