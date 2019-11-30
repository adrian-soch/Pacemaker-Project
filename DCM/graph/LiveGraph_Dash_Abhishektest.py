#pip install dash
#http://127.0.0.1:8050/
import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

import struct
from serial import Serial

#Serial communication starts here

ser = Serial()
ser.port = 'COM8'
ser.baudrate = 115200
ser.timeout = 0.5
ser.dtr = 0
ser.open()
print("Is Serial Port Open:", ser.isOpen())

var = struct.pack('<BBHHHHHHHdddHHdddHHdHHH', 69,21,1,60,120,250,150,10,200,3.5,2,2.4,5,200,2.5,1.9,2.4,10,8,2,20,120,0)
ser.write(var)
#time.sleep(1)
print("reading...")
values = ser.read(100)
print(values)

print("Done")
ser.close()
print("Serial Port Closed")
num = struct.unpack('<dHdHddHHHHHHHHHHdHddHdd',values)
num1 = num[-2]
num2 = num[-1]

#Serial communication ends here

X = deque(maxlen=20)
X.append(0)
Y = deque(maxlen=20)
Y.append(0)

PulseWidth = 5
PulseAMP = 6


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph_scatter(input_data):
    X.append(X[-1]+1)
    if (X[-1]%PulseWidth==0):
        Y.append(PulseAMP)
    else:
        Y.append(0)

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}


if __name__ == '__main__':
    app.run_server(debug=True)