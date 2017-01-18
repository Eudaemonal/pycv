#!/usr/bin/python3.5
# Created by Eudaemon, All Rights Reserved

import numpy as np
import cv2
from matplotlib import pyplot as plt



img = cv2.imread('../src/shuttle.jpg',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

hist, bins = np.histogram(img.ravel(),256,[0,256])

plt.hist(img.ravel(),256,[0,256]); plt.show()


