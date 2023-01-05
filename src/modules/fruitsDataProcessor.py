#from base64 import get_class_name
import os
import glob as gb
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

labels = {
    
    "apple" : 0, 
    "avocado" :1, 
    "banana" :2, 
    "cherry" :3, 
    "kiwi" :4, 
    "mango" :5, 
    "orange" :6, 
    "pinenapple" :7,
    "strawberries" :8, 
    "watermelon" :9 
}

def get_class_name(code):
    for x,y in labels.items():
        if code==y: return x
        
def _load_files(path,dim):

    X = []
    y = []
    
    for folder in os.listdir(path=path):
        
        files = gb.glob(pathname=str(path+folder + "/*.jpeg"))
        
        for imageFile in files:
            
            image = cv.imread(imageFile)
           

            if image is None:
                continue
            
            
            image_array = cv.resize(image , (dim,dim))
            
            X.append(list(image_array))
            y.append(labels[str.lower(folder)])
    
    return (X,y)

def load_data(dim):  
    (X_train,y_train) = _load_files('./data/train/',dim=dim)
    (X_test,y_test) = _load_files('./data/test/',dim=dim)
    
    return (X_train,y_train),(X_test,y_test)

def display_data(X,y):
    
    plt.figure(figsize=(20,20))
    
    for n,i in enumerate(list(np.random.randint(0,len(X) ,36))):
        img = cv.cvtColor(np.array(X[i]), cv.COLOR_BGR2RGB)
        plt.subplot(6 , 6 , n+1)
        plt.imshow(img)
        plt.axis("off")
        plt.title(get_class_name(y[i]))