import streamlit as st

# ------ Sample Data ------
sample_data = [
    {'name': 'Alice', 'project': 'AI Onboarding', 'week': 45, 'report': 'Completed initial setup.'},
    {'name': 'Alice', 'project': 'AI Onboarding', 'week': 46, 'report': 'Configured Slack integration.'},
    {'name': 'Alice', 'project': 'AI Onboarding', 'week': 47, 'report': 'Added onboarding checklist.'},
    {'name': 'Alice', 'project': 'AI Onboarding', 'week': 48, 'report': 'Demoed onboarding module.'},
    {'name': 'Bob', 'project': 'Task Automation', 'week': 45, 'report': 'Designed workflow logic.'},
    {'name': 'Bob', 'project': 'Task Automation', 'week': 46, 'report': 'Wrote first automation script.'},
    {'name': 'Bob', 'project': 'Task Automation', 'week': 47, 'report': 'Implemented prototype scripts.'},
    {'name': 'Bob', 'project': 'Task Automation', 'week': 48, 'report': 'User testing and feedback.'},
    # Add more entries as needed
]

# ------ Extract Options for Select Boxes ------
names = sorted(set(entry['name'] for entry in sample_data))
# For the demo, show all projects associated with chosen name
def get_projects_for_name(name):
    return sorted(set(e['project'] for e in sample_data if e['name'] == name))

def get_weeks_for_name_project(name, project):
    return sorted(set(e['week'] for e in sample_data if e['name'] == name and e['project'] == project))

st.title("Participant Weekly Report Tracker (Prototype)")

# --- UI Selection ---
selected_name = st.selectbox("Choose Participant", names)
projects = get_projects_for_name(selected_name)
selected_project = st.selectbox("Choose Project", projects)
weeks = get_weeks_for_name_project(selected_name, selected_project)
selected_week = st.selectbox("Choose Week (last 4)", weeks)

if st.button("Show Weekly Report"):
    # Find the relevant report
    report = next(
        (e['report'] for e in sample_data 
         if e['name'] == selected_name and e['project'] == selected_project and e['week'] == selected_week), 
        "No report found."
    )
    st.markdown(f"**Report for {selected_name}, {selected_project}, Week {selected_week}:**")
    st.info(report)
