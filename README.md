# SafeMail (https://ratificate.us/SafeMail)

## BLAHAJGang Team

HackUPC and Neighborhood Hacks 2021 project.

Backend: https://github.com/neeltron/SafeMail

Frontend: https://github.com/saketsarin/SafeMail-frontend

Devpost: https://devpost.com/software/safemail

Demo Video: TBD

### Purpose and Functionality
SafeMail is a theft prevention system that uses facial recognition and identifies whether it's the authorized user or not and then unlocks the mailbox or cash counter. It informs the user, logs the image of the perpetrator on a dashboard, and finally tweets potential mail or cash theft on a neighborhood Twitter.

### Instructions to Run Frontend Locally:
Just open ```index.html``` in a web browser. :)

### Instructions to Run Backend Locally:

In a terminal:
```
git clone https://github.com/neeltron/SafeMail
cd Safemail
```

#### Arduino

Install Arduino IDE: https://www.arduino.cc/en/software/

Then, save and upload code to the physical board connected to your PC. If you don't have one, you can try an Arduino simulator from this list: https://all3dp.com/2/best-arduino-simulators-online-offline/

#### Python

In a terminal: 
```
py -m pip install --upgrade pip
pip install pyserial 
pip install opencv-python
pip install cognitive-face
pip install mysql
pip install mysql-connector
py SafeMail.py

```
to install all the libraries needed and then run the file (only works if you have a physical arduino connected to port COM5; can change this port on line 69).

### Authorship:
* **Neel Adwani** (https://devpost.com/neeltron)
* **Pravallika Myneni** (https://devpost.com/mynenisp1703)
* **Saket Sarin** https://devpost.com/sarinsaket)
* **Tiffany Trinh** (https://devpost.com/tiffanytrinh685)
