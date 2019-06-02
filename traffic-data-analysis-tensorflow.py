# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:53:43 2018

@author: katiyar.a
"""
import os
import  skimage 
from skimage import data
import matplotlib

def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory) 
                   if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f) 
                      for f in os.listdir(label_directory) 
                      if f.endswith(".ppm")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels

ROOT_PATH = "D:/python/traffic-data"
train_data_directory = ROOT_PATH + "/Training"
test_data_directory = ROOT_PATH + "/Testing"

images, labels = load_data(train_data_directory)


# Print the `images` dimensions
print(images.ndim)

# Print the number of `images`'s elements
print(images.size)

# Print the first instance of `images`
images[0]


# Count the number of unique labels
print(len(set(labels)))