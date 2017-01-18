#!/usr/bin/python3.5
# Created by Eudaemon, All Rights Reserved


import numpy as np
import cv2


img = cv2.imread('images.png')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


print(contours)
