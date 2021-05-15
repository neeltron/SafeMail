# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:57:16 2021

@author: Neel
"""

import serial
serial_distance = serial.Serial('COM5')
serial_distance.flushInput()
count = 0
count_valid = 0

while True:
    try:
        ser_bytes = serial_distance.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        count_valid += 1
        if decoded_bytes < 8 and count_valid > 100:
            print("Action triggered!")
            serial_distance.close()
            break
    except:
        print("Error")
        count += 1
        if count > 100:
            break
