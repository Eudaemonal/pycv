#!/usr/bin/python3.5
# Created by Eudaemon, All Rights Reserved


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../src/shuttle.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()
# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
# Print all default params
print("Threshold: ", fast.getThreshold())
print("nonmaxSuppression: ", fast.getNonmaxSuppression())
print("neighborhood: ", fast.getType())
print("Total Keypoints with nonmaxSuppression: ", len(kp))

cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
