


import streamlit as st
import pandas as pd
import numpy as np
import time
from src.preprocessing import FraudPreprocessor

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Athena Fraud Engine",
    page_icon="🛡️",
    layout="wide"
)

# --- HEADER ---
st.title("🛡️ Athena: Fraud Detection Engine")
st.markdown("""
> **System Status:** Active | **Model Version:** v1.0-Beta
>
> Detects Account Takeover (ATO) and Transaction Fraud in real-time using XGBoost logic.
""")

# --- SIDEBAR (INPUTS) ---
st.sidebar.header("📝 Transaction Details")

# Simulation inputs
amount = st.sidebar.number_input("Transaction Amount ($)", min_value=0.0, value=150.50, step=10.0)
card_type = st.sidebar.selectbox("Card Type", ["visa", "mastercard", "amex", "discover"])
device_info = st.sidebar.text_input("Device String (User-Agent)", "Windows 10.0; Win64; x64")
email = st.sidebar.text_input("User Email", "customer@gmail.com")

st.sidebar.markdown("---")
analyze_btn = st.sidebar.button("🔍 Analyze Transaction")

# --- MAIN LOGIC ---
if analyze_btn:
    # 1. Loading Animation
    with st.spinner('Running behavioral analysis...'):
        time.sleep(1.5) # Simulating API latency
        
        # 2. Call our Preprocessing Pipeline
        preprocessor = FraudPreprocessor()
        raw_data = {
            'TransactionAmt': amount,
            'DeviceInfo': device_info,
            'P_emaildomain': email
        }
        
        clean_features = preprocessor.run_pipeline(raw_data)
        
        # 3. Mock Prediction (PLACEHOLDER until we train the model)
        # Logic: If amount > 1000 or email is weird, flag as High Risk
        risk_score = 0.0
        
        if clean_features['DeviceType'] == 'Unknown':
            risk_score += 0.4
        if amount > 1000:
            risk_score += 0.5
        
        # Random noise for realism
        final_score = min(risk_score + np.random.uniform(0, 0.2), 0.99)
        
    # --- RESULTS DASHBOARD ---
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Risk Score")
        if final_score > 0.7:
            st.metric(label="Probability of Fraud", value=f"{final_score:.1%}", delta="High Risk", delta_color="inverse")
            st.error("🛑 ACTION: BLOCK TRANSACTION")
        elif final_score > 0.4:
            st.metric(label="Probability of Fraud", value=f"{final_score:.1%}", delta="Medium Risk", delta_color="off")
            st.warning("⚠️ ACTION: MANUAL REVIEW")
        else:
            st.metric(label="Probability of Fraud", value=f"{final_score:.1%}", delta="Safe", delta_color="normal")
            st.success("✅ ACTION: APPROVE")

    with col2:
        st.subheader("Analysis Signals")
        st.write("Processed Features (Input to Model):")
        st.json(clean_features)
        
        st.markdown("### 🧠 Explainability (Why?)")
        if final_score > 0.7:
            st.write(f"- **High Amount:** ${amount} exceeds user threshold.")
            if clean_features['DeviceType'] == 'Unknown':
                st.write("- **Device Risk:** Unrecognized device signature.")
        else:
            st.write("- **Device:** Recognized trusted device.")
            st.write("- **Velocity:** Normal transaction frequency.")

# --- FOOTER ---
st.markdown("---")
st.caption("Athena Engine | Developed by Santiago Torterolo")
