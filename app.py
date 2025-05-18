import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfNVkHyvXMaKjB65CSJKu1XD6dg0nsiFDaa3HShnuyDw7Ba3w/formResponse"
MOOD_ENTRY_FIELD = "entry.1853127787"
NOTE_ENTRY_FIELD = "entry.126102288"
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTEa9wvpHiAVYG-tJnc2apb3RCKDjlQOps5Cli9je39GO5dbAUxBfls9oXpSZM8y9t1o-uIPMkO5T9J/pub?gid=1201132299&single=true&output=csv"
MOODS = {
    "😊 Happy": "😊 Happy",
    "😠 Angry": "😠 Angry",
    "😕 Confused": "😕 Confused",
    "🎉 Excited": "🎉 Excited",
    "😐 Neutral": "😐 Neutral"
}

st.set_page_config(page_title="Mood of the Queue")
st.title("Mood of the Queue")

with st.form("mood_form"):
    mood = st.selectbox("How's the vibe?", list(MOODS.keys()))
    note = st.text_input("Optional note:")
    submitted = st.form_submit_button("Log Mood")
    if submitted:
        data = {
            MOOD_ENTRY_FIELD: MOODS[mood],
            NOTE_ENTRY_FIELD: note
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(FORM_URL, data=data, headers=headers)
        if response.status_code in [200, 302]:
            st.toast("Mood logged successfully 🎉", icon="✅")
            st.rerun()
        else:
            st.warning("Something went wrong while submitting.")

st_autorefresh(interval=30 * 1000, key="chartrefresh")

try:
    df = pd.read_csv(SHEET_CSV_URL)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df.rename(columns={"What’s the mood?": "Mood", "Add a note": "Note"})

    selected_date = st.date_input("Filter by date", value=datetime.today())
    filtered_df = df[df['Timestamp'].dt.date == selected_date]

    if not filtered_df.empty:
        mood_counts = filtered_df["Mood"].value_counts().reset_index()
        mood_counts.columns = ['Mood', 'Count']
        fig = px.bar(mood_counts, x='Mood', y='Count', title=f"Mood Chart for {selected_date}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No mood logs for this date yet.")

except Exception as e:
    st.error("Failed to load mood data.")
    st.exception(e)
