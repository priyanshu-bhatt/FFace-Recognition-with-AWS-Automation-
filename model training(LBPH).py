#MODEL TRAINING FOR TWO PEOPLE


import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

# Get the training data we previously made
data_path = './facetask/first/'
data_path1='./facetask/harry/'

onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
onlyfiles1 = [f1 for f1 in listdir(data_path1) if isfile(join(data_path1, f1))]

# Create arrays for training data and labels
Training_Data, Labels = [], []
Training_Data1, Labels1 = [], []

# Open training images in our datapath
# Create a numpy array for training data
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
    
for j, files in enumerate(onlyfiles1):
    image_path1 = data_path1 + onlyfiles1[j]
    images1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    Training_Data1.append(np.asarray(images1, dtype=np.uint8))
    Labels1.append(j)

# Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)
#creating a numpy array for second person data and labels
Labels1 = np.asarray(Labels1, dtype=np.int32)


priyanshu_model= cv2.face_LBPHFaceRecognizer.create()
# Let's train Priynshu  model 
priyanshu_model.train(np.asarray(Training_Data), np.asarray(Labels))
print("*******Model  for Priyanshu trained sucessefully********")

harry_model= cv2.face_LBPHFaceRecognizer.create()
# Let's train our second  model 
harry_model.train(np.asarray(Training_Data1), np.asarray(Labels1))
print("******* Model trained for second person sucessefully*********")
