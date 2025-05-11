import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

df = pd.read_csv('data/cleaned_startups_v2.csv')

st.title("Investor Network Graph")

sample_df = df[df['venture'] > 0].sample(100, random_state=42)

G = nx.Graph()

for _, row in sample_df.iterrows():
    investors = row[' market ']
    startup = row['name']
    G.add_node(startup, color='orange')
    for investor in investors.split(','):
        investor = investor.strip()
        if investor != 'Unknown':
            G.add_node(investor, color='blue')
            G.add_edge(investor, startup)

net = Network(height='600px', width='100%', bgcolor='#222222', font_color='white')
net.from_nx(G)
net.repulsion(node_distance=150, spring_length=100)

net.save_graph('investor_network.html')

html_file = open('investor_network.html', 'r', encoding='utf-8')
components.html(html_file.read(), height=620)
