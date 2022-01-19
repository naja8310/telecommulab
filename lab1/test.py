import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\CGFaceGrayscale.bmp',0)
mask1=cv2.inRange(img,50,285)
mask2=cv2.inRange(img,181,230)
mask3=np.equal(img,137)
mask4=np.equal(img,0)
mask5=np.equal(img,245)
filterd= ((mask3 | mask4 | mask5))
plt.imshow(filterd,cmap='gray')
plt.show()
