import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\CGFaceGrayscale.bmp',0)
region = np.equal(img,156)
plt.imshow(region,cmap='gray')
plt.show()