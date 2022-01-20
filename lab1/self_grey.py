import cv2
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\self.bmp',0)
plt.imshow(img,cmap='gray')
plt.show()