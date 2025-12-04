# PharmaSync AI  
### Intelligent Medication Timing Optimization Tool  
*A behavioral-pattern AI project for the HealthTech Innovators Hackathon 2025*

---

## 🌟 Overview

PharmaSync AI is a lightweight, behavior-driven tool that analyzes **when users actually attempt to take their medication** and uses Machine Learning to recommend the **best one-hour window** where they are most likely to remember.

Instead of focusing on dosage or diagnosis, PharmaSync AI focuses strictly on **habit patterns** — giving users a personalized, data-driven adherence schedule.

---

## 🚀 Key Features

### 🧠 Smart ML Window Prediction  
- Dynamic KMeans clustering (1–3 clusters depending on data size)  
- Automatically selects the strongest adherence pattern  
- Returns:
  - Best time window to take medication  
  - One-hour optimized window  
  - Confidence score (%)  

### ✍️ Manual Habit Entry (No CSV Required)  
Users can enter:
- Time attempted  
- Success or missed  
Data updates live inside the app.

### 📊 Real-Time Visual Analytics  
- **Success Rate by Time of Day**  
- **Raw Attempts Scatter Plot**  
- Highlights high-adherence vs low-adherence time ranges.

### 📈 Confidence Score  
Shows how dependable the AI’s recommendation is based on pattern strength.

### 📤 CSV Export  
All entered data can be downloaded for reuse or analysis.

---

## 🧠 How It Works

1. **User records daily attempts** (time + success).  
2. **ML engine converts time → minutes** for clustering.  
3. **Dynamic clustering**:
   - If successes = 1 → simple rule model  
   - If successes = 2 → k = 1 or 2  
   - If successes ≥ 3 → k = 1, 2, 3  
4. The model selects the cluster with the **highest success density**.  
5. Produces the **optimal 1-hour window** + **confidence score**.  

---

## 🔧 Tech Stack

- Python  
- Streamlit  
- Pandas  
- Seaborn  
- Matplotlib  
- Scikit-learn  

---
---

## 📁 Project Structure

```
PharmaSync-AI/
│── app.py                 # Streamlit UI
│── pharmasync_model.py    # ML clustering engine
│── requirements.txt       # Dependencies
│── README.md              # Documentation
│── habit_data.csv (optional)
```

---


## 🌱 Future Enhancements

- Multi-user behavior profiles  
- Weekday vs weekend adherence modeling  
- Personalized reminder engine  
- Behavior drift detection  
- Mobile UI version  

---

## 👤 Author  
Devi Manoharan
Enterprise Quality Engineering Specialist  
FOE Portfolio Project  
PharmaSync AI – HealthTech Innovators Hackathon 2025 Submission  