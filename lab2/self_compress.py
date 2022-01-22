import cv2
import matplotlib.pyplot as plt
import os
# read compress and write 
img = cv2.imread('D:\Lab\Telecommunication Lab\lab2\self.bmp',0)
img_compress = cv2.imwrite('D:\Lab\Telecommunication Lab\lab2\MyCompressedFace.jpeg',img, [int(cv2.IMWRITE_JPEG_QUALITY), 33])
result = cv2.imread('D:\Lab\Telecommunication Lab\lab2\MyCompressedFace.jpeg',0)
# size and dimension
## os path reveal size as byte 
size_img = (os.path.getsize('D:\Lab\Telecommunication Lab\lab2\self.bmp')/1000)
size_result = (os.path.getsize('D:\Lab\Telecommunication Lab\lab2\MyCompressedFace.jpeg')/1000)
h1, w1 = img.shape
h2, w2 = result.shape
img_title = ('Original Image With Size = {} kB Height = {} px and Width = {} px '.format(size_img,h1,w1))
compressed_title = ('Compressed Image With Size = {} kB Height = {} px and Width = {} px '.format(size_result,h2,w2))
#display
plt.subplot(1,2,1) # 1 row 2 colum img 1
plt.imshow(img,cmap='gray')
plt.title(img_title)
plt.subplot(1,2,2) # 1 row 2 colum img 2
plt.imshow(result,cmap='gray')
plt.title(compressed_title)
plt.suptitle('Settasak Images')
plt.show()