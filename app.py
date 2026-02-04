import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Page Config
st.set_page_config(
    page_title = "Smart Demand Forecasting and Dynamic Pricing",
    layout = "centered"
)

st.title("📈 Smart Demand Forecasting & Dynamic Pricing")
st.write("AI-based system to predict demand and recommend optimal pricing")

# Load Model
model = joblib.load("model\demand_forecasting_model.pkl")

# User Inputs
st.header("🔢 Input Parameters")

price = st.number_input("Product price", min_value=100, max_value=5000, value=1000)
discount = st.slider("Discount (%)", 0, 50, 10)
day = st.slider("Day of Month", 1, 31, 15)
weekday = st.slider("Weekday (0=Mon, 6=Sun)", 0, 6, 2)
month = st.slider("Month", 1, 12, 6)

lag_7 = st.number_input("Last 7-day Demand", value=80)
rolling_14 = st.number_input("14-day Average Demand", value=85)

# Predict Button 
if st.button("🔮 Predict Demand & Price"):
    input_df = pd.DataFrame([{
        "price": price,
        "discount": discount,
        "day": day,
        "month": month,
        "lag_7": lag_7,
        "rolling_14": rolling_14
    }])

    predicted_demand = model.predict(input_df)[0]

    # Pricing Logic
    if predicted_demand > 120:
        recommended_price = price * 1.10
        strategy = "Increase Price 📈"
    elif predicted_demand < 60:
        recommended_price = price * 0.90
        strategy = "Decrease Price 📉"
    else:
        recommended_price = price
        strategy = "Maintain Price ⚖️"

    st.success(f"📦 Predicted Demand:, {int(predicted_demand)}, units")
    st.info(f"💡 Pricing Strategy:, {strategy}")
    st.warning(f"Recommend Price: ₹{recommended_price:.2f}")










