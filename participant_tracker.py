import streamlit as st
import datetime

# ------ Sample Data ------
sample_data = [
    {'name': 'Alice', 'project': 'AI Onboarding', 'week': 45, 'date': datetime.date(2025, 10, 27), 'report': 'Completed initial setup.'},
    {'name': 'Alice', 'project': 'AI Onboarding', 'week': 46, 'date': datetime.date(2025, 11, 3), 'report': 'Configured Slack integration.'},
    {'name': 'Alice', 'project': 'AI Onboarding', 'week': 47, 'date': datetime.date(2025, 11, 10), 'report': 'Added onboarding checklist.'},
    {'name': 'Alice', 'project': 'AI Onboarding', 'week': 48, 'date': datetime.date(2025, 11, 17), 'report': 'Demoed onboarding module.'},
    {'name': 'Bob', 'project': 'Task Automation', 'week': 45, 'date': datetime.date(2025, 10, 27), 'report': 'Designed workflow logic.'},
    {'name': 'Bob', 'project': 'Task Automation', 'week': 46, 'date': datetime.date(2025, 11, 3), 'report': 'Wrote first automation script.'},
    {'name': 'Bob', 'project': 'Task Automation', 'week': 47, 'date': datetime.date(2025, 11, 10), 'report': 'Implemented prototype scripts.'},
    {'name': 'Bob', 'project': 'Task Automation', 'week': 48, 'date': datetime.date(2025, 11, 17), 'report': 'User testing and feedback.'},
]

st.title("Participant Weekly Performance Tracker (Prototype)")

# --- Step 1: Choose a participant ---
names = sorted({e['name'] for e in sample_data})
selected_name = st.selectbox("Select Participant", names)

# --- Step 2: Choose a project for that participant ---
projects = sorted({e['project'] for e in sample_data if e['name'] == selected_name})
selected_project = st.selectbox(f"Select Project for {selected_name}", projects)

# --- Step 3a: View by Week (Date Only in Selector) ---
weeks_info = [
    f"Week ({e['date'].strftime('%b %d, %Y')})"
    for e in sample_data if e['name'] == selected_name and e['project'] == selected_project
]
week_date_map = {
    f"Week ({e['date'].strftime('%b %d, %Y')})": e
    for e in sample_data if e['name'] == selected_name and e['project'] == selected_project
}
st.subheader("To view a single week's report")
if weeks_info:
    selected_week_label = st.selectbox("Choose Week", weeks_info)
    if st.button("Show Weekly Report"):
        entry = week_date_map.get(selected_week_label)
        st.success(f"**{selected_name} - {selected_project} - {selected_week_label}:**\n\n{entry['report']}")
else:
    st.info("No weekly data available for this project/participant.")

st.markdown("---")

# --- Step 3b: View by Date Range ---
st.subheader("View reports for a date range")
dates = [e['date'] for e in sample_data if e['name'] == selected_name and e['project'] == selected_project]
if dates:
    min_date, max_date = min(dates), max(dates)
    start_date, end_date = st.date_input("Select date range", [min_date, max_date], min_value=min_date, max_value=max_date)
    if st.button("Show Reports from Date Range"):
        filtered = [
            e for e in sample_data
            if e['name'] == selected_name and
               e['project'] == selected_project and
               start_date <= e['date'] <= end_date
        ]
        if filtered:
            for entry in filtered:
                st.markdown(f"- **Week ({entry['date'].strftime('%b %d, %Y')}):** {entry['report']}")
        else:
            st.info("No reports in selected date range.")
else:
    st.info("No date data available for this project/participant.")
