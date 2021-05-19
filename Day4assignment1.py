# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:22:35 2021

@author: Suman
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
import streamlit as st
st.title("Assignment-Day4")
st.header("ICFOSS")
# Subheader
st.subheader("Machine Learning")
# Text
st.text("ML BATCH7")
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)

#create a dataframe by reading the provided csv file
df=pd.read_csv("Sacramentorealestatetransactions.csv")
tips=df.head(10)
st.text ("The no of rows and columns in the dataset")
df.shape
df.describe()
st.text ("verify head and tail of the dataset")
df.head(10)
df.tail(5)
st.text ("created a new dataframe with first 4 columns")
newdf=df[['street', 'city', 'zip', 'state', 'beds']].copy()
newdf
st.text ("The details of real estate on the no of bedroom")
df1=newdf.groupby(['beds']).size()
df1
st.subheader ("Pie Chart")
 
b=df1.plot.pie(label='noofbeds',figsize=(11, 6))
b.plot(kind='pie')
print("Display no of real estate available based on type of building") 
df2=df.groupby(['type']).size()
df2
st.text ("sorting real estate transaction data in the ascending order of price")
df.to_numpy()
st.text ("The maximum price")
df['price'].max()


