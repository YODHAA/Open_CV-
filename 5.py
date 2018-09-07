""" perfect code of simple computer vision"""

import cv2



def get_split(img,n):
    h,w=img.shape
    h_del=h/n
    w_del=w/n
    sp_img=[]
    for x in range (0,n):
        for y in range (0,n):
            sp_img.append(img[y*h_del:(y+1)*h_del,x*w_del:(x+1)*w_del])
    return sp_img
img=cv2.imread("lion.jpg")

