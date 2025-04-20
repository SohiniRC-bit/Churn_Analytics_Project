
# 📊 Customer Churn Analysis Project

This end-to-end data analytics project focuses on identifying factors that influence customer churn using Python, Snowflake SQL, and Tableau. It involves data cleaning, EDA, SQL transformations, and visual storytelling through dashboards.

---

## 🚀 Project Overview

**Objective:**  
To analyze customer behavior and identify key factors leading to churn using Telco data, enabling better decision-making for retention strategies.

**Tools & Technologies:**
- 🐍 Python (Pandas, Seaborn, Matplotlib)
- ❄️ Snowflake (Cloud SQL Data Warehouse)
- 📊 Tableau (Dashboard creation)
- 📁 CSV (Data files)

---

## 📁 Folder Structure

```bash
customer-churn-analysis/
│
├── data/
│   └── Telco_cleaned.csv            # Cleaned dataset ready for analysis
│
├── notebooks/
│   └── churn_analysis.ipynb         # Python EDA & preprocessing notebook
│
├── sql/
│   └── churn_queries.sql            # SQL queries executed in Snowflake
│
├── tableau/
│   └── dashboard_link.txt           # Public link to Tableau dashboard
│
├── screenshots/
│   └── tableau_dashboard.png        # Preview of the dashboard
│
└── README.md                        # Project overview and instructions
```

---

## 📌 Steps Followed

### 1. Data Preprocessing (Python)
- Loaded Telco customer data
- Handled null values, fixed data types
- Encoded categorical variables
- Exported cleaned data to `Telco_cleaned.csv`

### 2. Snowflake SQL Layer
- Uploaded cleaned CSV to Snowflake using Web UI
- Created `TELCO_CLEANED` table under `CHURN_ANALYSIS_DB.PUBLIC`
- Executed SQL queries for churn segmentation, tenure buckets, service usage patterns

### 3. Visualization (Tableau)
- Connected Tableau to Snowflake live
- Built KPI cards, bar charts, heatmaps, and filters
- Created an interactive dashboard to explore churn across multiple dimensions

🔗 **Tableau Dashboard:**  
👉 [View it on Tableau Public](https://public.tableau.com/app/profile/sohini.roy.chowdhury/viz/ChurnAnalyticsOverview/Dashboard5)

---

## 📌 Key Business Insights

- Customers with month-to-month contracts are more likely to churn.
- High churn is observed in customers with fiber optic internet.
- Longer tenure generally results in lower churn probability.
- Additional services like OnlineBackup or StreamingTV impact churn trends.

---

## ⚙️ How to Run This Project

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/customer-churn-analysis.git
   ```

2. **Run Python EDA**
   ```bash
   jupyter notebook notebooks/churn_analysis.ipynb
   ```

3. **Upload to Snowflake**
   - Open Snowsight → Load data → Upload `Telco_cleaned.csv`
   - Run queries from `sql/churn_queries.sql`

4. **Open Tableau**
   - Connect to Snowflake → Load `TELCO_CLEANED` table
   - Recreate or explore dashboard visuals

---

## 📈 Future Enhancements

- Build churn prediction model (Logistic Regression / XGBoost)
- Automate Snowflake upload using Python connector
- Deploy a Power BI version of the dashboard
- Add cohort or LTV analysis

---

## 👩‍💻 Author

**Sohini Roy Chowdhury**  
_Data Analyst | Tableau & Python Enthusiast_  
🔗 [LinkedIn](https://www.linkedin.com/in/sohini-roy-chowdhury)
