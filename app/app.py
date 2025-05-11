import streamlit as st

st.set_page_config(
    page_title="Startup Investments Dashboard",
    layout="wide"
)

st.title("Startup Investments Analysis")
st.markdown("""
Welcome to the interactive dashboard on Indian Startup Investments. Navigate through the pages to discover insights:

### Dataset Overview
- Detailed exploration of the dataset, showing complete data structure.

### Funding Insights
- Insights on funding distribution, top-funded startups, and rounds.

### Sector Analysis
- Sector-specific analysis to identify booming startup categories.

### Status 
- startup status trends.

### Predictive Insights
- Machine learning model predicting startup success.

### Investor Network Graph
- Interactive network visualization showing relationships between investors and startups.
- Zoomable graphs for detailed analysis.

""")
