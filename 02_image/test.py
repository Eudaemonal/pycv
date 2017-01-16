#!/usr/bin/python3.5


# Insert your code here


import numpy as np
import cv2


img = cv2.imread('opencv.png',0)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

