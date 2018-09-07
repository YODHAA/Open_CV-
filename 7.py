""" chess board made in image processing """

import numpy as np
import cv2

fullPattern =np.zeros((400,400),np.uint8)
""" np.zero initialses all values to zero in multidimensal array to zeroes
parameters : zeroes(shape,dtype=float,order='C')
here:=> shape:(2,3) or 2
        dtype:numpy.int8  by default numpy.float64
        order:{C or F} optional for storing data in C or Fortan contignous form
e.g: np.zeros(5)
     array([ 0.,  0.,  0.,  0.,  0.])
2. np.zeros((5,), dtype=np.int)
   array([0, 0, 0, 0, 0])
3. np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
      array([(0, 0), (0, 0)],
      dtype=[('x', '<i4'), ('y', '<i4')])
"""

fullPattern[:,:]=25
fullPattern[0:200,200:400]=255
cv2.imshow('chess',fullPattern)

cv2.waitKey(0)
cv2.destroyAllWindows()
