import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\CGFaceGrayscale.bmp',0)

th1 = 1
th2 = 137
th3 = 245
thr = th1 and th2 and th3
region = np.equal(img, thr)
plt.imshow(region,cmap='gray')
plt.show()