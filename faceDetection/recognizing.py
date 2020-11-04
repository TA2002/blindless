from firebase import firebase
import cv2
import numpy as np
import os
import playsound
import threading
import time
import pygame
import smtplib


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
id2 = 0

names = ['Unknown','Lost Child', 'Criminal', 'Stranger']

cam = cv2.VideoCapture(1)
cam.set(3, 450)
cam.set(4, 380)

cap2 = cv2.VideoCapture(2)
cap2.set(3,450)
cap2.set(4,380)

minW = 0.05*cam.get(3)
minH = 0.05*cam.get(4)

minW2 = 0.05*cap2.get(3)
minH2 = 0.05*cap2.get(4)

while True:

    ret, img =cam.read()
    ret2, img2 = cap2.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        gmail_user = 'onemanarmy228@gmail.com'
        gmail_password = 'nopassword'
        sent_from = gmail_user
        to = ['onemanarmy228@gmail.com', 'as.tarlan02@gmail.com']
        subject = 'Face was detected!!!'
        body = 'In the cinema'
        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)
        print(confidence)
        if (confidence < 120):
            if (id==1 or id==2) and (confidence<110):
                pygame.init()
                time.sleep(1)
                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(gmail_user, gmail_password)
                    server.sendmail(sent_from, to, email_text)
                    server.close()

                    print('Email sent!')
                except:
                    print('Email sent!')
                playsound.playsound("alarm.wav")
            id = names[id]
            confidence = "  {0}%".format(round(180 - confidence))

        else:
            id = "unknown"
            confidence = "  {0}%".format(round(180 - confidence))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)



    cv2.imshow('camera',img)

    faces2 = faceCascade.detectMultiScale(
        gray2,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW2), int(minH2)),
    )
    
    for(x,y,w,h) in faces2:
        
        cv2.rectangle(img2, (x,y), (x+w,y+h), (0,255,0), 2)
        
        id2, confidence2 = recognizer.predict(gray2[y:y+h,x:x+w])
        
        print(confidence2)
        if (confidence2 < 120):
            if (id2==1 or id2==2) and (confidence2<110):
                pygame.init()
                time.sleep(1)
                try:
                    gmail_user = 'onemanarmy228@gmail.com'
                    gmail_password = 'nopassword'
                    sent_from = gmail_user
                    to = ['as.tarlan02@gmail.com', 'onemanarmy228@gmail.com']
                    subject = 'Face was detected!!'
                    body = 'In the foodcoourt'
                    email_text = """\
                    From: %s
                    To: %s
                    Subject: %s
            
                    %s
                    """ % (sent_from, ", ".join(to), subject, body)
                    server2 = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server2.ehlo()
                    server2.login(gmail_user, gmail_password)
                    server2.sendmail(sent_from, to, email_text)
                    server2.close()
                    
                    print('Email sent!')
                except:
                    print('Email sent!')
                playsound.playsound("alarm.wav")
            id2 = names[id2]
            confidence2 = "  {0}%".format(round(180 - confidence2))

        else:
            id2 = "unknown"
            confidence2 = "  {0}%".format(round(150 - confidence2))

        cv2.putText(img2, str(id2), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img2, str(confidence2), (x+5,y+h-5), font, 1, (255,255,0), 1)


    cv2.imshow('camera2',img2)
    exitButton = cv2.waitKey(10) & 0xff
    if exitButton == 27:
        break

print("\n Stopping the programm ...")
cam.release()
cap2.release()
cv2.destroyAllWindows()

