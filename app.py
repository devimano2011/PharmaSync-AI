import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from pharmasync_model import find_best_window

# ------------------------------------
# Initialize session state FIRST
# ------------------------------------
if "user_data" not in st.session_state:
    st.session_state.user_data = []

# ------------------------------------
# Page Title
# ------------------------------------
st.title("PharmaSync AI")
st.subheader("Medication Timing Optimization Tool")

# ------------------------------------
# User Input Section
# ------------------------------------
st.subheader("Enter Your Habit Data")

with st.form("habit_form"):
    time_input = st.time_input("Time you attempted medication")
    success_input = st.selectbox("Did you remember?", ["Yes", "No"])
    submitted = st.form_submit_button("Add Entry")

if submitted:
    st.session_state.user_data.append({
        "day": "User",  # placeholder for now
        "time": time_input.strftime("%H:%M"),
        "success": 1 if success_input == "Yes" else 0
    })
    st.success("Entry added!")

# ------------------------------------
# Display User Data
# ------------------------------------
st.write("### Current Habit Data")

if len(st.session_state.user_data) > 0:
    df = pd.DataFrame(st.session_state.user_data)

    # Always compute minutes for ML + charts
    df['time_in_minutes'] = df['time'].apply(lambda t: int(t[:2]) * 60 + int(t[3:5]))

    st.dataframe(df)
else:
    st.info("No habit entries yet. Add some above.")

# ------------------------------------
# Prediction Section
# ------------------------------------
st.write("### Run Prediction")

if len(st.session_state.user_data) >= 3:
    result = find_best_window(df)

    if isinstance(result, tuple) and len(result) == 3:
        start, end, confidence = result
        st.success(f"Best Medication Window: **{start} – {end}**")
        st.info(f"Confidence Score: **{confidence}%**")
else:
    st.warning("Add at least 3 habit entries to run prediction.")

# ------------------------------------
# Visualizations Section
# ------------------------------------
if len(st.session_state.user_data) > 0:
    
    # -------- Success Rate by Time of Day --------
    st.write("### Success Rate by Time of Day")

    rate_df = df.groupby('time')['success'].mean().reset_index()
    rate_df['success_percent'] = rate_df['success'] * 100

    fig_rate, ax_rate = plt.subplots()
    sns.barplot(data=rate_df, x='time', y='success_percent', ax=ax_rate)
    ax_rate.set_xlabel("Time of Day")
    ax_rate.set_ylabel("Success Rate (%)")
    ax_rate.set_title("Medication Success Rate by Time of Day")
    st.pyplot(fig_rate)

    # -------- Scatter Plot --------
    st.write("### Success vs Time Scatter Plot")

    fig_sc, ax_sc = plt.subplots()
    colors = df['success'].map({1: 'green', 0: 'red'})
    ax_sc.scatter(df['time_in_minutes'], df['success'], c=colors)
    ax_sc.set_xlabel("Time of Day (minutes from midnight)")
    ax_sc.set_ylabel("Success (1) / Missed (0)")
    ax_sc.set_title("Raw Attempts (Green = Success, Red = Missed)")
    st.pyplot(fig_sc)

# ------------------------------------
# Download Data Button
# ------------------------------------
if len(st.session_state.user_data) > 0:
    csv_data = df.to_csv(index=False).encode()
    st.download_button("Download Habit Data as CSV", csv_data, "habit_data.csv")