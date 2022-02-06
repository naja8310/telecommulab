import cv2 as cv   
import numpy as np  
from matplotlib import pyplot as plt   
img = cv.imread(r'D:\Lab\Telecommunication Lab\lab4\MyFacePic1.jpg',0) 
ret1,th1 = cv.threshold(img,254,255,cv.THRESH_BINARY) 
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) 
blur = cv.GaussianBlur(img,(5,5),0) 
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) 
images = [img,0,th1,img,0,th2,blur,0,th3] 
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)','Original Noisy Image','Histogram',"Otsu's Thresholding",'Gaussian filtered Image','Histogram',"Otsu's Thresholding"] 
for i in range(3):     
    plt.subplot(3,4,i*4+1),plt.imshow(images[i*3],'gray')     
    plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])      
    plt.subplot(3,4,i*4+2),plt.hist(images[i*3].ravel(),256)    
    plt.title(titles[i*3+1]),plt.ylabel('Number of pixel'),plt.xlabel('intensity  value')      
    plt.subplot(3,4,i*4+3),plt.imshow(images[i*3+2],'gray')    
    plt.title(titles[i*3+2]),plt.xticks([]), plt.yticks([])      
    plt.subplot(3,4,i*4+4),plt.hist(images[i*3+2].ravel(),256)     
    plt.title('BW histrogram'),plt.ylabel('Number of pixel'),plt.xlabel('intensity value') 
plt.subplots_adjust(hspace=0.5)
plt.show()