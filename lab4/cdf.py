import cv2 as cv   
import numpy as np  
from matplotlib import pyplot as plt   
img = cv.imread(r'D:\Lab\Telecommunication Lab\lab4\MyFacePicSVRC.jpg',0)
hist,bins = np.histogram(img.ravel(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.ravel(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()