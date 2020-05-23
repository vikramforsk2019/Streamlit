import streamlit as st
import numpy as np
import pandas as pd
# Title
st.title("AIR Quality Analysis")

# Subheader
#st.subheader("Simple Data Science App")

# Text
#st.text("For a simple text")

html_temp = """
<div style="background-color:tomato;"><p style="color:white;font-size:60px;"> COVID 19 AQI OF INDIA</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)
df=pd.read_csv('city_day.csv')
if st.checkbox("Show DataSet"):
		number = int(st.number_input("Number of Rows to View"))
		st.dataframe(df.head(number))
if st.button('column names'):
 		st.write(df.columns)
if st.checkbox('dataset shape'):
	 st.write(df.shape)