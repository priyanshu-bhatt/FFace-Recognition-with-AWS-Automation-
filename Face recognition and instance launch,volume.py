import cv2
import numpy as np
import pywhatkit as py
import os
import pyttsx3
import time


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):
    
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi


# Open Webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    
    image, face = face_detector(frame)
    
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # "results" comprises of a tuple containing the label and the confidence value
        results = priyanshu_model.predict(face)
        results1=harry_model.predict(face)
        
        
        #SETTING UP CONFIDENCE SCORE FOR MY FACE
        if results[1]< 500:
            confidence = int( 100 * (1 - (results[1])/400) )
            display_string = str(confidence) + '% Confident it is User'
            
            
         #SETTING  UP CONFIDENCE SCORE FOR HARRY FACE   
        if results1[1]<500:
            confidence_harry= int( 100 * (1 - (results1[1])/400) )
            display_string1 = str(confidence_harry) + '% Confident it is User'
            
        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
        
        if confidence> 85:
            cv2.putText(image, "Hey Priyanshu !!", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image)
            ctr=1
            #ctr 1 for my face it will send whatsapp and email
            break
            
            
        if confidence_harry>85:
            cv2.putText(image, "Hey purva !!", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image)
            ctr=2 
            #ctr 2 for harry face it will launch an instance and attach volume
            break
            
        else:
            
            cv2.putText(image, "I dont know, how r u ", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )
            engine=pyttsx3.init()
            engine.setProperty("rate",160)
            engine.say("Sorry , I know only Priyanshu and Harry Styles") 
            engine.runAndWait()
            #pyttsx3.speak(" I know ,Prriyanshu ,and Hary Styles ,only ,sorry")

    except:
        cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.putText(image, "looking for face", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Face Recognition', image )
        pass
        
    if cv2.waitKey(1) == 13: #13 is theEnter Key
        break
cap.release()        
cv2.destroyAllWindows()



#email and whatsapp
if ctr==1:
    #subprocess.run('engine=pyttsx3.init() engine.setProperty("rate",160) engine.say("hello Priyanshu , sending WhatsApp and Email now") engine.runAndWait()',shell=True) 
    #pyttsx3.speak("Hello ,Priyanshu , Sending  WhatsApp and Email now")
    engine=pyttsx3.init()
    engine.setProperty("rate",160)
    engine.say("hello Priyanshu , sending WhatsApp and Email now") 
    engine.runAndWait()
    
    
    py.sendwhatmsg_instantly("+91 7302469023","Face detection")
    py.sendMail("exampleemail1822@gmail.com","example2345@##$%","exampleemail1822@gmail.com","FACE DETECTED")
    print("mail sent")
    
    
#FOR LAUNCHING INSTANCE AND ATTACHING STORAGE    

elif ctr==2:
    engine=pyttsx3.init()
    engine.setProperty("rate",160)
    engine.say("hello Harry Styles ,Launching ec2 instance and adding volume to it now") 
    engine.runAndWait()
    
    #Launching instance commands
    
    os.system("aws ec2 run-instances --image-id ami-0ad704c126371a549  --instance-type t2.micro  --count 1  --subnet-id subnet-7b98c237 --security-group-ids sg-0dae0a1d6032375b2 --key-name first_os_key >ec2.txt")
    print("Your Instance Had been Launched")
    #storage
    os.system(" aws ec2 create-volume --availability-zone ap-south-1b  --size 5  --volume-type gp2 >ebs.txt")
    print("volume created")
    time.sleep(30)
    engine=pyttsx3.init()
    engine.setProperty("rate",160)
    engine.say("To attach volume please  run the next Cell") 
    engine.runAndWait()
