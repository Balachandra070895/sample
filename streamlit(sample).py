import streamlit as st
import time as t


#title- It is used to add the title of an app
st.title("Welcome to VirueS")

# Header
st.header("Microsoft")

#sub header
st.subheader("Power BI")

#To give Information 
st.info("For Interacting Dashboards")

#warning message
st.warning("Come on time or else you will be marked absent")

#Error message
st.error("Wrong password")

#Success message
st.success("Congrats you have got A grade")

#write
st.write("Employee Name")

#range
st.write(range(50))

#Markdown
st.markdown("# VirtueS")
st.markdown("## VirtueS")
st.markdown("### VirtueS")
st.markdown(":moon:")

#Text
st.text("VirtueS learners")

#To write caption
st.caption("Caption is here")

#To display a mathematical equation (a+bx^2+c)
st.latex(r'''a+b x^2+c''')

# Widget

# Checkbox
st.checkbox("Login")

# Button
st.button("Click")

# Radio Widget
st.radio("Pick your Gender",["Male","Female","Others"])

# Select box
st.selectbox("Pick your course",["Cloud","PowerBI","Testing"])

# MultiSelect 
st.multiselect("Choose your department",["Sales","Manufacturing","Marketing"])

# Select Slider
st.select_slider("Rating",["Good","Bad","Satisfactory"])

# Slider
st.slider("Choose your number",0,100)

# Number_Input
st.number_input("Pick your Number",0,1000)

# Text_Input
st.text_input("Enter your Email")

# DATE_iNPUT
st.date_input("Opening Ceremony")

# Time_Input
st.time_input("Hey what's the time now")

# Text_Area
st.text_area("Hello VirtueS team. Here we have more information")

# If you want to upload a file/folder (upto 200mb is the limit)
st.file_uploader("Upload your file/foder")

# For choosing color
st.color_picker("Color")

# If you want to see the progress
st.progress(90)

# Spinner- used to show the temp time during execution
with st.spinner("Just wait"):t.sleep(1)

# Balloons-for celebrations 
st.balloons()

# Sidebar
st.sidebar.title("VirtueS")
st.sidebar.text_input("Email Address")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")
st.sidebar.radio("Profession",["Tester","Developer","Admin","Others"])


# Data Visualization

import pandas as pd
import numpy as np

st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)

st.title("Line Chart")
st.line_chart(data)

st.title("Area Chart")
st.area_chart(data)