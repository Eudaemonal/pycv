#!/usr/bin/python3.5
# Created by Eudaemon, All Rights Reserved


import cv2
import numpy as np


img = cv2.imread('shuttle.jpg')

rows,cols = img.shape[:2]

# Transform

#M = np.float32([[1,0,100],[0,1,50]])
#dst = cv2.warpAffine(img,M,(cols,rows))



# Rotation

#M = cv2.getRotationMatrix2D((cols/2,rows/2),120,1)
#dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
