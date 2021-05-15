# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:57:16 2021

@author: Neel
"""

import serial
serial_distance = serial.Serial('COM5')
serial_distance.flushInput()

while True:
    try:
        ser_bytes = serial_distance.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
    except:
        print("Error")
        
