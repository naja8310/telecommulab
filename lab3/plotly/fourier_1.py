import cv2 
import numpy as np 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
img = np.zeros((30,30)) 
img[5:24,13:17] = 1 
# src[start:end,start:end],เอาตัว start แต่ไม่เอาตัว end เช่น 2:5 คือเริ่มที่ array ห้องที่ 2 จบที่ห้อง 4
x,y = np.mgrid[0:img.shape[0],0:img.shape[1]]
fig = make_subplots(rows=1,cols=2,
                    subplot_titles=['Original Image','Surface View'],
                    specs=[[{'type':'heatmap'},{'type':'surface'}]])
fig.add_trace(go.Heatmap(z=img,colorscale='gray',showscale=False),row=1,col=1)
fig.add_trace(go.Surface(x=x,y=y,z=img,colorscale='gray',showscale=False),row=1,col=2)
fig.update_yaxes(autorange='reversed', scaleanchor='x', constrain='domain')
fig.update_xaxes(constrain='domain', scaleanchor='y')
fig.show()