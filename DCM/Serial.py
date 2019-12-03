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

var = struct.pack('<BBHHHHHHHdddHHdddHHdHHH', 69,7,1,60,120,250,150,10,200,3.5,2,2.4,5,200,2.5,1.9,2.4,10,8,2,20,120,0)  # B for unsigned char, takes an int
                                                                                                                                # d for double, takes a float
                                                                                                                                # < for little-endian, as programmed on FRDM board thru Simulink
print("To send (in binary): ", var)
print("Size of string representation is {}.".format(struct.calcsize('<BBB')))
#print("To send (in decimal): ", struct.unpack('<BBB',var))
#var = struct.unpack('<BBB',var)
print("send1",ser.write(var))   


#time.sleep(1)
var = struct.pack('<BBHHHHHHHdddHHdddHHdHHH', 69,21,1,60,120,250,150,10,200,3.5,2,2.4,5,200,2.5,1.9,2.4,10,8,2,20,120,0)
ser.write(var)
#time.sleep(1)
print("reading...")
values = ser.read(100)
print(values)

print("Done")
ser.close()
print("Serial Port Closed")
print("read (in decimal): ", struct.unpack('<dHdHddHHHHHHHHHHdHddHdd',values))


serialvar = struct.pack('<BBHHHHHHHdddHHdddHHdHHH', 69,21,1,60,120,250,150,10,200,3.5,2,2.4,5,200,2.5,1.9,2.4,10,8,2,20,120,0)

#Send over Serial
ser.write(serialvar)

#Read echo Parameters
serialvar = struct.pack('<BBHHHHHHHdddHHdddHHdHHH', 69,7,1,60,120,250,150,10,200,3.5,2,2.4,5,200,2.5,1.9,2.4,10,8,2,20,120,0)
echoVar = ser.read(100)
echoVarUP = struct.unpack('<dHdHddHHHHHHHHHHdHddHdd',echoVar)
checkList = [69,7,1,60,120,250,150,10,200,3.5,2,2.4,5,200,2.5,1.9,2.4,10,8,2,20,120,0]
for val in checklist:
    if(checkList(val) != echoVarUP(val)):
        print("error")