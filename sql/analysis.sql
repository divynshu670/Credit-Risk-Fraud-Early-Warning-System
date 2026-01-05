-- 1. Cohort default analysis
SELECT
  DATE_TRUNC('month', signup_date) AS signup_month,
  COUNT(DISTINCT u.user_id) AS users,
  AVG(CASE WHEN r.repayment_status = 'default' THEN 1 ELSE 0 END) AS default_rate
FROM users u
LEFT JOIN repayments r ON u.user_id = r.user_id
GROUP BY signup_month
ORDER BY signup_month;

-- 2. Default rate by merchant category
SELECT
  t.merchant_category,
  COUNT(*) AS txn_count,
  AVG(CASE WHEN r.repayment_status = 'default' THEN 1 ELSE 0 END) AS default_rate
FROM transactions t
JOIN repayments r ON t.user_id = r.user_id
GROUP BY t.merchant_category
ORDER BY default_rate DESC;

-- 3. Night transaction fraud proxy
SELECT
  EXTRACT(HOUR FROM transaction_time) AS hour,
  COUNT(*) AS txns
FROM transactions
GROUP BY hour
ORDER BY hour;

-- 4. High exposure users
SELECT
  u.user_id,
  u.credit_limit,
  COUNT(t.transaction_id) AS txn_count,
  SUM(t.amount) AS total_spend
FROM users u
JOIN transactions t ON u.user_id = t.user_id
GROUP BY u.user_id, u.credit_limit
ORDER BY total_spend DESC;
