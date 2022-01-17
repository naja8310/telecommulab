import cv2 
import numpy as np 
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\CGFaceGrayscale.bmp',0) 
ret,thresh_bin = cv2.threshold(img,245,255,cv2.THRESH_BINARY)
plt.imshow(thresh_bin,cmap='gray')
plt.show()