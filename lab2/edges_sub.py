import cv2 
import matplotlib.pyplot as plt
import time
start = time.time() 
img = cv2.imread('D:\Lab\Telecommunication Lab\lab2\cameraman.jpg' , 0)
img_resize = cv2.resize(img,None,None,0.05,0.05)
sigma = 2 
factor = 0.75 
smoothedInput = cv2.GaussianBlur(img_resize,(7,7),sigmaX=sigma)  
ret, otsu = cv2.threshold(smoothedInput, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)   
edges = cv2.Canny(smoothedInput, ret * 0.4 * factor, ret * factor)
end = time.time()
print('Operate Time = {} Sec '.format(end-start))
plt.subplot(121) 
plt.imshow(img , cmap = 'gray') 
plt.title('Original Image') 
plt.subplot(122) 
plt.imshow(edges , cmap = 'gray') 
plt.title('Edges') 
plt.show()