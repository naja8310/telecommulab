import cv2 
import numpy as np 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
img = cv2.imread(r'D:\Lab\Telecommunication Lab\lab3\figure1.jpg',0) 
fft = np.fft.fft2(img)
fft_vis = np.abs(fft)
fftshift_vis = np.fft.fftshift(fft_vis)
x,y = np.mgrid[0:img.shape[0],0:img.shape[1]]
# plotly.graph_objects.images don't work on grayscale 
fig= make_subplots(rows=2,cols=3,
                   specs=[[{'type':'heatmap'},{'type':'heatmap'},{'type':'heatmap'}],[{'type':'surface'},{'type':'surface'},{'type':'surface'}]],
                   subplot_titles=['Original Image','FFT','Shift FFT','Original Image','FFT','Shift FFT'])
#2d plot
fig.add_trace(go.Heatmap(z=img,colorscale='gray',showscale=False),row=1,col=1)
fig.add_trace(go.Heatmap(z=np.real(fft),colorscale='gray',showscale=False),row=1,col=2)
fig.add_trace(go.Heatmap(z=np.real(fftshift_vis),colorscale='gray',showscale=False),row=1,col=3)
#3d plot
fig.add_trace(go.Surface(x=x,y=y,z=img,colorscale='gray',showscale=False),row=2,col=1)
fig.add_trace(go.Surface(x=x,y=y,z=np.real(fft),colorscale='gray',showscale=False),row=2,col=2)
fig.add_trace(go.Surface(x=x,y=y,z=np.real(fftshift_vis),colorscale='gray',showscale=False),row=2,col=3)
fig.show()