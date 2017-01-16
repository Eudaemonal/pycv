#!/usr/bin/python3.5
# Created by Eudaemon, All Rights Reserved


import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while(1):
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	cv2.imshow('frame', hsv)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()



