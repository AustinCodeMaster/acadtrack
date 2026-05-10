### Building the Dashboard

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Title
st.title("Learner Performance Tracker")

# 2. Input Section (Sidebar)
st.sidebar.header("Enter Exam Data")
learner_name = st.sidebar.text_input("Learner Name", "Student A")
exam1 = st.sidebar.number_input("Exam 1 Score", min_value=0, max_value=100, value=0)
exam2 = st.sidebar.number_input("Exam 2 Score", min_value=0, max_value=100, value=0)
exam3 = st.sidebar.number_input("Exam 3 Score", min_value=0, max_value=100, value=0)

# 3. Data Processing
data = {
    "Exams": ["Exam 1", "Exam 2", "Exam 3"],
    "Scores": [exam1, exam2, exam3]
}
df = pd.DataFrame(data)

# 4. Display Results
st.subheader(f"Results for: {learner_name}")

# Create the Bar Graph
fig = px.bar(
    df, 
    x="Exams", 
    y="Scores", 
    text="Scores", 
    color="Exams",
    title=f" Mathematics Performance for - {learner_name}"
)

# Update layout to fix the scale
fig.update_layout(yaxis_range=[0, 100])

# Show graph in Streamlit
st.plotly_chart(fig)

# Show a summary table
st.table(df)