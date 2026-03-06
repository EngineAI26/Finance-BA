"""
data_generator.py
Generates realistic India BFSI financial data for analysis.
"""

import pandas as pd
import numpy as np
import os

np.random.seed(42)

months = ['Apr-24','May-24','Jun-24','Jul-24','Aug-24','Sep-24',
          'Oct-24','Nov-24','Dec-24','Jan-25','Feb-25','Mar-25']

# ── Monthly P&L Data ─────────────────────────────────────────
actual_rev    = [620,680,710,740,760,800,820,780,850,870,920,910]
budget_rev    = [640,660,700,720,750,780,800,800,820,850,880,900]
actual_cost   = [310,330,345,355,360,375,382,370,398,405,428,420]
budget_cost   = [320,330,340,350,360,370,380,380,390,400,420,415]

pl_df = pd.DataFrame({
    'Month'        : months,
    'Actual_Rev'   : actual_rev,
    'Budget_Rev'   : budget_rev,
    'Actual_Cost'  : actual_cost,
    'Budget_Cost'  : budget_cost,
    'Actual_EBITDA': [r - c for r, c in zip(actual_rev, actual_cost)],
    'Budget_EBITDA': [r - c for r, c in zip(budget_rev, budget_cost)],
})
pl_df['Rev_Variance'] = pl_df['Actual_Rev'] - pl_df['Budget_Rev']
pl_df['Rev_Var_Pct']  = (pl_df['Rev_Variance'] / pl_df['Budget_Rev'] * 100).round(1)
pl_df['EBITDA_Margin_Pct'] = (pl_df['Actual_EBITDA'] / pl_df['Actual_Rev'] * 100).round(1)

# ── Segment Revenue ──────────────────────────────────────────
segments = ['Retail Banking','Corporate Loans','Wealth Mgmt','Insurance','Digital Finance']
seg_rev  = [2840, 2210, 1460, 1120, 830]
seg_prev = [2540, 2090, 1280, 1000, 620]

seg_df = pd.DataFrame({
    'Segment'    : segments,
    'FY25_Rev'   : seg_rev,
    'FY24_Rev'   : seg_prev,
    'YoY_Growth' : [round((c-p)/p*100,1) for c,p in zip(seg_rev,seg_prev)]
})
seg_df['Share_Pct'] = (seg_df['FY25_Rev'] / seg_df['FY25_Rev'].sum() * 100).round(1)

# ── Budget Variance Line Items ───────────────────────────────
line_items = ['Total Revenue','Personnel Exp.','Technology','Marketing',
              'Compliance','Admin & Facilities','EBITDA','Net Profit']
budget_vals = [4000,1200, 800, 500, 350, 400, 900, 650]
actual_vals = [4321,1340, 745, 470, 362, 380,1004, 721]

var_df = pd.DataFrame({
    'Line_Item'  : line_items,
    'Budget_Cr'  : [v/100 for v in budget_vals],
    'Actual_Cr'  : [v/100 for v in actual_vals],
})
var_df['Variance'] = (var_df['Actual_Cr'] - var_df['Budget_Cr']).round(2)
var_df['Var_Pct']  = ((var_df['Variance'] / var_df['Budget_Cr']) * 100).round(1)

# ── Forecast Scenarios ───────────────────────────────────────
fcast_months = ['Apr-25','May-25','Jun-25','Jul-25','Aug-25','Sep-25',
                'Oct-25','Nov-25','Dec-25','Jan-26','Feb-26','Mar-26']
fcast_df = pd.DataFrame({
    'Month'     : fcast_months,
    'Best_Case' : [920,960,995,1020,1050,1080,1110,1090,1130,1160,1200,1220],
    'Base_Case' : [880,910,940, 965, 990,1010,1030,1010,1050,1070,1100,1110],
    'Worst_Case': [820,840,860, 880, 900, 910, 920, 905, 930, 945, 960, 970],
})

# Save to CSV
os.makedirs('data', exist_ok=True)
pl_df.to_csv('data/monthly_pl.csv', index=False)
seg_df.to_csv('data/segment_revenue.csv', index=False)
var_df.to_csv('data/budget_variance.csv', index=False)
fcast_df.to_csv('data/forecast_scenarios.csv', index=False)

print("✅ Data files generated:")
for f in ['monthly_pl.csv','segment_revenue.csv','budget_variance.csv','forecast_scenarios.csv']:
    print(f"   data/{f}")
