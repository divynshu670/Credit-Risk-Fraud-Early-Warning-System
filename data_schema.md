## Core Datasets

### users
- user_id
- signup_date
- city
- age_band
- employment_type
- credit_limit
- kyc_status

### transactions
- transaction_id
- user_id
- amount
- merchant_category
- transaction_time
- device_id
- location_city
- payment_type

### repayments
- user_id
- billing_cycle
- due_date
- repayment_date
- repayment_status
- outstanding_amount

### fraud_flags (derived)
- transaction_id
- fraud_flag
- flag_reason

---

## Design Notes

- Only users, transactions, and repayments are persisted
- Fraud flags are generated dynamically from behavior
- All schemas are intentionally lean and decision-focused
