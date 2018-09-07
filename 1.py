import numpy as np
import argparse
import cv2

# initialise camera
cap=cv2.VideoCapture(0)

# Read Image
ret,frame=cap.read()

# show the process image
cv2.imshow('window',frame)

#close and exit camera
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
