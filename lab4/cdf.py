import cv2 as cv   
import numpy as np  
from matplotlib import pyplot as plt   
img = cv.imread(r'D:\Lab\Telecommunication Lab\lab4\MyFacePicSVRC.jpg',0)
# data distribution , cdf from hist and normalized
hist,bins = np.histogram(img.ravel(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.hist(img.ravel(),256,[0,256], color = 'r')
plt.plot(cdf_normalized, color = 'b')
plt.xlim([0,256])
plt.legend(('Normalized CDF','Histogram'), loc = 'upper left')
plt.show()