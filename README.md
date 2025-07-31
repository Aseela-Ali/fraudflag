# 🚩 FraudFlag – Lightweight Fraud Detection Dashboard

FraudFlag is a proof-of-concept anomaly detection app developed to explore fraud identification in e-commerce and public sector-inspired datasets. Built using **Streamlit**, the tool allows users to upload transactional data (CSV), apply rule-based checks, and instantly visualise flagged anomalies.

This open-source project is inspired by an internal AI-powered fraud tool I developed at **Hardedge Ltd.** using large language models (LLMs) for anomaly and root-cause detection. Due to confidentiality and computational cost, this public demo replicates the logic using **rule-based heuristics** and **open datasets**.

🔗 **GitHub Repo**: https://github.com/Aseela-Ali/fraudflag

---

## 🧩 Features

- 📥 Upload your own CSV transaction file
- 🚩 Automatically flag:
  - Orders above configurable high-value thresholds
  - Customers with frequent order activity
- 📊 Real-time metrics and dashboards
- 📤 Download flagged entries as CSV

---

## 🖼️ Screenshots

### Dataset Overview
![Dataset Overview](screenshots/Screenshot%202025-07-31%20205005.png)

### Flagged Orders View
![Flagged Orders](screenshots/Screenshot%202025-07-31%20204921.png)

---

## ⚙️ Tech Stack

- **Streamlit** – for interactive web UI
- **Python** – core logic
- **Pandas** – data analysis
- **Faker** – for generating sample datasets

---

## 📂 Example Input Format

| Order_ID | Order_Amount | Orders_Last_Month | Customer_Name | Email              |
|----------|--------------|-------------------|----------------|---------------------|
| 1001     | 2,500.00     | 5                 | John Smith     | john@example.com    |

Flagging logic:
- If `Order_Amount > £1500` OR `Orders_Last_Month > 4` → mark as suspicious

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/Aseela-Ali/fraudflag.git
cd fraudflag
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔭 Future Enhancements

- Integrate actual ML models (Isolation Forest, LLM-based logic)
- Add user-defined thresholds and filters
- Docker deployment & API integration
- Live dashboard with Streamlit Cloud or HuggingFace Spaces

---

## 👤 Author

**Aseela Ali**  
PhD Researcher | Web Developer | AI for Cloud Observability  
🔗 [LinkedIn](https://www.linkedin.com/in/aseela-ali/)

---

> ⚠️ This app is for demonstration purposes only and not intended for production use.
