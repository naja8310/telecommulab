import cv2 
import numpy as np 
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\CGFaceGrayscale.bmp',0) 
ret,thresh_mount = cv2.threshold(img,157,255,cv2.THRESH_BINARY)
cv2.imwrite('D:\Lab\Telecommunication Lab\lab1\imgmount.bmp',thresh_mount)