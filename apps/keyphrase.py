import streamlit as st
import pandas as pd
import numpy as np

def app():
    df = pd.read_csv('data/Book1.csv')

    webinar = st.sidebar.selectbox('Select a webinar', [1,2,3])

    col01, col02 = st.beta_columns(2)
    col01.header('Top key phrases')

    col11, col12 = st.beta_columns(2)

    keyphrase = col02.text_input('Enter some text')

    col11.table(df)
    col12.table(df['text'][df['text'].str.contains(keyphrase, case=False)==True])

    #col12.table(df[[df['text'].str.contains(keyphrase, case=False) == True]])