# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:57:16 2021

@author: Neel
"""

import serial
import cv2
import base64
import requests


def detect_faces(path):
    from google.cloud import vision
    import io
    face_exists = 0
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
        
    image = vision.Image(content=content)
    response = client.face_detection(image=image)
    faces = response.face_annotations
    
    if faces:
        face_exists = 1
    else:
        face_exists = 0
        print("face not found")
        
    for face in faces:
        print('Confidence: {}'.format(face.detection_confidence))

    return face_exists


serial_distance = serial.Serial('COM5')
serial_distance.flushInput()
count = 0
count_valid = 0
live = cv2.VideoCapture(0)

while True:
    try:
        ser_bytes = serial_distance.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        count_valid += 1
        if decoded_bytes < 8 and count_valid > 2:
            ret, frame = live.read()
            color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', color)
            print("Action triggered!")
            serial_distance.close()
            cv2.imwrite('image.jpg', frame)
            
            with open("image.jpg", "rb") as file:
                url = "https://api.imgbb.com/1/upload"
                payload = {
                    "key": "4e8e6f9baef8b46f75ac078d4bded8c1",
                    "image": base64.b64encode(file.read()),
                }
                res = requests.post(url, payload)
                
                dict = res.json()
                url = dict['data']['url']
                print(url)
                
            break
        
    except:
        print("Error")
        count += 1
        if count > 100:
            break

live.release()
cv2.destroyAllWindows()
detected = detect_faces('image.jpg')
print(detected)
