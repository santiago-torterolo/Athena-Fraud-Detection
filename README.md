# 🛡️ Athena Fraud Detection Engine

> **Live Demo:** [🚀 Launch App](https://athena-fraud-detection-u5.streamlit.app/)

A hybrid Fraud Detection System designed to identify **Account Takeover (ATO)** and high-risk transactions in real-time. This project bridges the gap between traditional rule-based logic and Machine Learning.

---

### 🧠 The Problem
In modern fintech, static rules are not enough. Fraudsters use sophisticated techniques like:
- **Device Spoofing:** Mimicking legitimate user devices.
- **Velocity Attacks:** High-frequency transactions from new IPs.
- **Identity Swapping:** Using valid credentials on unknown networks.

### 💡 The Solution: Athena Engine
Athena uses a **XGBoost** model trained on a synthetic dataset mirroring **IEEE-CIS** patterns, enhanced with a **Behavioral Layer** that analyzes device fingerprints and user velocity.

### 📐 System Architecture
![Athena Architecture Diagram](https://github.com/santiago-torterolo/Athena-Fraud-Detection/blob/main/architecture_diagram.png)

#### Key Features
1.  **ML Core:** Gradient Boosting model optimized for imbalanced datasets (Fraud < 1%).
2.  **Simulation Mode:** Capable of running real-time inference on new transaction data.
3.  **Real-Time Dashboard:** A Streamlit interface for analysts to test transactions manually.

---

### 🛠️ Tech Stack
| Component | Technology | Use Case |
| :--- | :--- | :--- |
| **Model** | `XGBoost` | High-performance fraud classification |
| **Data Processing** | `Pandas` / `NumPy` | Feature Engineering (Device & Velocity) |
| **Explainability** | `SHAP` | White-box analysis for compliance |
| **Frontend** | `Streamlit` | Analyst Dashboard |
| **Deployment** | `Streamlit Cloud` | Hosting |

---

### 📂 Project Structure
Athena-Fraud-Detection/
├── .streamlit/ # UI Configuration (Dark Mode)
├── models/ # Trained XGBoost Model (.json)
├── src/
│ ├── preprocessing.py # Device & Identity cleaning logic
│ └── init.py # Package initialization
├── app.py # Main Dashboard application
├── requirements.txt # Python dependencies
└── README.md # Documentation


### 🚀 How to Run Locally

1. **Clone the repository**
git clone https://github.com/santiago-torterolo/Athena-Fraud-Detection.git
cd Athena-Fraud-Detection


2. **Install dependencies**
pip install -r requirements.txt


3. **Run the App**
streamlit run app.py


---

### 📊 Model Performance (v1.0)
*Metrics based on validation set (20% split)*
- **ROC-AUC:** 0.94
- **Recall (Fraud):** 78% (Optimized to catch fraud)
- **Precision:** 85% (Optimized to reduce false positives)

---

**Author:** [Santiago Torterolo](https://www.linkedin.com/in/santiago-torterolo-5u)
