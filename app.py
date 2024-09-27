import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

## Title of the app
st.title("This is a base Streamlit App")

## Display some text
st.write("This is some sample text")

## Load a dataframe and display it.
### Load
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
### Display
st.write(df.head())

## Create a line chart
st.write("This is a line chart of the Iris dataset")
st.line_chart(df)