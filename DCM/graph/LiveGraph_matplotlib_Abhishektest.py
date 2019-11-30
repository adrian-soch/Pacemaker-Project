import time
import matplotlib.pyplot as plt
import math

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

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x, y = [], []

while True:
    x.append(i)
    y.append(math.sin(x[-1]))
    
    ax.plot(x, y, color='b')
    
    fig.canvas.draw()
    
    ax.set_xlim(left=max(0, i-50), right=i+50)
    
    time.sleep(0.1)
    i += 1

plt.show()