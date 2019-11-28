#Imports
import tkinter as tk
import serial
from serial import Serial
import numpy
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys
import time
import usb.core
from threading import Thread
import struct


portName = "COM6" #Change to our port

#State 1
mode = 0
startbyte = 69
serialtype = 0
serialvar = ''


#Start Serial Component
ser = serial.Serial(
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    port = portName,
    baudrate=115200
    )
print("Is Serial Port Open:", ser.isOpen())

try:
    mode = 1
    print("Point 1")

    serialvar = struct.pack('<B', 1)

    print("Point 2")
    transList = [0] * len(serialvar)
    i = 0
    while i<len(serialvar):
        transList[i] = serialvar[i]
        i += 1
    print("Point 3")
    ser.write(transList)
    print("Point 4")
    time.sleep(1)
    print("Point 5")
    ser.close()
    print("Point 6")
    print("Serial Port Closed")

except Exception as e: 
    print(e)
