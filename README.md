# Face Recognition with AWS Automation 

Uisng LBPH algorithm to train the model for here Two Faces(mine and one celebrity),
if it recognizes mine face it by using pyttsx3 it speaks "HELLO PRIYANSHU ,SENDING WHATSAPP AND EMAIL" and sends it to given account.

As it recognizes Second Face(celebrity here) using Pyttsx3 it speaks :"HELLO HARRY STYLES,LAUNCHING EC2 INCTANCE AND ADDING VOLUME " it launches an specifies AMI ec2 instance by using python subprocess through AWS cli in my AWS account and attaches a volume specified .

At last :
it attaches a additional volume to the launched instance using the same AWS cli and subprocess module.


**Library used**

subprocess
Time
pyttsx3
pywhatkit
cv2
numpy
os
