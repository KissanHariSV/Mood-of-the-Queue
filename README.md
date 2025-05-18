# Mood of the Queue

A quick internal tool built with **Streamlit** to track and visualize the emotional state of a support queue throughout the day. This app lets users log a mood, leave a note, and instantly see trends on a chart.

---

## 🚀 Features

- Emoji-based mood logging via Streamlit UI
- Optional notes for context
- Data submission to a Google Sheet via Google Forms
- Auto-refreshing chart every 30 seconds
- Filter mood trends by date

---

## 🛠 Tech Stack

- Python
- Streamlit
- Plotly
- Google Forms + Google Sheets (CSV published)

---

## 📦 Setup

### 1. Install dependencies

```bash
streamlit run app.py
```

## 📊 Output

- Logged moods are stored in a Google Sheet.
- A real-time bar chart shows the mood breakdown for the selected day.
- New entries trigger an immediate refresh of the chart.

---

## 🔗 Live Demo & Data

- **🌐 Streamlit App**: [mood-of-the-queue.streamlit.app]([https://mood-of-the-queue.streamlit.app](https://mood-of-the-queue-hdyzpmytwyb3azlwe2yqch.streamlit.app/))
- **📄 Google Sheet (Responses)**: [View Sheet](https://docs.google.com/spreadsheets/d/1Gl3FAgqE4HNFAuqH-Ve_XFmBUJzyqPA6JOqHwc763iA/edit?usp=sharing)
