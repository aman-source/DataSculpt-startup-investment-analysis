import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/cleaned_startups_v2.csv')

st.title("Sector and Geographic Analysis")

st.subheader("Popular Startup Sectors")
sectors = df['category_list'].str.split(', ').explode().value_counts().head(10).reset_index()
sectors.columns = ['Sector', 'Count']
fig1 = px.bar(sectors[::-1], x='Count', y='Sector', orientation='h')
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Geographic Investment Analysis")
cities = df.groupby('city')['funding_total_usd'].sum().reset_index().sort_values(by='funding_total_usd', ascending=False).head(10)
fig2 = px.bar(cities[::-1], x='funding_total_usd', y='city', orientation='h')
st.plotly_chart(fig2, use_container_width=True)
