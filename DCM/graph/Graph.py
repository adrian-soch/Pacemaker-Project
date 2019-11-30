import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from math import *

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("myfile.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
    ax1.clear()
    ax1.plot(xar,yar)

q = 1
p = 1
file1 = open("myfile.txt","w+")
while (q!=100):
    q += 1
    p = sin(q+2)
    file1.write(str(q)+","+str(p)+"\n")
file1.close()
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()