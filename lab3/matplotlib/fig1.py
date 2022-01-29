import cv2 
import numpy as np 
import matplotlib.pyplot as plt
#import fft process 
img = cv2.imread(r'D:\Lab\Telecommunication Lab\lab3\figure1.jpg',0) 
fft = np.fft.fft2(img)
fft_vis = np.abs(fft)
#2d plot
plt.subplot(121) 
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(122) 
plt.imshow(fft_vis,cmap='gray')
plt.title('FFT')
plt.suptitle('Figure 1 2D View')
#3d plot
xx, yy = np.mgrid[0:img.shape[0],0:img.shape[1]]
fig = plt.figure()
ax = fig.add_subplot(121,projection='3d')
ax2 = fig.add_subplot(122,projection='3d')
ax.plot_surface(xx, yy, img, rstride=1, cstride=1, linewidth=0, cmap='gray')
ax.set_title('Original Image')
ax2.plot_surface(xx, yy, fft_vis, rstride=1, cstride=1, linewidth=0, cmap='gray')
ax2.set_title('FFT')
plt.suptitle('Figure 1 3D Surface View')
plt.show()