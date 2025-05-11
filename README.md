# Startup Investments Analysis Dashboard

## Overview

This project analyzes startup funding data from the startup ecosystem. It explores how startups have evolved in terms of funding, founding trends, investor relationships, sector performance, and success likelihood. The project includes an interactive Streamlit dashboard with multiple pages, visualizations, and a predictive model.

## Problem Statement

Understanding startup investment trends is crucial for investors, entrepreneurs, and analysts. With thousands of startups operating, it becomes important to identify which sectors attract the most funding, which cities are most active, what funding patterns correlate with success, and how investment networks are structured.

## Objective

Build a fully interactive Streamlit dashboard that delivers deep, visual, and predictive insights from the startup dataset. The dashboard helps users answer questions like:

- Which startups have raised the most funding?
- Which sectors are attracting the most attention?
- What are the trends in funding across years and cities?
- How do funding rounds relate to startup success?
- Can we predict whether a startup will likely survive?

## Features

### 1. Dataset Overview
- Explore the structured dataset after cleaning.
- Visualize overall funding distribution.
- View top funded startups.
- Observe startup founding trends by year.

### 2. Funding Insights
- Yearly funding trend analysis.
- Distribution across seed, venture, angel, and private equity.
- Correlation between number of rounds and funding raised.

### 3. Sector & Geographic Analysis
- Identify top-performing startup sectors.
- Analyze investment distribution across Indian cities.

### 4. Investor Network Grapgh
- Explore investor-startup network graph.\
- Zoomable graph

### 5. Predictive Insights
- Predict the success probability of a startup using Random Forest based on funding and funding rounds.

### 6. Startup Status
- Visualize operating vs closed startups.

## Dataset

The dataset contains information about:
- Startup name, founding year, city, region
- Total funding raised
- Funding rounds (seed, venture, angel, etc.)
- Status (operating, closed, acquired)
- Sector/category information

Cleaned version used: `data/cleaned_startups_v2.csv`

## Technologies Used

- Python
- Pandas, NumPy
- Streamlit
- Plotly
- Scikit-learn
- NetworkX, PyVis

## How to Run the App

1. Install dependencies:
- pip install -r requirements.txt

2. Run the app
- streamlit run app/app.py


