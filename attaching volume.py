#Attaching 5GB volume to created instance

os.system("aws ec2 attach-volume --volume-id   VOLUME ID --instance-id  INSTANCE ID    --device /dev/xvdi")
engine=pyttsx3.init()    
engine.setProperty("rate",160)
engine.say("Thank you ,Your volume is attached now") 
engine.runAndWait()
