import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image 
import matplotlib.pyplot as plt
import seaborn as sns
# Title
st.title("AIR Quality Analysis")

# Subheader
#st.subheader("Simple Data Science App")

# Text
#st.text("For a simple text")

html_temp = """
<div style="background-color:tomato;"><p style="color:green;font-size:60px;"> COVID 19 AQI OF INDIA</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)

img = Image.open("air.jpeg")
st.image(img,width=800,caption='INDIA AIR AQI')
# Videos

video_file = open("hare.mp4",'rb')
video_bytes = video_file.read()
st.video(video_bytes)

df=pd.read_csv('city_day.csv')

if st.checkbox("Show DataSet"):
		number = int(st.number_input("Number of Rows to View"))
		st.dataframe(df.head(number))
if st.button('column names'):
 		st.write(df.columns)
if st.checkbox('dataset shape'):
	 st.write(df.shape)
if st.checkbox('select columns to show'):	 
     all_columns=df.columns.tolist()
     selected=st.multiselect('Select',all_columns)
     new_df=df[selected]
     st.write(new_df)
if st.button("Data Types"):
	st.write(df.dtypes)
if st.button("Value Counts"):
	st.text("Value Counts By Target/Class")
	st.write(df.iloc[:,-1].value_counts())   #last column value count
if st.checkbox("Show Summary of Dataset"):
	st.write(df.describe())

st.subheader("Data Visualization")
# Show Correlation Plots
# Matplotlib Plot
if st.checkbox("Correlation Plot [Matplotlib]"):
	plt.matshow(df.corr())
	st.pyplot()

# Seaborn Plot
if st.checkbox("Correlation Plot with Annotation[Seaborn]"):
	st.write(sns.heatmap(df.corr(),annot=True))
	st.pyplot()


# Counts Plots
if st.checkbox("Plot of Value Counts"):
	st.text("Value Counts By Target/Class")

	all_columns_names = df.columns.tolist()
	primary_col = st.selectbox('Select Primary Column To Group By',all_columns_names)
	selected_column_names = st.multiselect('Select Columns',all_columns_names)
	if st.button("Plot"):
		st.text("Generating Plot for: {} and {}".format(primary_col,selected_column_names))
		if selected_column_names:
			vc_plot = df.groupby(primary_col)[selected_column_names].count()	#count non nan value 	
		else:
			vc_plot = df.iloc[:,-1].value_counts()
		st.text(vc_plot)
		st.write(vc_plot.plot(kind='bar'))
		st.pyplot()






























# SIDE Bar
st.sidebar.header("AIR Side bar")
st.sidebar.text("INDIA")
st.sidebar.text("other's")