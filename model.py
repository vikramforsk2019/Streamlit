#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  
@author: jagveer
"""
import pandas as pd

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
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder()
x_new1 = pd.DataFrame(ohe.fit_transform(x1[:,[0]]).toarray()) #state
feature_set = pd.concat([x_new1,pd.DataFrame(z1.iloc[:,2:].values)],axis=1,sort=False)

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

y_predict = mreg.predict(x_test)

#df2 = pd.DataFrame({'Actual': y_test, 'Predicted':y_predict}) 
 
print (df) 
from matplotlib import pyplot as plt
#Visualize the best fit line
#df['Date'] = pd.to_datetime(df['Date'])
#df['year'] = df['Date'].dt.year
#year=df['year']

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



# polynomial regression model
# degree = 2

poly_reg = PolynomialFeatures(degree = 2)
preg = LinearRegression()
pf = poly_reg.fit_transform(x_train)
preg.fit(pf,y_train)

pr_y_predict = preg.predict(poly_reg.fit_transform(x_test))

# decision tree regression model

dec_tree = DecisionTreeRegressor(random_state = 0)
dec_tree.fit(x_train,y_train)

dt_y_predict = dec_tree.predict(x_test)
# random forest regression model
# random forest with 500 trees

rt_reg = RandomForestRegressor(n_estimators = 500, random_state = 0)
rt_reg.fit(x_train,y_train)
rt_y_predict = rt_reg.predict(x_test)

# --- feature scaling the paramenters for better results ---
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x_train_svr = sc_x.fit_transform(x_train)
y_train_svr = sc_y.fit_transform(y_train)

svr_reg = SVR()
svr_reg.fit(x_train_svr,y_train_svr)

svr_y_predict = sc_y.inverse_transform(svr_reg.predict(sc_x.transform(x_test)))




# Use the loaded pickled model to make predictions 
from sklearn.externals import joblib
joblib.dump(mreg,"Multiple Regression.pkl")
joblib.dump(preg, "pregression.pkl")
joblib.dump(dec_tree, "Decision tree.pkl")
joblib.dump(rt_reg, "RandomForest.pkl")
joblib.dump(svr_reg, "svrression.pkl")

# Load model from file
classifer = joblib.load("pregression.pkl")
classifer.predict(x_test) 
classifer.predict(poly_reg.fit_transform(x_test)) 


model_list=['MR','PR','DTR','RF','SVR']
import streamlit as st
if st.checkbox('select columns to show'):	 
	 selected=st.multiselect('Select',model_list)
	 #new_df=df[selected]
	 st.write(selected)



