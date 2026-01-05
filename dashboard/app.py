import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Credit Risk & Fraud Dashboard", layout="wide")
st.title("Credit Risk & Fraud Early-Warning System")

# -------------------------
# Path handling (IMPORTANT)
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Load data safely
users = pd.read_csv(DATA_DIR / "users.csv")
repayments = pd.read_csv(DATA_DIR / "repayments.csv")
risk_users = pd.read_csv(DATA_DIR / "risk_scored_users.csv")

# -------------------------
# Risk Distribution
# -------------------------
st.header("Risk Segment Distribution")

risk_dist = risk_users["risk_segment"].value_counts(normalize=True) * 100
st.bar_chart(risk_dist)

# -------------------------
# Defaults by Risk Segment
# -------------------------
st.header("Defaults by Risk Segment")

merged = repayments.merge(
    risk_users[["user_id", "risk_segment"]],
    on="user_id",
    how="left"
)

defaults = (
    merged[merged["repayment_status"] == "default"]
    .groupby("risk_segment")
    .size()
)

st.bar_chart(defaults)

# -------------------------
# Policy Impact Simulation
# -------------------------
st.header("Policy Impact Simulation")

baseline_defaults = (repayments["repayment_status"] == "default").sum()

high_risk_defaults = (
    merged[
        (merged["repayment_status"] == "default") &
        (merged["risk_segment"] == "High")
    ].shape[0]
)

preventable = int(high_risk_defaults * 0.6)
post_policy = baseline_defaults - preventable

st.metric("Baseline Defaults", baseline_defaults)
st.metric("Post-Policy Defaults (Simulated)", post_policy)
st.metric(
    "Estimated Reduction (%)",
    round((preventable / baseline_defaults) * 100, 2) if baseline_defaults > 0 else 0
)
