""" print the image position """

import numpy
import cv2

img=cv2.imread('lion.jpg')
print img.shape
h,w,c=img.shape
lt=img[:,(w/2):,1:2]

cv2.imshow('LION',lt)

cv2.waitKey(0)
cv2.destroyAllWindows()
