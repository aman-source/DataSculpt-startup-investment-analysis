import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/cleaned_startups_v2.csv')

st.title("Dataset Overview")

st.subheader("Total Funding Distribution")
range_max = st.slider("Funding Range Max", 1000000, 100000000, 50000000)
fig1 = px.histogram(df[df['funding_total_usd'] <= range_max], 
                    x='funding_total_usd', nbins=30, title='Funding Distribution')
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Top Funded Startups")
top_n = st.slider("Top Startups", 5, 20, 10)
top_funded = df.nlargest(top_n, 'funding_total_usd')
fig2 = px.bar(top_funded[::-1], x='funding_total_usd', y='name', orientation='h')
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Yearly Startup Launch Trends")

year_counts = df['founded_year'].value_counts().reset_index()
year_counts.columns = ['Year', 'Startup Count']
year_counts = year_counts.sort_values('Year')

fig3 = px.bar(
    year_counts,
    x='Year',
    y='Startup Count',
    labels={'Year': 'Year', 'Startup Count': 'Number of Startups'},
    title="Number of Startups Founded Per Year"
)
st.plotly_chart(fig3, use_container_width=True)

