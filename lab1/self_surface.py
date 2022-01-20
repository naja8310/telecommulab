import cv2 
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\self.bmp',0)
#downscaling has a "smoothing" effect
img = cv2.resize(img, (70,70))
xx, yy = np.mgrid[0:img.shape[0],0:img.shape[1]]
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(xx, yy, img, rstride=1, cstride=1, linewidth=0, cmap='gray')
plt.show()