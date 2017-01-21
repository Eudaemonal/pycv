#!/usr/bin/python3.5
# Created by Eudaemon, All Rights Reserved


import numpy as np
import cv2
from matplotlib import pyplot as plt



x = np.random.randint(25,100,25)
y = np.random.randint(175,255,25)
z = np.hstack((x,y))
z = z.reshape((50,1))
z = np.float32(z)
plt.hist(z,256,[0,256]),plt.show()




