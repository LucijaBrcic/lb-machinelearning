import streamlit as st
import pandas as pd

st.title('🎈 App Name')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df

st.write('Hello world!')
