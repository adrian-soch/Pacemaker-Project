import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#serial libraries
import struct
from serial import Serial

ser = Serial()
ser.port = 'COM6'
ser.baudrate = 115200
ser.timeout = 0.5
ser.dtr = 0
ser.open()
print("Is Serial Port Open:", ser.isOpen())


fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x, y1, y2= [], [], []



while True:

    #Read echo Parameters
    serialvar = struct.pack('<BBHHHHHHHdddHHdddHHdHHH', 69,21,1, 60,120, 250, 150,10, 200, 2.5, 2, 2.4, 5, 200, 2.5, 2, 2.4, 10, 8, 2.5, 20, 120,0)
    ser.write(serialvar)
    echoVarUP = struct.unpack('<HHHHHHHdddHHdddHHdHHHdd', ser.read(100))
    num1 = echoVarUP[-2]
    num2 = echoVarUP[-1]
    
    x.append(i)
    y1.append(num1)
    y2.append(num2)
    
    ax.plot(x, y1, color='b')
    ax.plot(x, y2, color='r')
    
    fig.canvas.draw()
    
    ax.set_xlim(left=max(0, i-50), right=i+50)
    
    time.sleep(0.1)
    i += 1

plt.ion()
plt.draw()
ser.close()