import streamlit as st
import seaborn as sns
import pandas as pd
import seaborn as sns
import plotly.express as px

df = sns.load_dataset("iris")
st.write("""
# Iris Dataset
How are different properties of Iris related to each other
""")
fig = px.scatter_3d(df, x = 'sepal_width', 
                    y = 'sepal_length', 
                    z = 'petal_width',
                    color = 'species', 
                    size='petal_length',
                    size_max = 20, 
                    opacity = 0.5)

st.plotly_chart(fig, use_container_width=True)