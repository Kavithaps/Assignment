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

#create a dataframe by reading the provided csv file
df=pd.read_csv("Sacramentorealestatetransactions.csv")
df.head(10)
#to print the no of rows and columns in the dataset
df.shape
df.describe())
#to verify head and tail of the dataset.
df.head(10)
df.tail(5)
#created a new dataframe with first 4 columns
newdf=df[['street', 'city', 'zip', 'state', 'beds']].copy()
newdf
print("The details of real estate on the no of bedroom")
df1=newdf.groupby(['beds']).size()
df1
df1.plot.pie(label='noofbeds',figsize=(11, 6))
#st.pyplot()
#display no of real estate available based on type of building 
df2=df.groupby(['type']).size()
#sorting real estate transaction data in the ascending order of price
df.to_numpy()
print("The maximum price")
df['price'].max()


