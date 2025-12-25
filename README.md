# 🛡️ Athena Fraud Detection Engine

> **Live Demo:** [Click here to launch the App](https://share.streamlit.io/) *(Link pending deployment)*

A hybrid Fraud Detection System designed to identify **Account Takeover (ATO)** and high-risk transactions in real-time. This project bridges the gap between traditional rule-based logic and Machine Learning.

---

### 🧠 The Problem
In modern fintech, static rules are not enough. Fraudsters use sophisticated techniques like:
- **Device Spoofing:** Mimicking legitimate user devices.
- **Velocity Attacks:** High-frequency transactions from new IPs.
- **Identity Swapping:** Using valid credentials on unknown networks.

### 💡 The Solution: Athena Engine
Athena uses a **XGBoost** model trained on the IEEE-CIS Fraud Detection dataset, enhanced with a **Behavioral Layer** that analyzes device fingerprints and user velocity.

#### Key Features
1.  **ML Core:** Gradient Boosting model optimized for imbalanced datasets (Fraud < 1%).
2.  **Explainability:** Integrated **SHAP** values to explain *why* a transaction was blocked (essential for Risk Analysts).
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
