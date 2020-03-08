#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TequilaSunrise.py
#  
#  Copyright 2020 Hyperbolic <danny0_89@hotmail.com>
import cv2
import numpy as np
from datetime import datetime
cv2.namedWindow('Tequila Sunrise')
cam = cv2.VideoCapture(0)
now = datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S")


def nothing(x):
	pass

switch = 'Video'
Photo = 'Photo'
Exit = 'Exit or press "Q"'
cv2.createTrackbar(switch, 'Tequila Sunrise',0,1,nothing)
cv2.createTrackbar(Photo, 'Tequila Sunrise',0,1,nothing)
cv2.createTrackbar(Exit, 'Tequila Sunrise',0,1,nothing)

# We convert the resolutions from float to integer.
frame_width = int(cam.get(3))
frame_height = int(cam.get(4))
video_counter = 0
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('Video'+dt_string+str(video_counter)+'.avi',fourcc,10, (frame_width,frame_height))
s2=0
while (1):
        ret_val, img = cam.read()
        cv2.imshow('Tequila Sunrise', img)
        s = cv2.getTrackbarPos(switch,'Tequila Sunrise')
        p = cv2.getTrackbarPos(Photo,'Tequila Sunrise')
        e = cv2.getTrackbarPos(Exit,'Tequila Sunrise')
        ##print(s2)
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y%H%M%S")
        if s2 == 2:
			out.write(img)
        if s == 1 and s2 == 0:
			s2=1
        if s == 0:
			out.release()
			s2=0
        if s2 == 1:
			out = cv2.VideoWriter('Video'+dt_string+str(video_counter)+'.avi',fourcc,10, (frame_width,frame_height))
			s2=2
        if p == 1:
            status = cv2.imwrite('Photo'+dt_string+'.png',img)
            print("Image written to file-system : ",status)
            cv2.setTrackbarPos(Photo, 'Tequila Sunrise', 0)
        if e == 1:
			break
			cv2.destroyAllWindows()
        if cv2.waitKey(1) == ord('q'):
            break  # esc to quit
            cv2.destroyAllWindows()
