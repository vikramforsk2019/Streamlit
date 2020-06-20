#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:41:11 2020

@author: jagveer
"""

import streamlit as st   
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.externals import joblib
import matplotlib.pyplot as plt
import os
def model_use(feature_set):
        model_list=['Multiple Regression.pkl','Decision tree.pkl']
        if st.checkbox('select Models for prediction'):
            selected=st.selectbox('Select',model_list)
        x_train,x_test,y_train,y_test = train_test_split(feature_set,y1,test_size=0.25,random_state=0)
        if selected:
            model_pkl=os.path.join('models pkl/',selected)
        classifer = joblib.load(model_pkl)
        
        y_predict = classifer.predict(x_test)
        plt.plot(y_predict[:20],color ='orange', 
         marker ='o', markersize = 12,  
         label ='predict')
        plt.plot(y_test[:20],color ='g', 
         linestyle ='dashed', linewidth = 2, 
         label ='actual')
        plt.title('AQI Level in different years') 
        plt.ylabel('AQI')
        plt.legend() 
        plt.show()
        st.pyplot()


if st.checkbox("Make Prediction"):
    df = pd.read_csv("city_day.csv")
    df.head(5)
    df.isnull().sum()
    df=df.fillna(df.mean())
    x1 = df.iloc[:,:13].values
    y1 = df.iloc[:,14:15].values
    z1 = pd.DataFrame(x1)
    z1=z1.drop([1], axis=1)
    x1 = z1.iloc[:,0:11].values
    z1 = pd.DataFrame(x1)
    ohe = OneHotEncoder()
    x_new1 = pd.DataFrame(ohe.fit_transform(x1[:,[0]]).toarray()) #state
    feature_set = pd.concat([x_new1,pd.DataFrame(z1.iloc[:,2:].values)],axis=1,sort=False)
    model_use(feature_set)
