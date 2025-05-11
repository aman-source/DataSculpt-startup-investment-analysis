import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/cleaned_startups_v2.csv')

st.title("Funding Insights")

st.subheader("Investment Trends Over Years")
df_yearly = df.groupby('founded_year')['funding_total_usd'].sum().reset_index()
fig1 = px.line(df_yearly, x='founded_year', y='funding_total_usd', title="Investment Trends Over Years")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Funding Rounds Analysis")
round_cols = ['seed', 'venture', 'angel', 'private_equity']
round_sums = df[round_cols].sum().reset_index()
round_sums.columns = ['Funding Round', 'Amount']
fig2 = px.pie(round_sums, names='Funding Round', values='Amount')
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Funding vs Number of Rounds Correlation")
fig3 = px.scatter(df, x='funding_rounds', y='funding_total_usd', trendline='ols')
st.plotly_chart(fig3, use_container_width=True)
