import streamlit as st
import pandas as pd
from recommendations import get_recommendations

st.set_page_config(page_title="Health Metrics Dashboard", layout="wide")

st.title("🏥 Health Metrics Dashboard")

# Sidebar input
st.sidebar.header("Enter Your Daily Health Data")
heart_rate = st.sidebar.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=75)
steps = st.sidebar.number_input("Steps Taken", min_value=0, value=5000)
sleep_hours = st.sidebar.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0)

# Store data in dataframe
data = {
    "Heart Rate (bpm)": [heart_rate],
    "Steps Taken": [steps],
    "Sleep Hours": [sleep_hours]
}
df = pd.DataFrame(data)

st.subheader("📊 Your Health Data")
st.dataframe(df)

# Recommendations
st.subheader("💡 Recommendations")
recommendations = get_recommendations(heart_rate, steps, sleep_hours)
for rec in recommendations:
    st.write(f"- {rec}")
