


import numpy as np 
import matplotlib.pyplot as plt
from skimage import transform
from skimage import io

im1= io.imread("frame1.png")
plt.imshow(im1)
plt.show()

x=500
y=1000
src = np.array([[0, 0], [x, 0], [0, y], [x, y]])
dst = np.array([[122, 57], [446,87], [86,608], [521, 521]])


tform3 = transform.ProjectiveTransform()

tform3.estimate(src, dst)
plt.imshow(transform.warp(im1, tform3,output_shape=(y,x)))

plt.show()


