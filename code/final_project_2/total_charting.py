import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

## Reading the data first
 
nif = pd.read_csv("C:\\Users\\naman\\Desktop\\Regression Anlysis\\code\\final_project_2\\base.csv")

print(nif)

from pylab import rcParams
from plotly import tools
import plotly as py

import plotly.graph_objs as go

fig = go.Figure(data=[go.Candlestick(
                open=nif['o'],
                high=nif['h'],
                low=nif['l'],
                close=nif['c'])])

fig.update_layout(
    title='Market Recovery Trading',
    yaxis_title='Nifty Index',
    
    shapes = [dict(
        x0='339', x1='575', y0=0, y1=1, xref='x', yref='paper',
        line_width=2),
        dict(
        x0='1576', x1='1960', y0=0, y1=1, xref='x', yref='paper',
        line_width=2),
         dict(
        x0='2278', x1='2588', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],

     annotations=[dict(
        x='339', y=0.04, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Recovery Begin'),
        dict(
        x='575', y=0.18, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Recovery lasted :220 Days'),
        dict(
        x='460', y=0.50, xref='x', yref='paper',
        showarrow=False, xanchor='center', text='2000 points increased'),
        dict(
        x='1576', y=0.40, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Recovery Begin'),
        dict(
        x='1960', y=0.40, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Recovery End'),
        dict(
        x='1820', y=0.80, xref='x', yref='paper',
        showarrow=False, xanchor='center', text='2000 points increased'),
        dict(
        x='2280', y=0.50, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Recovery Begin'),
        dict(
        x='2588', y=0.75, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Recovery End'),
         dict(
        x='2450', y=0.95, xref='x', yref='paper',
        showarrow=False, xanchor='center', text='2000 points increased')]
   
)

fig.show()


## base charting done
