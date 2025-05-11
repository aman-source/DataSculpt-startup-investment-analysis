import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/cleaned_startups_v2.csv')

st.title("Startup Status")



status_counts = df['status'].value_counts().reset_index()
status_counts.columns = ['Status', 'Count']
fig2 = px.pie(status_counts, names='Status', values='Count', title='Startup Status Distribution')
st.plotly_chart(fig2, use_container_width=True)
