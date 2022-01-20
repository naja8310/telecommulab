import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\self.bmp',0)
#region mask
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask,(130,354),(210,313),255,-1)
#color mask
mask1 = cv2.inRange(img,50,130)
#combine mask
mask2 = (mask & mask1)
plt.imshow(mask1,cmap='gray')
plt.show()