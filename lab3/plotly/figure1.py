import cv2 
import numpy as np 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
img = cv2.imread(r'D:\Lab\Telecommunication Lab\lab3\figure1.jpg',0) 
fft = np.fft.fft2(img)
fft_vis = np.abs(fft)
# plotly.graph_objects.images don't work on grayscale 
#2d plot
fig = make_subplots(rows=1,cols=2,
                    subplot_titles=['Original Image','FFT'])
fig.add_trace(go.Heatmap(z=img,colorscale='gray',showscale=False),row=1,col=1)
fig.add_trace(go.Heatmap(z=fft_vis,colorscale='gray',showscale=False),row=1,col=2)
fig.update_yaxes(autorange='reversed', scaleanchor='x', constrain='domain')
fig.update_xaxes(constrain='domain', scaleanchor='y')
fig.show()
#3d plot
x,y = np.mgrid[0:img.shape[0],0:img.shape[1]]
fig1 = make_subplots(rows=1,cols=2,
                    specs=[[{'type':'surface'},{'type':'surface'}]],
                    subplot_titles=['Original Image','FFT'])
fig1.add_trace(go.Surface(x=x,y=y,z=img,colorscale='gray',showscale=False),row=1,col=1)
fig1.add_trace(go.Surface(x=x,y=y,z=fft_vis,colorscale='gray',showscale=False),row=1,col=2)
fig1.show()