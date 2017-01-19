#!/usr/bin/python3.5
# Created by Eudaemon, All Rights Reserved


import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('../src/shuttle.jpg')

surf = cv2.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img,None)

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()
