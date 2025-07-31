# 🚩 FraudFlag – Lightweight Fraud Detection Dashboard

FraudFlag is a proof-of-concept anomaly detection app developed to explore fraud identification in e-commerce and public sector-inspired datasets. Built using **Streamlit**, the tool allows users to upload transactional data (CSV), apply rule-based checks, and instantly visualise flagged anomalies.

This open-source project is inspired by an internal AI-powered tool I developed at **Hardedge Ltd.**, where I used large language models (LLMs) for fraud and root-cause analysis. Due to confidentiality, I cannot share that code — but this version replicates the structure using simulated datasets and transparent rules.

🔗 **Live Demo** (optional if deployed): [link here]  
📁 **GitHub Repo**: https://github.com/Aseela-Ali/fraudflag

---

## 🧩 Features

- Upload your own CSV dataset
- Flag anomalies based on:
  - High order amounts
  - Frequent recent activity
- Summary metrics and dashboards
- Export flagged transactions

---

## 📁 Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Faker** (for synthetic datasets)

---

## 📄 Example Use Case

Upload a file like:

| Order_ID | Order_Amount | Orders_Last_Month | Customer_Name | ... |
|----------|--------------|-------------------|----------------|-----|
| 1001     | £2,500.00     | 5                 | John Smith      | ... |

FraudFlag will flag orders with high values or frequency, and display them in a dashboard for review.

---

## 📌 Future Enhancements

- LLM integration (Isolation Forest / SVM / GPT-powered explanations)
- Scoring model with confidence levels
- Real-time fraud stream (Kafka / REST API)
- Docker deployment

---

## 👤 Author

**Aseela Ali**  
PhD Researcher in Cloud Computing | Web Developer | AI for Public Sector  
📧 [a.s.b.ali@keele.ac.uk](mailto:a.s.b.ali@keele.ac.uk)  
🔗 [LinkedIn](https://www.linkedin.com/in/aseelaali)

---

> ⚠️ This project is for demonstration purposes and not production-ready.
