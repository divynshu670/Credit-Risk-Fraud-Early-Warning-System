# Credit Risk & Fraud Early-Warning System (UPI Credit)

This project simulates an internal analytics initiative for a consumer fintech company
to proactively identify credit risk and fraud signals in UPI-based credit products.

The objective is not to build a production ML system, but to demonstrate how
**SQL- and Python-driven analytics** can support **real business decisions**
around credit approvals, monitoring, and risk controls.

---

## Business Context

UPI-based credit products are designed to offer fast and seamless access to credit.
As usage scales, the business faces a fundamental trade-off:

- Drive growth through higher approvals and usage  
- Control credit defaults and fraud losses to protect unit economics  

Risk detection is often reactive, with losses observed only after defaults or fraud occur.
This project explores how **early behavioral and repayment signals**
can be used to support **proactive, data-driven risk decisions**.

---

## Problem Statement

How can the business:

- Identify high-risk users and transactions early  
- Reduce credit defaults and fraud losses  
- Without significantly impacting user growth or approval rates?

---

## Dataset Overview

The analysis is built on three core datasets:

### `users.csv`
User-level attributes used for segmentation and exposure analysis.
- user_id  
- signup_date  
- city  
- age_band  
- employment_type  
- credit_limit  
- kyc_status  

### `transactions.csv`
UPI credit transaction behavior used to derive early risk signals.
- transaction_id  
- user_id  
- amount  
- merchant_category  
- transaction_time  
- device_id  
- location_city  
- payment_type  

### `repayments.csv`
Credit outcome data used to evaluate repayment behavior.
- user_id  
- billing_cycle  
- due_date  
- repayment_date  
- repayment_status  
- outstanding_amount  

> Fraud flags are **not pre-stored**.  
> They are intended to be **derived dynamically from behavior**, reflecting how real systems operate.

---

## Analytical Approach

### 1. Feature Engineering (Python)
Interpretable features were derived from transaction and repayment behavior, including:
- Transaction frequency and spend patterns  
- Night-time transaction ratio  
- Repayment delays and default counts  

The focus was on **explainability**, not black-box modeling.

---

### 2. Risk Segmentation
Users were segmented into **Low**, **Medium**, and **High** risk buckets
based on a weighted combination of behavioral and repayment signals.

This segmentation enables **targeted actions** rather than one-size-fits-all rules.

---

### 3. Impact Simulation
Instead of relying only on historical losses, the project simulates
**preventable defaults** under hypothetical policy actions, such as:

- Restricting or manually reviewing High-risk users  
- Applying transaction limits to Medium-risk users  

This allows risk strategies to be evaluated **before implementation**.

---

### 4. SQL Analysis
SQL was used for:
- Exploratory analysis  
- Cohort and aggregation checks  
- Cross-validation of Python findings  

Python was used for feature engineering and simulation,
while SQL supported **relational reasoning and validation**.

---

## Key Insights (High-Level)

- Risk is **concentrated**: a smaller subset of users contributes disproportionately to defaults.  
- Behavioral signals (such as night-time usage and repayment delays) act as **early indicators of stress**.  
- Evaluating policies based on **preventable loss**, rather than historical loss alone,
  provides more realistic estimates of business impact.

---

## Decision Framework

Based on the analysis, risk actions can be framed as:

| Risk Segment | Suggested Action |
|-------------|------------------|
| Low Risk | Standard approvals and monitoring |
| Medium Risk | Usage monitoring and transaction caps |
| High Risk | Restriction or manual review |

---

## Outputs

- Interpretable risk-segmented user dataset  
- Policy impact simulation results  
- Executive-ready decision memo  
- Streamlit dashboard (visualizing risk distribution and impact)

---

## What This Project Demonstrates

- Breaking down ambiguous business problems into analyzable components  
- Designing clean, realistic data schemas  
- Applying SQL and Python in complementary roles  
- Translating analysis into **clear, defensible recommendations**  

This mirrors how analytics work is executed inside modern fintech teams such as
:contentReference[oaicite:0]{index=0}.

---

## Limitations & Next Steps

- Synthetic data may not capture all real-world edge cases  
- Risk thresholds require calibration with live data  
- Future work could include real-time monitoring and feedback loops  

---

## Disclaimer

This project is a simulation created for learning and demonstration purposes.
All data is synthetic, and no real user information is used.
