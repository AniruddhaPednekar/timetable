import streamlit as st
import requests
import pandas as pd

# Flask URL for timetable generation
FLASK_URL = "http://127.0.0.1:5000/generate_timetable"

st.title("Timetable Generator")

# Button to generate the timetable
if st.button('Generate Timetable'):
    response = requests.get(FLASK_URL)  # Call Flask API
    
    if response.status_code == 200:
        timetable = response.json()  # Parse JSON timetable from Flask

        # Convert timetable to a display-friendly format
        st.write("Generated Timetable:")
        for day, schedule in timetable.items():
            day_schedule = pd.DataFrame({day: schedule}, index=[i for i in range(1, len(schedule)+1)])
            st.dataframe(day_schedule)

    else:
        st.error("Error: Unable to generate timetable. Please try again.")
