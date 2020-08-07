import cv2
import time
import pandas
from datetime import datetime

first_frame = None
status_list = [None, None]
times = []
video = cv2.VideoCapture(0)
#Pandas DataFrame
df = pandas.DataFrame(columns=['Start','End'])

while True:
    check, frames = video.read()

    status = 0          #Initial no motion detected
    #To convert to gray
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    #To convert to Gaussian Blur 
    gray = cv2.GaussianBlur(gray,(21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    #Find difference between initial and present
    delta_frame = cv2.absdiff(first_frame, gray)
    #Set the Threshold
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)

    cnts,_ = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) > 10000:
            continue
        status = 1

        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frames, (x,y), (x+w,y+h), (0,225,0), 5)

    status_list.append(status)
    status_list = status_list[-2:]

    #Detected Start time
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow('Frames',frames)
    cv2.imshow('Gray',gray)
    cv2.imshow('Difference',delta_frame)
    cv2.imshow('threshold',thresh_delta)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

#for i in range(0,len(times),2):
    #df = df.append({'Start':times[i], 'End':times[i+1]}, ignore_index = True)

for i in range(0, len(times), 2): 
    df = df.append({"Start":times[i], "End":times[i + 1]}, ignore_index = True) 
  

df.to_csv('times.csv')

video.release()
cv2.destroyAllWindows()