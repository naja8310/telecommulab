import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./CGFaceGrayscale.bmp',0)

plt.imshow(img, cmap='gray')
plt.show()