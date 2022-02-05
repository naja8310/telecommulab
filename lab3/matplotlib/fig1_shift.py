import cv2 
import numpy as np 
import matplotlib.pyplot as plt
#import fft process 
img = cv2.imread(r'D:\Lab\Telecommunication Lab\lab3\figure1.jpg',0) 
fft = np.fft.fft2(img)
fft_vis = np.abs(fft)
fftshift_vis = np.fft.fftshift(fft_vis)
#2d plot
plt.subplot(131) 
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(132) 
plt.imshow(fft_vis,cmap='gray')
plt.title('FFT')
plt.subplot(133) 
plt.imshow(fftshift_vis,cmap='gray')
plt.title('Shifted FFT')
plt.suptitle('Figure 1 2D View',y=0.85)
#3d plot
x,y = np.mgrid[0:img.shape[0],0:img.shape[1]]
fig = plt.figure()
ax = fig.add_subplot(131,projection='3d')
ax2 = fig.add_subplot(132,projection='3d')
ax3 = fig.add_subplot(133,projection='3d')
ax.plot_surface(x,y,img, rstride=1, cstride=1, linewidth=0, cmap='gray')
ax.set_title('Original Image')
ax2.plot_surface(x,y,fft_vis, rstride=1, cstride=1, linewidth=0, cmap='gray')
ax2.set_title('FFT')
ax3.plot_surface(x,y,fftshift_vis, rstride=1, cstride=1, linewidth=0, cmap='gray')
ax3.set_title('Shifted FFT')
plt.suptitle('Figure 1 3D Surface View',y=0.79)
plt.show()