import cv2
import numpy as np
import matplotlib.pyplot as plt
#26 254
img = cv2.imread(r'D:\Lab\Telecommunication Lab\lab4\MyFacePicSVRC.jpg',0)
mask = cv2.inRange(img,26,254)
np.bitwise_not(mask,img)
plt.imshow()