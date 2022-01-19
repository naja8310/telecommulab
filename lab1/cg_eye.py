import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('D:\Lab\Telecommunication Lab\lab1\CGFaceGrayscale.bmp',0)
#region mask
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask,(50,183),(290,250),255,-1)
#color mask
mask1=np.equal(img,137) #คิ้วกับตาดำนอก
mask2=np.equal(img,0) # ตาดำใน
mask3=np.equal(img,245) #ตาขาว
#combine mask
mask_c= (mask & (mask1 | mask2 |mask3))
plt.imshow(mask_c,cmap='gray')
plt.show()
