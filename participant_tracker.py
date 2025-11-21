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
    # Add more entries as needed
]

st.title("Participant Weekly Report Tracker (with Date and Week Selection)")

# --- Extract options for selection ---
names = sorted({e['name'] for e in sample_data})

def get_projects_for_name(name):
    return sorted({e['project'] for e in sample_data if e['name'] == name})

def get_weeks_for_name_project(name, project):
    return sorted({e['week'] for e in sample_data if e['name'] == name and e['project'] == project})

def get_dates_for_name_project(name, project):
    return sorted({e['date'] for e in sample_data if e['name'] == name and e['project'] == project})

selected_name = st.selectbox("Choose Participant", names)
projects = get_projects_for_name(selected_name)
selected_project = st.selectbox("Choose Project", projects)

# --- Week slider selection ---
weeks = get_weeks_for_name_project(selected_name, selected_project)
if weeks:
    min_week = min(weeks)
    max_week = max(weeks)
    selected_week = st.slider("Select Week Number", min_week, max_week, value=max_week)

    if st.button("Show Weekly Report (by Week)"):
        report = next(
            (e['report'] for e in sample_data if
             e['name'] == selected_name and e['project'] == selected_project and e['week'] == selected_week),
            "No report found."
        )
        st.markdown(f"**Report for {selected_name}, {selected_project}, Week {selected_week}:**")
        st.info(report)
else:
    st.warning("No week data available for this selection.")

# --- Calendar date range picker ---
st.write("---")
st.write("Or select a date range to see reports:")

dates = get_dates_for_name_project(selected_name, selected_project)
if dates:
    start_date = min(dates)
    end_date = max(dates)
    user_start_date, user_end_date = st.date_input(
        "Select Start and End Date",
        value=[start_date, end_date],
        min_value=start_date, max_value=end_date
    )

    if st.button("Show Weekly Reports (by Date Range)"):
        filtered = [
            e for e in sample_data
            if e['name'] == selected_name and
               e['project'] == selected_project and
               user_start_date <= e['date'] <= user_end_date
        ]
        if filtered:
            for entry in filtered:
                st.markdown(f"- **Week {entry['week']} ({entry['date'].isoformat()}):** {entry['report']}")
        else:
            st.info("No reports found in this date range.")
else:
    st.warning("No date data available for this selection.")

