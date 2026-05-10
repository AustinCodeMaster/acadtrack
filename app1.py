import streamlit as st
import pandas as pd
import plotly.express as px
from tinydb import TinyDB, Query

# Initialize Database
db = TinyDB('student_data.json')
User = Query()

st.set_page_config(page_title="School Performance Tracker")

# Sidebar - Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Enter Data", "View Dashboard"])

# --- PAGE 1: DATA ENTRY ---
if page == "Enter Data":
    st.header("Enter Exam Scores")
    
    with st.form("data_form", clear_on_submit=True):
        name = st.text_input("Learner Name (e.g., Malcolm)")
        subject = st.selectbox("Subject", ["Maths", "English", "Science", "Swahili"])
        
        col1, col2, col3 = st.columns(3)
        with col1: e1 = st.number_input("Exam 1", 0, 100)
        with col2: e2 = st.number_input("Exam 2", 0, 100)
        with col3: e3 = st.number_input("Exam 3", 0, 100)
        
        submit = st.form_submit_button("Save to Database")
        
        if submit:
            if name:
                # Store data in TinyDB (No SQL needed!)
                db.insert({
                    'name': name.strip().title(),
                    'subject': subject,
                    'scores': [e1, e2, e3]
                })
                st.success(f"Data for {name} in {subject} saved successfully!")
            else:
                st.error("Please enter a learner name.")

# --- PAGE 2: VIEW DASHBOARD ---
else:
    st.header("📊 Performance Dashboard")
    
    # Get unique names from DB for the dropdown
    all_records = db.all()
    names = sorted(list(set([r['name'] for r in all_records])))
    # adding something
    if not names:
        st.info("No data found. Please go to 'Enter Data' to add some records.")
    else:
        selected_name = st.selectbox("Select Learner", names)
        
        # Filter data for the selected learner
        learner_records = db.search(User.name == selected_name)
        subjects = [r['subject'] for r in learner_records]
        
        selected_subject = st.radio("Select Subject to View", subjects, horizontal=True)
        
        # Find the specific record for that subject
        record = next(item for item in learner_records if item["subject"] == selected_subject)
        
        # Create DataFrame for Plotly
        df = pd.DataFrame({
            "Exams": ["Exam 1", "Exam 2", "Exam 3"],
            "Scores": record['scores']
        })
        
        # Display Bar Chart
        fig = px.bar(df, x="Exams", y="Scores", text="Scores", color="Exams",
                     title=f"{selected_subject} Performance: {selected_name}")
        fig.update_layout(yaxis_range=[0, 100])
        st.plotly_chart(fig)
        
        # Show a summary table
        st.dataframe(df.T) # .T transposes it for a cleaner look