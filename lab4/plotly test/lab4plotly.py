import cv2 as cv
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
img = cv.imread(r'D:\Lab\Telecommunication Lab\lab4\MyFacePic1.jpg',0) 
ret1,th1 = cv.threshold(img,216,255,cv.THRESH_BINARY) 
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) 
blur = cv.GaussianBlur(img,(5,5),0) 
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) 
images = [img,0,th1,
          img,0,th2,
          blur,0,th3]
fig = make_subplots(rows=3,cols=4,
                    subplot_titles=[
                    'Original Noisy Image','Histogram','Global Thresholding (v=127)','BW Histogram',
                    'Original Noisy Image','Histogram',"Otsu's Thresholding",'BW Histogram',
                    'Gaussian filtered Image','Histogram',"Otsu's Thresholding",'BW Histogram'])
fig.add_trace(go.Heatmap(z=img,colorscale='gray',showscale=False),row=1,col=1)
fig.add_trace(go.Histogram(x=img.ravel()),row=1,col=2)
fig.add_trace(go.Heatmap(z=th1,colorscale='gray',showscale=False),row=1,col=3)
fig.add_trace(go.Histogram(x=th1.ravel()),row=1,col=4)
fig.show()