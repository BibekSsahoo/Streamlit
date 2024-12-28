import streamlit as st
import pandas as pd

data = {
    'task':['Extract','Transfermation', 'Load'],
    'status':['Completed','Inprogress','Pending']}

df=pd.DataFrame(data)
st.write('ETL PIPELINE EXECUTION STATUS created by Bibek Sahoo',df)