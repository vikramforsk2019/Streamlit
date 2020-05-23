import streamlit as st

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