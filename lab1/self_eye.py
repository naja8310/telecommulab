import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\self.bmp',0)
#region mask
mask1 = np.zeros(img.shape[:2], dtype="uint8") 
cv2.rectangle(mask1,(77,212),(140,186),255,-1)
mask2 = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask2,(200,212),(266,187),255,-1)
#color mask
mask3 = cv2.inRange(img,0,60)
mask4 = cv2.inRange(img,150,200)
#combine mask
mask5 = ((mask1|mask2) & (mask3|mask4))
plt.imshow(mask5,cmap='gray')
plt.show()