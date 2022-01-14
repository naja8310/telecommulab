# openCV use BGR (RGB color space)
import cv2
import sys
import numpy 
path = 'D:\Lab\Telecommunication Lab\TelComSys2DSLab1\imgtst.jpg'
img = cv2.imread(path,0)
print(img)