import cv2
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab2\cameraman.jpg',0)
img_resize = cv2.imread('D:\Lab\Telecommunication Lab\lab2\subsampledImage .jpeg',0)
#display
plt.subplot(1,2,1) # 1 row 2 colum img 1
plt.hist(img.ravel(),64,[0,64])
plt.title("Original img")
plt.subplot(1,2,2) # 1 row 2 colum img 2
plt.hist(img_resize.ravel(),64,[0,64])
plt.title("Resized img")
plt.show()