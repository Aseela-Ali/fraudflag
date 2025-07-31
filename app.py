import streamlit as st
import pandas as pd

st.set_page_config(page_title="FraudFlag - Order Anomaly Detector", layout="wide")

st.title("🚩 FraudFlag: Internal Order Anomaly Detector")
st.markdown("""
A lightweight dashboard developed for internal use at Hardedge Ltd. to flag and review potentially fraudulent or suspicious orders.
""")

# Upload or load default dataset
uploaded_file = st.file_uploader("Upload your order data CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("fraudflag_orders.csv")  # Use sample if none uploaded

# Display basic info
st.subheader("📊 Dataset Overview")
st.write(df.head())

# Summary stats
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Orders", len(df))
with col2:
    st.metric("Flagged Orders", df['Is_Flagged'].sum())
with col3:
    avg_order = round(df['Order_Amount'].mean(), 2)
    st.metric("Avg. Order Amount", f"£{avg_order}")

# Show flagged orders
st.markdown("---")
st.subheader("🚨 Flagged Orders")
flagged_df = df[df['Is_Flagged'] == 1]
st.dataframe(flagged_df, use_container_width=True)

# Optional download
st.markdown("---")
st.download_button(
    label="Download Flagged Orders CSV",
    data=flagged_df.to_csv(index=False).encode('utf-8'),
    file_name='flagged_orders.csv',
    mime='text/csv'
)

st.markdown("---")
st.caption("© 2025 Hardedge Ltd. Internal Use Only")
