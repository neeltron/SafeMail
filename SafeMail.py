# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:57:16 2021

@author: Neel
"""

faceURI = "https://centralindia.api.cognitive.microsoft.com/face/v1.0/"
faceKey = "38850d7c8fe547d6af9dc644a5f1c894"

import serial
import cv2
import base64
import requests
import cognitive_face as CF
import mysql.connector
import requests
from io import BytesIO
from matplotlib.pyplot import imshow
from PIL import Image


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


def verify_face(face1, face2):
    verify = CF.face.verify(face1, face2)
    if verify['isIdentical'] == True:
        return "Verified"
    else:
        return "Not Verified"
            

def push_db(theft):
    db = mysql.connector.connect(
    host = "remotemysql.com",
    user = "hwW4R6cA0s",
    password = "9bVe4xsxvX",
    database = "hwW4R6cA0s"
    )
    cursor = db.cursor()
    sql = "INSERT INTO SafeMail (auth) VALUES (1)"
    val = str(theft)
    cursor.execute(sql, val)
    db.commit()
    

serial_distance = serial.Serial('COM5')
serial_distance.flushInput()
count = 0
count_valid = 0
live = cv2.VideoCapture(0)
CF.BaseUrl.set(faceURI)
CF.Key.set(faceKey)
img_url = 'https://c.ndtvimg.com/2021-03/9op9k9ko_elon-musk-reuters_625x300_25_March_21.jpg'
result = CF.face.detect(img_url)
print(result)
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))


while True:
    try:
        ser_bytes = serial_distance.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        count_valid += 1
        if decoded_bytes < 8 and count_valid > 5:
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
            
            imshow(img)
            face1 = result[0]['faceId']
            print ("Face 1:" + face1)	
            
            img2_url = url
            response2 = requests.get(img2_url)
            img2 = Image.open(BytesIO(response2.content))
            
            result2 = CF.face.detect(img2_url)
            
            if result2 is not None:
                face2 = result2[0]['faceId']
                print ("Face 2:" + face2)
            
            val = verify_face(face1, face2)
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
theft = 0
if val == "Verified":
    theft = 0
else:
    theft = 1
    tweet_exec = requests.get('https://maker.ifttt.com/trigger/tweelon/with/key/dnDRzxYa_9QqoK-lOJYa_K')
    print(tweet_exec.status_code)
    
print(theft)
push_db(theft)
