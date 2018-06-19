# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importing library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#importing dataset
dataset=pd.read_csv('Data.csv')
#print(type(dataset))

#Divinding data set into
#Matrix of features

X=dataset.iloc[ : , : -1]
print(type(X))

#Vector of dependent values

y= dataset.iloc[ : , 3 ]

# We take care of using missing parameter using scikit
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NaN",strategy="mean",axis=0)
imputer=imputer.fit(X.iloc[:,1:3])
X.iloc[:,1:3]=imputer.transform(X.iloc[:,1:3])
#encoding values
#importing library to use
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x=LabelEncoder()
X.iloc[:,0]=labelencoder_x.fit_transform(X.iloc[:,0])
#in 0,1,2 now to encode with dummy variables
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()
#for y only labelencoder is needed
labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)