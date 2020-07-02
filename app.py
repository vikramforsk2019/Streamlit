import streamlit as st
import pandas as pd
from PIL import Image 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
import os
import base64
from sklearn.preprocessing import OneHotEncoder
matplotlib.use('Agg')

# Title
st.title("AIR Quality Analysis")

# Subheader
#st.subheader("Simple Data Science App")

# Text
#st.text("For a simple text")
activity = ['Analysis','About',]
choice = st.sidebar.selectbox("Select Activity",activity)

html_temp = """
<div style="background-color:tomato;"><p style="color:green;font-size:40px;">Impact of Air Pollution on our Lives</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)
if choice=="Analysis":
	img = Image.open("air.jpeg")
	st.image(img,width=800,caption='INDIA AIR AQI')
	img = Image.open("air4.png")
	st.info("Air pollution in India is a serious health issue Of the most polluted cities in the world, \
		21 out of 30 were in India in 2019.The 51% of pollution is caused by the industrial pollution, \
		27% by vehicles, 17% by crop burning and 5% by diwali fireworks.")
	st.image(img,width=800,caption='AIR AQI Different aspects')
	if st.checkbox("Show More"):
		st.text('1.Agricultural Burning is also a Major Problem ')
		st.info("Like tens of thousands of farmers in India’s northern states of Haryana, Punjab and Uttar Pradesh, \
			Satish, whose farm sits on the outskirts of the rural Haryana village of Gharaunda, had recently cleared \
			his fields of old rice crop stubble to make way for wheat by setting it alight. The practice was banned \
			when its contribution to the mounting pollution crisis in nearby Delhi and across northern India became \
			impossible to ignore, but deprived of equally cheap and easy alternatives of preparing the fields, farmers \
			have continued to flout the law.As record-breaking pollution threw Delhi into a state of crisis this week, \
			and the city was shrouded in a thick brown smog with toxins over 50 times the levels deemed healthy, crop \
			burning – which began in earnest in late October and is due to continue for the rest of the month – was \
			labelled as the chief culprit. According to the government environment agency, almost 50% of Delhi’s \
			pollution was from crop burning.")
		st.text('2.Traffic')
		st.success("One of the sources of PM 2.5 particles is car engine exhaust. While campaigning for more public  \
			transportation usage is in general good for the environment, the effectiveness toward reducing PM 2.5 \
			pollution is unclear. ")
		st.text("3.Industry And Power Generation")
		st.success("Various studies clearly show that causes of pollution, especially in Northern India cannot \
		 attributed to the farmers alone for burning farm biomass. Major share of the pollution is contributed by \
		 vehicular and industrial emissions.")
		st.info("Together, household air pollution from cooking and ambient (outside) air pollution cause more \
			han 50% of acute lower respiratory infections in children under 5 years of age in low- and \
			middle-income countries.")
	img = Image.open("air5.jpeg")
	st.image(img,width=800,caption='impact of AIR pollution on health')
	img = Image.open("air7.jpeg")
	if st.checkbox("Show Health More"):
		st.success("Air pollution is one of the leading threats to child health, \
	accounting for almost 1 in 10 deaths in children under five years of age.Every day around 93% of the world’s \
	children under the age of 15 years (1.8 billion children) breathe air that is so polluted it puts their \
	health and development at serious risk. According to a new report from the World Health Organization (WHO)\
	600,000 children died from acute lower respiratory infections caused by polluted air in 2016.\
	The new report also reveals that when pregnant women are exposed to polluted air, \
	they are more likely to give birth prematurely, and have small, low birth-weight children. \
	Air pollution also impacts neurodevelopment and cognitive ability and can trigger asthma, and \
	childhood cancer. Children who have been exposed to high levels of air pollution may be at greater \
	risk for chronic diseases such as cardiovascular disease later in life.")
		st.info("The health impact of air pollution is quite severe. It is estimated that 29% of cardiopulmonary \
			deaths and 40% of lung cancer deaths are attributable to air pollution.Mothers and young children are \
			especially vulnerable. During winter months (when pollution is highest) fetal deaths increase 3.5 times \
			and birth defects are more common.")
	st.image(img,width=800,caption='Delhi before and after covid 19 image')
	if st.checkbox("show  Delhi"):
		st.info("So if we are prepared to extrapolate up to high-levels of PM2.5, long-term exposure to Delhi’s \
		air is roughly equivalent to smoking 20 cigarettes a day, and will reduce life expectancy of inhabitants \
		by around 7 years, equivalent to losing around 3 hours life a day.")
	img = Image.open("air6.jpeg")
	st.image(img,width=800,caption='Solutions to overcome this pollution')
	if st.checkbox("show Solutions"):
		st.info("All countries should work towards meeting WHO global air quality guidelines to enhance the h\
			ealth and safety of children.reducing the over-dependence on fossil fuels in the global energy mix,\
	investing in improvements in energy efficiency and,facilitating the uptake of renewable energy sources.")
	# Videos

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
	if st.checkbox('check null values'):
		 st.write(df.isnull().sum())
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
def model_use(feature_set):
        selected=''
        model_pkl=''
        classifer=''
        model_list=['Multiple Regression.pkl','Decision tree.pkl']
        st.write('continue')
        if st.checkbox('select Models for prediction'):
            selected=st.selectbox('Select',model_list)
            model_pkl=os.path.join('models pkl/',selected)
            classifer = joblib.load(model_pkl)
            x_train,x_test,y_train,y_test = train_test_split(feature_set,y1,test_size=0.25,random_state=0)
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
        else:
        	st.write('pls Select Model')

        
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
    



# SIDE Bar
if choice =="About":
	st.sidebar.header("AIR Side bar")
	st.sidebar.text("INDIA")
	st.sidebar.text("other's")
	st.subheader("About us")
	st.info("Designed by Vikram")
	st.text("Data Science")
	st.success("Machine Learning Built with Streamlit")


