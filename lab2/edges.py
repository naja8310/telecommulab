import cv2 
import matplotlib.pyplot as plt
import time
img = cv2.imread('D:\Lab\Telecommunication Lab\lab2\cameraman.jpg' , 0)  
sigma = 2 
factor = 0.75 
start = time.time() 
smoothedInput = cv2.GaussianBlur(img,(7,7),sigmaX=sigma)  
ret, otsu = cv2.threshold(smoothedInput, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   
edges = cv2.Canny(smoothedInput, ret * 0.4 * factor, ret * factor)
end = time.time()
plt.subplot(121) 
plt.imshow(img , cmap = 'gray') 
plt.title('Original Image') 
plt.subplot(122) 
plt.imshow(edges, cmap = 'gray') 
plt.title('Edges')
plt.suptitle('Operate Time = {} Sec '.format(end-start))
plt.show()