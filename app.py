# ==========================================
# Air Quality & Health Impact Dashboard (UI Only)
# ==========================================

import streamlit as st
import pandas as pd


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Air Quality Health Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Air Quality & Health Impact Dashboard")

st.markdown(
    """
    Interactive dashboard for monitoring **air pollution indicators, environmental conditions,
    and related healthcare metrics**.
    """
)

st.divider()


# ==========================================
# Sidebar Inputs
# ==========================================

st.sidebar.header("⚙️ Enter Environmental Data")

AQI = st.sidebar.number_input("AQI", min_value=0.0, max_value=500.0, value=150.0)

st.sidebar.subheader("Pollution Indicators")

PM10 = st.sidebar.number_input("PM10", min_value=0.0, max_value=300.0, value=80.0)
PM2_5 = st.sidebar.number_input("PM2.5", min_value=0.0, max_value=200.0, value=50.0)
NO2 = st.sidebar.number_input("NO2", min_value=0.0, max_value=200.0, value=60.0)
SO2 = st.sidebar.number_input("SO2", min_value=0.0, max_value=100.0, value=20.0)
O3 = st.sidebar.number_input("O3", min_value=0.0, max_value=300.0, value=100.0)

st.sidebar.subheader("Environmental Conditions")

Temperature = st.sidebar.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
Humidity = st.sidebar.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
WindSpeed = st.sidebar.number_input("Wind Speed", min_value=0.0, max_value=30.0, value=5.0)

st.sidebar.subheader("Healthcare Data")

RespiratoryCases = st.sidebar.number_input("Respiratory Cases", min_value=0, max_value=50, value=5)
CardiovascularCases = st.sidebar.number_input("Cardiovascular Cases", min_value=0, max_value=30, value=3)
HospitalAdmissions = st.sidebar.number_input("Hospital Admissions", min_value=0, max_value=20, value=1)

HealthImpactScore = st.sidebar.number_input("Health Impact Score", min_value=0.0, max_value=100.0, value=90.0)


# ==========================================
# AQI Category Section
# ==========================================

st.header("🌫 Air Quality Index (AQI)")

if AQI <= 50:
    category = "Good"
elif AQI <= 100:
    category = "Moderate"
elif AQI <= 150:
    category = "Unhealthy for Sensitive Groups"
elif AQI <= 200:
    category = "Unhealthy"
elif AQI <= 300:
    category = "Very Unhealthy"
else:
    category = "Hazardous"

col1, col2 = st.columns(2)

with col1:
    st.metric("AQI Value", AQI)

with col2:
    st.write(f"Air Quality Category: **{category}**")

st.divider()


# ==========================================
# Pollution Charts
# ==========================================

st.header("📊 Air Pollution Indicators")

pollution_df = pd.DataFrame({
    "Pollutant": ["PM10", "PM2.5", "NO2", "SO2", "O3"],
    "Value": [PM10, PM2_5, NO2, SO2, O3]
})

st.bar_chart(pollution_df.set_index("Pollutant"))

st.divider()


# ==========================================
# Environmental Conditions
# ==========================================

st.header("🌡 Environmental Conditions")

env_df = pd.DataFrame({
    "Metric": ["Temperature", "Humidity", "Wind Speed"],
    "Value": [Temperature, Humidity, WindSpeed]
})

st.line_chart(env_df.set_index("Metric"))

st.divider()


# ==========================================
# Health Indicators
# ==========================================

st.header("🏥 Health Indicators")

health_df = pd.DataFrame({
    "Indicator": [
        "Respiratory Cases",
        "Cardiovascular Cases",
        "Hospital Admissions"
    ],
    "Value": [
        RespiratoryCases,
        CardiovascularCases,
        HospitalAdmissions
    ]
})

st.bar_chart(health_df.set_index("Indicator"))

st.divider()


# ==========================================
# Health Impact Score Display
# ==========================================

st.header("📉 Health Impact Score")

st.metric("Health Impact Score", HealthImpactScore)

st.divider()


# ==========================================
# Footer
# ==========================================

st.caption(
    """
    Air Quality Monitoring Dashboard  
    Environmental & Health Indicators Visualization  
    Built with **Streamlit**
    """
)
