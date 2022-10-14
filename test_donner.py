import pickle
import sys

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from dbn import SupervisedDBNClassification, SupervisedDBNRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
from PIL import Image

path_url = sys.argv[1]
path1 = ('ImagesPredict//' + path_url)
image = Image.open(path1).convert('L').resize((100, 100))
img = np.asarray(image)
img = img.astype('float32')
img /= 255.0
path = 'dbntrained_255_24_hum_94.pkl'
classifier = SupervisedDBNClassification.load(path)
y = list()
y.append(img)
y = np.array(y)
y = y.reshape(-1, 100 * 100)
Y_pred = classifier.predict(y)
# print(Y_pred[0]) #0-> normal 1-> pneumonie
if (Y_pred[0] == 0):
    print("Absence de signe de pneumonie.")
elif (Y_pred[0] == 1):
    print("Attention presence d'une pneumonie mogene !")
else:
    print("veillez inserer une image correct !")

