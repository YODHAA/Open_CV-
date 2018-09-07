
Image Processing:
--------------------

software: 1.pip install opencv-python
           2.  pip install wheel
          3. 64 bit version of python.

1. 32/64 bit refers to types of CPU,OS,Drivers,Software Programmes that utilises the particular architecture.

2. 32-bit location: C:\Program Files (x86)\
64-bit location: C:\Program Files\
thus 64 bit system have two different installation directory but not so in 32 bit system.


Loading Images in Image Processing:
--------------------------------------

1.matplotlib: display frames from vedios and images.

import cv2
import matplotlib
import numpy

- Recording are done in frames,with 30to 60 times a second. At core they are like static images . 

Directional Tracking:
----------------------
 1.Detect the Presence of colored ball using computer vision.

 2.Track the ball as it moves around in the vedios frames, drawing its previous position as it moves.

 topic: Blurring, thresholding,edge detection

 - Read Image from Disk:
 ----------------------
  # import the necessary packages
import numpy as np
import argparse
import cv2


# Load the image path
path = "D:\Projects-Simplified\OPEN-CV\images.png"

# Read the image from disk
img=cv2.imread(path)

# Show the image : Original:name of window,file path (next parameter)
cv2.imshow("Original",img)

# Wait for user input (any key)to stop  the program
cv2.waitKey(0)
# takes integer and wait for ms or -1 

cv2.destroyAllWindowns()

note:

$ python load_image.py --image doge.jpg

then write : 
  ap=argparse.ArgumentParser()
  ap.add_argument("i","--image",required=True,help="Path to image")
  args=vars(ap.parse_args())

>image=cv2.imread(args["image"])

to meet the cmd prototype.
--image switch points to the path to the doge.jpg image.

thus argparse module: makes it easy to write user friendly command line interface.
if we want to use cmd to give input to programme:

import sys

tot=len(sys.argv);
s_args=str(sys.argv);

print(%tot); print(%s_args);
print(%str(sys.argv[0]));

if you want to print all input of cmd then other one:
 for i in xrange(tot):
 	 print("%d:%s",(i,str(sys.argv[0])));


input to compile:
$ ./prog_name input.txt output.txt;


Camera Detector:
-------------------

# initialise camera
cap=cv2.VedioCapture(0)

# Read Image
ret,frame=cap.read()

# show the process image
cv2.imshow('window',frame)

#close and exit camera
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()











