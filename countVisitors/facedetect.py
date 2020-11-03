from firebase import firebase
import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(2)
cap.set(3,450)
cap.set(4,380)

cap2 = cv2.VideoCapture(1)
cap2.set(3,450)
cap2.set(4,380)

count=0
i=1

while 1:
    ret, img = cap.read()
    ret2, img2 = cap2.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    faces2 = face_cascade.detectMultiScale(gray2, 1.3, 5)
    
    for (x,y,w,h) in faces2:
        cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)
        
        roi_gray = gray2[y:y+h, x:x+w]
        roi_color = img2[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    if (ret):
        cv2.imshow('img',img)
    if (ret):
        cv2.imshow('img2',img2)
    k = cv2.waitKey(30) & 0xff
    print(len(faces))
    
    if k == 27:
        break

cap.release()
cap2.release()
cv2.destroyAllWindows()
count=len(faces)
count2=len(faces2)
firebase = firebase.FirebaseApplication('https://school-8af38.firebaseio.com/')
data = {
    'faces': count
}

data2 = {
    'faces2': count2
}

#result = firebase.post('/MyTestData/', data)
result = firebase.put('https://school-8af38.firebaseio.com/','/face',data)
result2 = firebase.put('https://school-8af38.firebaseio.com/','/face2',data2)



