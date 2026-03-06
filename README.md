# FinAnalytica — Finance Business Analysis (Python)

> Business Analysis portfolio project for India's BFSI/Finance sector using **Python, Pandas & Matplotlib**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualisation-orange?style=for-the-badge)
![Domain](https://img.shields.io/badge/Domain-BFSI%20Finance-gold?style=for-the-badge)

---

## 📊 Project Overview

A complete Financial Business Analysis pipeline using Python — from raw data to charts and KPI reports. Covers all key BA skills used in India's banking, financial services & insurance sector.

---

## 🗂 Project Structure

```
finance-ba-python/
├── data_generator.py       # Generates all sample financial data (CSV)
├── finance_analysis.py     # Core analysis: Pandas + 6 Matplotlib charts
├── data/
│   ├── monthly_pl.csv          # Monthly P&L: actuals vs budget
│   ├── segment_revenue.csv     # Revenue by business segment
│   ├── budget_variance.csv     # Line-item variance table
│   └── forecast_scenarios.csv  # FY26 best/base/worst case
├── charts/
│   ├── 01_revenue_vs_budget.png
│   ├── 02_ebitda_trend.png
│   ├── 03_cost_breakdown.png
│   ├── 04_segment_analysis.png
│   ├── 05_variance_waterfall.png
│   └── 06_forecast_scenarios.png
└── outputs/
    ├── kpi_summary.csv
    ├── monthly_pl_analysis.csv
    ├── variance_analysis.csv
    └── segment_analysis.csv
```

---

## 📈 Analyses Performed

| # | Analysis | Technique | Chart Type |
|---|---|---|---|
| 1 | Revenue vs Budget Trend | Variance highlighting | Line + fill |
| 2 | EBITDA Margin Trend | Time-series + benchmark | Dual-axis line/bar |
| 3 | Cost Breakdown | Proportional analysis | Donut chart |
| 4 | Segment Revenue & Growth | YoY comparison | Grouped bar + horizontal bar |
| 5 | Budget Variance Waterfall | Fav/Adverse classification | Variance bar chart |
| 6 | 3-Scenario Forecast | Scenario analysis | Multi-line with range |

---

## 💼 BA Skills Demonstrated

- **Variance Analysis** — Favourable/Adverse with driver commentary
- **Financial KPI Design** — EBITDA, ROE, Current Ratio, Margin %
- **Segment Reporting** — Revenue contribution by business unit
- **Trend Analysis** — Monthly actuals vs budget with annotations
- **Scenario Planning** — Best / Base / Worst case modelling
- **Data Wrangling** — Pandas for financial data transformation
- **Stakeholder-ready charts** — Publication-quality Matplotlib visuals

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/finance-ba-python.git
cd finance-ba-python
```

### 2. Install dependencies
```bash
pip install pandas matplotlib seaborn openpyxl
```

### 3. Generate data & run analysis
```bash
python data_generator.py     # Creates CSV files in /data
python finance_analysis.py   # Runs analysis, saves charts + outputs
```

All 6 charts will appear in `/charts/` and CSV reports in `/outputs/`.

---

## 🚀 Deploy to GitHub

```bash
git init
git add .
git commit -m "Finance BA Analysis — Python Portfolio Project"
git remote add origin https://github.com/YOUR_USERNAME/finance-ba-python.git
git branch -M main
git push -u origin main
```

---

## 🎯 Target Job Roles (India)

- Business Analyst — BFSI / FinTech
- Financial Analyst
- MIS & Reporting Analyst
- Data Analyst — Banking & Finance
- Management Consultant (Finance Practice)

**Top companies:** HDFC Bank, ICICI Bank, Axis Bank, Bajaj Finserv, Paytm, PhonePe, Razorpay, Deloitte, EY, KPMG, TCS BFSI, Infosys BPM, Accenture

---

## 📄 License

MIT — Free to use for your BA portfolio.

---

*Built to demonstrate Python-based Business Analysis skills for India's Finance & BFSI sector.*
