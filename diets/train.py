#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:25:46 2019

@author: sabiya
"""
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics

#from numpy import argmax
import numpy as np
#import sklearn.cross_validation as cross_validation
print('k')
diet_file_path = '/home/sabiya/Desktop/project/train1.csv'
diet_data = pd.read_csv(diet_file_path) 
#print(diet_data)
y=diet_data.iloc[:,12]
#print(y)
x = diet_data.iloc[:,[-8,-9,-10,-2]]
#print(x)
#x=diet_data.iloc[:,[3,4,5,11]]
print(type(diet_data))
print(type(x))
print(type(y))
#ohc1=pd.get_dummies(val_x)
#print(x)
new_diet_data = pd.read_csv('/home/sabiya/Documents/test.csv')
nx=new_diet_data.iloc[:,4]
ny=new_diet_data.iloc[:,[0,1,2,3]]
train_x,val_x,train_y,val_y=train_test_split(ny,nx,test_size=0.50,random_state = 0)
#train_x,train_y,val_x,val_y=cross_validation.train_test_split(x, y, train_size=0.75, random_state=101)
'''ohc=pd.get_dummies(train_x)
ohc2=pd.get_dummies(val_x)
ohc3=pd.get_dummies(train_y)
ohc4=pd.get_dummies(val_y)'''
#print(ohc2)




print("==========================transformation===========================")

le=LabelEncoder()
'''================================kidney_disease=================='''
kd=diet_data.iloc[:,-10]
nkd=np.array(kd)
print(type(nkd))
le.fit(nkd)
#list(le.classes)
tkd=le.transform(nkd)

pd.DataFrame(tkd).to_csv("/home/sabiya/Desktop/project/formatted.csv",index = False)
print(type(tkd))
print(tkd)
reversetkd=le.inverse_transform(tkd)
'''================================kidney_disease=================='''
#print(reversex)
'''================================heart_disease=================='''
hd=diet_data.iloc[:,-8]
nhd=np.array(hd)
le.fit(nhd)
#list(le.classes)
thd=le.transform(nhd)
pd.DataFrame(thd).to_csv("/home/sabiya/Desktop/project/formatted2.csv",index = False)
print(thd)
reversethd=le.inverse_transform(thd)
'''================================heart_disease=================='''
'''================================diabetes=================='''
dia=diet_data.iloc[:,-9]
ndia=np.array(dia)
le.fit(ndia)
#list(le.classes)
tdia=le.transform(ndia)
pd.DataFrame(tdia).to_csv("/home/sabiya/Desktop/project/formatted3.csv",index = False)
print(tdia)
reversetdia=le.inverse_transform(tdia)
'''================================diabetes=================='''

print("==========================transformation complete !===========================")
#dec=enc.dot(OHC.active_features_).astype(int)
#print(dec)
#print(ohc1)
#print(val_x)
my_model=DecisionTreeRegressor(random_state=1)
my_model.fit(train_x,train_y)

#print("The predictions are")
#pred=my_model.predict(val_x)

pred=my_model.predict([[1,0,1,3600]])
gt = np.array(train_y)
pqr=print(pred)
#print(pred)

fpr,tpr,threshold = metrics.roc_curve(gt,pred,pos_label=2)
acc = metrics.auc(fpr, tpr)
print(acc)
#print(pred)
#b=pred[:,-1]
#print(b)

#rs=argmax(pred)
#print(rs)
#x=pred[-1,:]
#print(x)
#print(type(pred))
#rs=pd.get_dummies(pred).idmax(1)
#rs=np.reshape(pred,(1,1))
#fpr,tpr,thresholds=metrics.roc_auc_score(train_y,pred)
#print(pred)
#metrics.auc(fpr,tpr)
#print(my_model.predict(ohc2.head(1)))



