import cv2
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab2\cameraman.jpg',0)
img_resize = cv2.resize(img,None,None,0.1,0.1)
result = cv2.imwrite('D:\Lab\Telecommunication Lab\lab2\subsampledImage .jpeg',img_resize)
#display
plt.subplot(1,2,1) # 1 row 2 colum img 1
plt.imshow(img,cmap='gray')
plt.title('Original img')
plt.subplot(1,2,2) # 1 row 2 colum img 2
plt.imshow(img_resize,cmap='gray')
plt.title('Resized img')
plt.show()