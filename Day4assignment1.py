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
st.subheader("machine ")
# Text
st.text("ML BATCH")

#create a dataframe by reading the provided csv file
df=pd.read_csv(r"C:/Users/Suman/Sacramentorealestatetransactions.csv")
#to print the no of rows and columns in the dataset
print(df.shape)
print(df.describe())
#to verify head and tail of the dataset.
print(df.head(10))
print(df.tail(5))
#created a new dataframe with first 4 columns
newdf=df[['street', 'city', 'zip', 'state', 'beds']].copy()
print(newdf)
print("The details of real estate on the no of bedroom")
df1=newdf.groupby(['beds']).size()
print(df1)
print(df1.plot.pie(label='noofbeds',figsize=(11, 6)))
st.pyplot()
#display no of real estate available based on type of building 
df2=df.groupby(['type']).size()
print("Grouped data", df2)
#sorting real estate transaction data in the ascending order of price
print(df.to_numpy())
print("The maximum price")
print(df['price'].max())


