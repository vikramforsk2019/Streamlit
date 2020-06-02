#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: jagveer
"""

import numpy as np
import pandas as pd

df = pd.read_csv("city_day.csv")
df.head(5)
df.isnull().sum()

df=df.fillna(df.mean())

x1 = df.iloc[:,:13].values

y1 = df.iloc[:,14:15].values

z1 = pd.DataFrame(x1)
z1=z1.drop([1], axis=1)

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder()
x_new1 = pd.DataFrame(ohe.fit_transform(x1[:,[0]]).toarray()) #state
feature_set = pd.concat([x_new1,pd.DataFrame(x1[:,1:12])],axis=1,sort=False)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

x_train,x_test,y_train,y_test = train_test_split(feature_set,y1,test_size=0.25,random_state=0)
# multiple linear regression model
mreg = LinearRegression()
mreg.fit(x_train,y_train)

mlr_y_predict = mreg.predict(x_test)

