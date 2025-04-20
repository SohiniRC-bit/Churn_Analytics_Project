create database CHURN_ANALYSIS_DB;
-- View the table structure
DESCRIBE TABLE TELCO_CLEANED;
-- Check the first few rows
SELECT * FROM TELCO_CLEANED LIMIT 10;
-- Count total rows
SELECT COUNT(*) AS total_customers FROM TELCO_CLEANED;

-- Overall Churn Rate
SELECT 
  COUNT(*) AS total_customers,
  SUM(CASE WHEN churn = 1 THEN 1 ELSE 0 END) AS churned_customers,
  ROUND(100.0 * SUM(CASE WHEN churn = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_percent
FROM TELCO_CLEANED;

--Churn Rate By Gender
SELECT 
  gender,
  COUNT(*) AS total,
  SUM(CASE WHEN churn = 1 THEN 1 ELSE 0 END) AS churned,
  ROUND(100.0 * SUM(CASE WHEN churn = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_percent
FROM TELCO_CLEANED
GROUP BY gender;

--Churn By Contract Type
SELECT 
  contract,
  COUNT(*) AS total_customers,
  SUM(CASE WHEN churn = 1 THEN 1 ELSE 0 END) AS churned,
  ROUND(100.0 * SUM(CASE WHEN churn = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_percent
FROM TELCO_CLEANED
GROUP BY contract;

--Monthly Charges vs Churn
SELECT 
  churn,
  ROUND(AVG(monthlycharges), 2) AS avg_monthly_charges
FROM TELCO_CLEANED
GROUP BY churn;
