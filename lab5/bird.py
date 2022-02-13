from PIL import Image
import numpy as np
img = Image.open(r'D:\Lab\Telecommunication Lab\lab5\ClassificationGS.jpg') # image extension *.png,*.jpg
new_width  = 270
new_height = 480
img = img.resize((new_width, new_height))
img.save(r'D:\Lab\Telecommunication Lab\lab5\ClassificationGSResult.jpg') # format may what u want ,*.png,*jpg,*.gif
from skimage.io import imread
#from skimage.color import rgb2gray
mountain_r = imread(r'D:\Lab\Telecommunication Lab\lab5\ClassificationGSResult.jpg')
#Plot
import matplotlib.pyplot as plt
plt.figure(0)
plt.imshow(mountain_r,cmap="gray")
plt.title("Resized Image")
plt.show()
import cv2
img = cv2.imread(r'D:\Lab\Telecommunication Lab\lab5\ClassificationGSResult.jpg',0)
arr = np.array(img)
data = np.reshape(arr, (1,np.product(arr.shape)))[0]
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
meandata = mean(data)
stddata = np.std(data)
x= meandata+(4*stddata)
c = np.arange(0, x, 1)
k = len(c)
i = len(data)
plt.figure(1)
hist,bin = np.histogram(data,c)
y = len(hist)
w = np.arange(0, x-1, 1)
r = hist/i
plt.bar(w,r)
plt.xlabel('Grayscale Value')
plt.ylabel('Probability')
plt.title("Probability Distribution")
plt.show()
plt.figure(2)
plt.hist(img.ravel(),256,[0,256])
plt.ylabel('Number of pixel')
plt.xlabel('Intensity Value')
plt.plot([20,20],[0,3000],'-k')
plt.plot([100,100],[0,3000],'-k')
plt.title("Histogram")
plt.show()

img = cv2.imread(r'D:\Lab\Telecommunication Lab\lab5\ClassificationGSResult.jpg',0)
arr = np.array(img)
data = np.reshape(arr, (1,np.product(arr.shape)))[0]

m = len(data)
epsilon = 1.0e-4 # แก้ Epsilon
difference = epsilon
counter = 0
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
c = 3 # แก้ C

from numpy.random import seed
from numpy.random import rand

seed(1)

mu_est = 2*mean(data)*np.sort(rand(c,1))

sigma_est = np.ones(c)*np.std(data)

p_est = np.ones(c)/c

def gaussian_norm_density(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))/(sig * np.sqrt(2 * np.pi))
d = max(data)

xl = np.arange(0, d*3,0.1)


p1_est = p_est[0] * gaussian_norm_density(xl, mu_est[0], sigma_est[0]); # แก้ตาม C
p2_est = p_est[1] * gaussian_norm_density(xl, mu_est[1], sigma_est[1]);
p3_est = p_est[2] * gaussian_norm_density(xl, mu_est[2], sigma_est[2]);
plt.figure(3)
plt.plot(xl,p1_est+p2_est+p3_est, 'r--',linewidth=2.0) # แก้ตาม C
plt.plot(xl, p1_est, 'g-.', linewidth=2.0);
plt.plot(xl, p2_est, 'g-.', linewidth=2.0);
plt.plot(xl, p3_est, 'g-.', linewidth=2.0);
plt.xlabel('Grayscale Value')
plt.ylabel('Probability')
plt.title('Gaussian Weight Distribution')
plt.show()

clas = []
ok = []
while np.any(difference >= epsilon) and (counter < 25000):
    for j in range(0, c):

        clas.insert(j, p_est[j] * gaussian_norm_density(data, mu_est[j], sigma_est[j]))

    ok = clas[0] + clas[1] + clas[2] # แก้ตาม C

    for j in range(0, c):
        clas[j] = clas[j] / ok
    mu_est_old = mu_est
    sigma_est_old = sigma_est
    p_est_old = p_est
    mu_est = []
    sigma_est = []
    p_est = []
    for j in range(0, c):
        mu_est.insert(j, sum((clas[j]) * data) / sum(clas[j]))
        sigma_est.insert(j, np.sqrt(sum((clas[j]) * np.power((data - mu_est[j]), 2)) / sum(clas[j])))
        p_est.insert(j, mean(clas[j]))

    difference = sum(abs(np.subtract(mu_est_old,mu_est)))+sum(abs(np.subtract(sigma_est_old,sigma_est)))\
                 +sum(abs(np.subtract(p_est_old,p_est)))

    print(difference)

    counter = counter + 800
    print('counter =',counter)
xl = np.arange(0, d, 0.1)

p1_est = p_est[0] * gaussian_norm_density(xl, mu_est[0], sigma_est[0]); # แก้ตาม C
p2_est = p_est[1] * gaussian_norm_density(xl, mu_est[1], sigma_est[1]);
p3_est = p_est[2] * gaussian_norm_density(xl, mu_est[2], sigma_est[2]);
plt.figure(4)
plt.plot(xl, p1_est + p2_est+p3_est, 'r--', linewidth=2.0) # แก้ตาม C
plt.plot(xl, p1_est, 'b-.', linewidth=2.0);
plt.plot(xl, p2_est, 'g-.', linewidth=2.0);
plt.plot(xl, p3_est, 'm-.', linewidth=2.0);
plt.plot([20,20],[0,0.012],'-k')
plt.plot([100,100],[0,0.012],'-k')
plt.xlabel('Grayscale Value')
plt.ylabel('Probability')
plt.legend(('Gaussian Mixture','W1','W2','W3'), loc = 'upper left')
plt.title('Gaussian Distribution')
plt.figure(5)
plt.imshow(arr,cmap='gray',vmin=20,vmax=100)
plt.title('Bird Cut')
plt.show()
