""" perfect code of simple computer vision"""
""" to show the difference between the two images with image processing """

import numpy as np
import cv2

cap=cv2.VideoCapture(0)
ret,frame=cap.read()
if ret is True:
    g_old=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

h,w=g_old.shape
imgt1=cv2.resize(g_old,(w,h),interpolation=cv2.INTER_AREA)

while(True):
    ret,frame=cap.read()
    if ret is True:
        g_new=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    imgt2=cv2.resize(g_new,(w,h),interpolation=cv2.INTER_AREA)
    img_diff=cv2.absdiff(imgt2,imgt1)
    cv2.imshow('Result',img_diff)
    if cv2.countNonZero(img_diff)>2000:
        print "yo whats up"
    g_new=g_old
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()

    













