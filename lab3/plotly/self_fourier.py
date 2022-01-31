import cv2 
import numpy as np 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
img = cv2.imread(r'D:\Lab\Telecommunication Lab\lab3\self.bmp',0)
fft = np.fft.fft2(img) 
fft_abs = np.abs(fft)
fftshift = np.fft.fftshift(fft) 
fftshift_abs = np.abs(fftshift)
fftshift_log = np.log(1 + fftshift_abs) 
x,y = np.mgrid[0:img.shape[0],0:img.shape[1]]
fig = make_subplots(rows=1,cols=2,
                    subplot_titles=['Original Image','Surface View'],
                    specs=[[{'type':'heatmap'},{'type':'surface'}]])
fig.add_trace(go.Heatmap(z=img,colorscale='gray',showscale=False),row=1,col=1,)
fig.add_trace(go.Surface(x=x,y=y,z=img,colorscale='gray',showscale=False),row=1,col=2)
fig.update_yaxes(autorange='reversed', scaleanchor='x', constrain='domain')
fig.update_xaxes(constrain='domain')
fig.show()
