import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
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
df['Date'] = pd.to_datetime(df['Date'])
df['year'] = df['Date'].dt.year
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
if st.checkbox("See How AQI(air quality index) is distributed?"):
	cities = ['Delhi', 'Ahmedabad', 'Hyderabad', 'Bengaluru', 'Kolkata']
	fig,ax = plt.subplots(figsize=(15, 7))

	for city in cities: 
	    sns.lineplot(x="Date", y="AQI", data=df[df['City']==city].iloc[::30],label = city)

	ax.set_xticklabels(ax.get_xticklabels(cities), rotation=30, ha="left")

	ax.set_title('AQI values in cities')
	ax.legend()
	st.pyplot()
if st.checkbox("Correlation Plot [Matplotlib]"):
	plt.matshow(df.corr())
	st.pyplot()

# Seaborn Plot
if st.checkbox("Correlation Plot with Annotation[Seaborn]"):
	st.write(sns.heatmap(df.corr(),annot=True))
	st.pyplot()
if st.checkbox("Plot distribution to  all the dataset columns"):
	all_col=df.columns.tolist()
	col=st.selectbox('select column',all_col)
	sns.set_style("darkgrid")
	sns.kdeplot(data=df[col],label=col ,shade=True)
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
if st.checkbox("Pie Plot"):
	all_columns_names = df.columns.tolist()
	# st.info("Please Choose Target Column")
	# int_column =  st.selectbox('Select Int Columns For Pie Plot',all_columns_names)
	if st.button("Generate Pie Plot"):
		# cust_values = df[int_column].value_counts()
		# st.write(cust_values.plot.pie(autopct="%1.1f%%"))
		st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
		st.pyplot()
if st.button("Generate Which city has lowest AQI?"):
	aqi = df.groupby('City')['AQI'].min().reset_index()
	aqi  = aqi.sort_values("AQI")
	aqi = aqi.head(10)
	fig1, ax1 = plt.subplots(figsize=(15,10))
	ax1.pie(aqi['AQI'].tolist(), labels=aqi['City'].tolist(), autopct='%1.1f%%',
	        shadow=True, startangle=90)
	plt.legend(loc='right',bbox_to_anchor=(1.2,0.9))
	st.pyplot()
if st.button("Generate Which city has highest AQI?"):
	aqi = df.groupby('City')['AQI'].max().reset_index()
	aqi  = aqi.sort_values("AQI")
	aqi = aqi.tail(10)
	fig1, ax1 = plt.subplots(figsize=(15,10))
	ax1.pie(aqi['AQI'].tolist(), labels=aqi['City'].tolist(), autopct='%1.1f%%',
	        shadow=True, startangle=90)
	plt.legend(loc='right',bbox_to_anchor=(1.2,0.9))
	st.pyplot()
if st.checkbox("Cities with highest AQI per year"):
	data1 = df['AQI'].dropna()
	top_10_city = df.loc[data1.index].groupby('City')['AQI'].mean().reset_index()
	top_10_city.sort_values('AQI', ascending=False, inplace=True)
	st.write(top_10_city.head(10))
	top_cities = top_10_city.head(10)['City'].tolist()
	city=st.selectbox('select city',top_cities)
	talcher = df[df['City']==city]
	data_by_year = talcher.groupby('year')['AQI'].mean().reset_index().dropna()
	st.write(data_by_year.head())
	plt.plot(data_by_year['year'], data_by_year['AQI'])
	plt.xticks(data_by_year['year'].tolist())
	plt.title('Year wise mean AQI for Talcher')
	plt.xlabel('Years')
	plt.ylabel('Mean AQI')
	plt.show()
	st.pyplot()

if st.checkbox("Which city has highest PM2.5"):
	df = df.fillna(0.0)
	no = df.groupby('City')['PM2.5'].mean().reset_index()
	no  = no.sort_values("PM2.5")
	no = no.head(10)
	st.write(no)
	fig1, ax1 = plt.subplots(figsize=(15,10))
	ax1.pie(no['PM2.5'].tolist(), labels=no['City'].tolist(), autopct='%1.1f%%',
	        shadow=True, startangle=90)
	plt.legend(loc='right',bbox_to_anchor=(1.2,0.9))
	plt.show()
	st.pyplot()






















# SIDE Bar
st.sidebar.header("AIR Side bar")
st.sidebar.text("INDIA")
st.sidebar.text("other's")