# openCV use BGR (RGB color space)
import cv2
from matplotlib import pyplot as plt
path = 'D:\Lab\Telecommunication Lab\TelComSys2DSLab1\CGFaceGrayscale.bmp'
img = cv2.imread(path,0)
plt.imshow(img,cmap='gray')
plt.show()