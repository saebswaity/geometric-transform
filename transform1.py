


import numpy as np 
import matplotlib.pyplot as plt
from skimage import transform
from skimage import io

im1= io.imread("testimage3.jpg")
plt.imshow(im1)
plt.show()

x=180
y=50
src = np.array([[0, 0], [x, 0], [0, y], [x, y]])
dst = np.array([[338, 1423], [795, 530], [349,1527], [864, 559]])
src2=src+[500,1500]

tform3 = transform.ProjectiveTransform()
tform3.estimate(src2, dst)
#warped = transform.warp(im1, tform3,output_shape=(1800, 800))
warped = transform.warp(im1, tform3)
plt.imshow(warped)

plt.show()
plt.subplot(221)
plt.imshow(im1)


plt.subplot(122)
plt.imshow(warped)

tform3.estimate(src+[0,-10], dst)
plt.subplot(223)
plt.imshow(transform.warp(im1, tform3,output_shape=(y,x)))

plt.show()


