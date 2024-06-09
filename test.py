import numpy as np
import pandas as pd
import tensorflow as tf
import keras
from keras import Model
from keras.utils import load_img
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from keras.models import Sequential,load_model
from keras import layers
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization
import matplotlib.pyplot as plt
import os
import cv2
import csv
from PIL import Image
from keras.optimizers import RMSprop
 
# width = 80
# height = 50
# csv_file_path = r"C:\Users\Ido\Desktop\rnn project\try.csv"

# fields = ["filename","width","height","class"]



# with open(csv_file_path, 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields,lineterminator='\n')
#     writer.writeheader()
        
#     for i in range (10):
#         new_row = {'filename': str(i)+".jpg", 'width': width, 'height': height, 'class': "class"}
#         writer.writerow(new_row)
    
# with open('data.csv', 'r') as f:
#     reader = csv.reader(f)
#     data = list(reader)
# print(data)
# TODO EXTRACT ALL THE DATA FROM THE CSV FILES IN NNUMPY FORM

# labels = ['green', 'red', 'yellow', 'Bitter melon', 'Brinjal', 'Cabbage', 'Calabash', 'Capsicum', 'Cauliflower', 'Garlic', 'Ginger', 'Green Chili', 'Lady finger', "Onion", "Potato", "Sponge Gourd",
#           "Tomato", "apple", "apricots", "banana", "bell_pepper", "bitter_gourd", "carrot", "coconut", "cucumber", "dragon fruit", "grapes", "guava", "kiwi","lemon", "orange", "oren", "peach","pear",
#           "pineapple", "strawberry", "sugar apple", "zucchini"]
# labels.sort()
# print(labels)

def crop_direcory( array, csv_file_path):
    fields = ["filename","width","height","class"]

    
    i=0
    with open(csv_file_path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields,lineterminator='\n')

        writer.writeheader()
    
        for file in array:
            i +=1
            
            filename = file[0]
            width = file[1]
            height = file[2]
            category = file[3]
 
            if category not in ["red", "yellow", "green"]:
                
                new_row = {'filename': (str(i)+".jpg"), 'width': width, 'height': height, 'class': "not a traffic light"}
                writer.writerow(new_row)
               
               
test_df = pd.read_csv(r"F:\rnn project\object-detection-project\data\data_crop\test\_annotations.csv")
# test_df["class"]=test_df["class"].replace({"red": 0, "green": 1 , "yellow": 2})
array = test_df.to_numpy()
csv_file_path = r"F:\rnn project\try.csv"

crop_direcory( array, csv_file_path)