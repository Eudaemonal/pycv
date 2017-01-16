#!/usr/bin/python3.5
# Created by Eudaemon, All Rights Reserved


import cv2
import numpy as np


# Perspective
img = cv2.imread('shuttle.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

