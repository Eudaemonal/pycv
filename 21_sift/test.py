#!/usr/bin/python3.5
# Created by Eudaemon, All Rights Reserved

import cv2
import numpy as np

img = cv2.imread('../src/shuttle.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
img=cv2.drawKeypoints(gray,kp,img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()






