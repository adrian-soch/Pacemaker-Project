import struct
import time
from serial import Serial

ser = Serial()
ser.port = 'COM8'
ser.baudrate = 115200
ser.timeout = 0.5
ser.dtr = 0
ser.open()
print("Is Serial Port Open:", ser.isOpen())

var = struct.pack('<BBB', 69,7,1)  # B for unsigned char, takes an int
                                                                                                                                # d for double, takes a float
                                                                                                                                # < for little-endian, as programmed on FRDM board thru Simulink
print("To send (in binary): ", var)
print("Size of string representation is {}.".format(struct.calcsize('<BBB')))
print("To send (in decimal): ", struct.unpack('<BBB',var))
#var = struct.unpack('<BBB',var)
print("send1",ser.write(var))   

time.sleep(1)
ser.close()
print("Serial Port Closed")

# try:
#     mode = 1
#     print("Point 1")

#     serialvar = struct.pack('<B', 1)

#     print("Point 2")
#     transList = [0] * len(serialvar)
#     i = 0
#     while i<len(serialvar):
#         transList[i] = serialvar[i]
#         i += 1
#     print("Point 3")
#     ser.write(transList)
#     #ser.write(serialvar)
#     print("Point 4")
#     time.sleep(1)
#     print("Point 5")
#     ser.close()
#     print("Point 6")
#     print("Serial Port Closed")

# except Exception as e: 
#     print(e)
