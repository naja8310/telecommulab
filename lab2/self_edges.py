import cv2
import matplotlib.pyplot as plt
import time
img1 = cv2.imread('D:\Lab\Telecommunication Lab\lab2\self.bmp',0)
img2 = cv2.imread('D:\Lab\Telecommunication Lab\lab2\MyCompressedFace.jpeg',0)
sigma = 2 
factor = 0.75
start = time.time() 
#img1
smoothedInput1 = cv2.GaussianBlur(img1,(7,7),sigmaX=sigma)  
ret, otsu1 = cv2.threshold(smoothedInput1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   
edges1 = cv2.Canny(smoothedInput1, ret * 0.4 * factor, ret * factor)
#img2
smoothedInput2 = cv2.GaussianBlur(img2,(7,7),sigmaX=sigma)  
ret, otsu2 = cv2.threshold(smoothedInput2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   
edges2 = cv2.Canny(smoothedInput2, ret * 0.4 * factor, ret * factor)
end = time.time()
print('Operate Time = {} Sec '.format(end-start))
plt.subplot(2,2,1) 
plt.imshow(img1, cmap = 'gray') 
plt.title('Original Image') 
plt.subplot(2,2,2) 
plt.imshow(edges1, cmap = 'gray') 
plt.title('Original Image Edges') 
plt.subplot(2,2,3) 
plt.imshow(img2, cmap = 'gray') 
plt.title('Compressed Image')
plt.subplot(2,2,4) 
plt.imshow(edges2, cmap = 'gray') 
plt.title('Compressed Image Edges')
plt.suptitle('Settasak Images')
plt.show()