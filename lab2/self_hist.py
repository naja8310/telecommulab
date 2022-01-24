import cv2
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab2\self.bmp',0)
compress = cv2.imread('D:\Lab\Telecommunication Lab\lab2\MyCompressedFace.jpeg',0)
#display
plt.subplot(1,2,1) # 1 row 2 colum img 1
plt.hist(img.ravel(),254,[0,254])
plt.title('Original img')
plt.subplot(1,2,2) # 1 row 2 colum img 2
plt.hist(compress.ravel(),253,[0,253])
plt.title('Compressed img')
plt.suptitle('Settasak Images')
plt.show()