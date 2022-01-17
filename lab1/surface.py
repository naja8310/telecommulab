import cv2 
import numpy as np
import matplotlib.pyplot as plt
# canvas size
#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True
img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\CGFaceGrayscale.bmp',0)
# downscaling has a "smoothing" effect
#img = cv2.resize(img, (100,100))
xx, yy = np.mgrid[0:img.shape[0],0:img.shape[1]]
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(xx, yy, img, rstride=1, cstride=1, linewidth=0, cmap='gray')
plt.show()