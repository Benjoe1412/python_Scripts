# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:07:56 2020

@author: Benjoe
"""

# Python program to implement 
# Webcam Motion Detector 

# importing OpenCV, time and Pandas library 
import cv2, time, pandas 
import time as timedfor

# importing datetime class from datetime library 
from datetime import datetime 

# Assigning our static_back to None 
static_back = None
contouriterator = 0
# List when any moving object appear 
motion_list = [ None, None ] 
starttime = datetime.now()
# Time of movement 
time = [] 
img_arrayframe = []
sizeofpicture = (640,480)
# Initializing DataFrame, one column is start 
# time and other column is end time 
df = pandas.DataFrame(columns = ["Start", "End"]) 

contourgreencoord = (0,0,0,0)
def saveJpgImage(frame):
    #process image
    timed = timedfor.time()
    img_arrayframe.append(frame)
    height, width, layers = frame.shape
    sizeofpicture = (width,height)
def saveVideo():
    
    datetimestring = datetime.strftime(datetime.now(),"%y%m%d%H%M%S")
    filename = 'video' + datetimestring + '.mp4' 
    out = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*'DIVX'), 30, sizeofpicture)
 
    for i in range(len(img_arrayframe)):
        out.write(img_arrayframe[i])
    out.release()
    img_arrayframe.clear()
# Capturing video 
video = cv2.VideoCapture(0) 

# Infinite while loop to treat stack of image as video 
while True: 
    # Reading frame(image) from video 
    check, frame = video.read() 

    # Initializing motion = 0(no motion) 
    motion = 0

    # Converting color image to gray_scale image 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # Converting gray scale image to GaussianBlur 
    # so that change can be find easily 
    gray = cv2.GaussianBlur(gray, (21, 21), 0) 

    # In first iteration we assign the value 
    # of static_back to our first frame 
    if static_back is None: 
        static_back = gray 
        continue
    
    # Difference between static background 
    # and current frame(which is GaussianBlur) 
    diff_frame = cv2.absdiff(static_back, gray) 

    # If change in between static background and 
    # current frame is greater than 30 it will show white color(255) 
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1] 
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2) 

    # Finding contour of moving object 

    _, cnts,_ = cv2.findContours(thresh_frame.copy(), 
                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    for contour in cnts: 
        if cv2.contourArea(contour) < 10000: 
            continue
        motion = 1
        
        (x, y, w, h) = cv2.boundingRect(contour) 
        # making green rectangle arround the moving object 
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
            
        if contourgreencoord == cv2.boundingRect(contour):
            if contouriterator == 3:
                static_back = gray 
                
                contouriterator = 0
            contouriterator += 1
        else:
            contouriterator = 0
        contourgreencoord = cv2.boundingRect(contour)
    # Appending status of motion 
    motion_list.append(motion) 

    motion_list = motion_list[-2:] 
    if motion == 1:
        print("move")
        saveJpgImage(frame)
        starttime = datetime.now()
        
    # Appending Start time of motion 
    if motion_list[-1] == 1 and motion_list[-2] == 0: 
        time.append(datetime.now()) 
        

    # Appending End time of motion 
    if motion_list[-1] == 0 and motion_list[-2] == 1: 
        time.append(datetime.now()) 
        
    if motion != 1:
        if (datetime.now()-starttime).total_seconds() > 3 and len(img_arrayframe) > 15:
            print("ment")
            saveVideo()
    # Displaying image in gray_scale 
    #cv2.imshow("Gray Frame", gray) 

    # Displaying the difference in currentframe to 
    # the staticframe(very first_frame) 
    cv2.imshow("Difference Frame", diff_frame) 

    # Displaying the black and white image in which if 
    # intensity difference greater than 30 it will appear white 
    cv2.imshow("Threshold Frame", thresh_frame) 

    # Displaying color frame with contour of motion of object 
    cv2.imshow("Color Frame", frame) 

    key = cv2.waitKey(1) 
    # if q entered whole process will stop 
    if key == ord('q'): 
        # if something is movingthen it append the end time of movement 
        if motion == 1: 
            time.append(datetime.now()) 
            
        break

# Appending time of motion in DataFrame 
for i in range(0, len(time), 2): 
    df = df.append({"Start":time[i], "End":time[i + 1]}, ignore_index = True) 

# Creating a CSV file in which time of movements will be saved 
df.to_csv("Time_of_movements.csv") 

video.release() 

# Destroying all the windows 
cv2.destroyAllWindows() 
