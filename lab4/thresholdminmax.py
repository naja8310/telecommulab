import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'D:\Lab\Telecommunication Lab\lab4\MyFacePicSVRC.jpg',0)
blur = cv2.GaussianBlur(img,(5,5),0) 
mask = cv2.inRange(blur,160,190)
ret,th = cv2.threshold(mask,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(th,cmap='gray')
plt.title("Otsu's Thresholding")
plt.show()