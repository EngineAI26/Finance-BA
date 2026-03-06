"""
finance_analysis.py
================================================
Finance Business Analysis — India BFSI Sector
Tools: Pandas (data), Matplotlib + Seaborn (charts)

Analyses:
  1. Revenue vs Budget trend + variance
  2. EBITDA margin trend
  3. Cost breakdown (donut)
  4. Segment revenue & YoY growth
  5. Budget variance waterfall
  6. 3-scenario revenue forecast
  7. KPI summary report (printed + CSV)
================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np
import os

# ── Setup ────────────────────────────────────────────────────
os.makedirs('charts', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

# Style
plt.rcParams.update({
    'figure.facecolor' : '#09090f',
    'axes.facecolor'   : '#111118',
    'axes.edgecolor'   : '#2a2a38',
    'axes.labelcolor'  : '#9898b0',
    'xtick.color'      : '#686880',
    'ytick.color'      : '#686880',
    'text.color'       : '#e8e8f0',
    'grid.color'       : '#1e1e2e',
    'grid.linestyle'   : '--',
    'grid.linewidth'   : 0.5,
    'font.family'      : 'DejaVu Sans',
    'font.size'        : 10,
    'axes.titlesize'   : 13,
    'axes.titleweight' : 'bold',
    'axes.titlepad'    : 14,
    'legend.framealpha': 0,
    'legend.fontsize'  : 9,
})

GOLD   = '#c9a84c'
GREEN  = '#2dd4a0'
RED    = '#f05a6e'
BLUE   = '#5b8def'
PURPLE = '#a78bfa'
ORANGE = '#f97316'
MUTED  = '#686880'
SURFACE= '#18181f'

# ── Load Data ─────────────────────────────────────────────────
pl  = pd.read_csv('data/monthly_pl.csv')
seg = pd.read_csv('data/segment_revenue.csv')
var = pd.read_csv('data/budget_variance.csv')
fc  = pd.read_csv('data/forecast_scenarios.csv')

print("=" * 55)
print("  FinAnalytica — Finance Business Analysis Report")
print("  India BFSI | FY 2024-25")
print("=" * 55)

# ════════════════════════════════════════════════════════════
# CHART 1 — Revenue vs Budget Trend
# ════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor('#09090f')

x = np.arange(len(pl['Month']))
ax.fill_between(x, pl['Actual_Rev'], pl['Budget_Rev'],
                where=pl['Actual_Rev'] >= pl['Budget_Rev'],
                alpha=0.15, color=GREEN, label='_nolegend_')
ax.fill_between(x, pl['Actual_Rev'], pl['Budget_Rev'],
                where=pl['Actual_Rev'] < pl['Budget_Rev'],
                alpha=0.15, color=RED, label='_nolegend_')

ax.plot(x, pl['Actual_Rev'], color=GOLD,  linewidth=2.5, marker='o', markersize=5, label='Actual Revenue')
ax.plot(x, pl['Budget_Rev'], color=MUTED, linewidth=1.5, linestyle='--', label='Budget Revenue')

for i, (a, b) in enumerate(zip(pl['Actual_Rev'], pl['Budget_Rev'])):
    if abs(a - b) > 20:
        ax.annotate(f"{'▲' if a>b else '▼'}{abs(a-b)}",
                    xy=(i, max(a,b)+15), ha='center', fontsize=8,
                    color=GREEN if a>b else RED)

ax.set_xticks(x)
ax.set_xticklabels(pl['Month'], rotation=45, ha='right')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'₹{int(v)}L'))
ax.set_title('Revenue vs Budget — Monthly Trend  |  FY 2024-25  (₹ in Lakhs)')
ax.legend(loc='lower right')
ax.grid(axis='y', alpha=0.4)
ax.spines[['top','right','left','bottom']].set_visible(False)

# Annotation box
total_var = pl['Rev_Variance'].sum()
ax.text(0.01, 0.97, f"YTD Variance: ₹{total_var}L  |  Avg Monthly: ₹{total_var//12}L",
        transform=ax.transAxes, fontsize=9, color=GREEN if total_var>0 else RED,
        va='top', bbox=dict(boxstyle='round,pad=0.4', facecolor=SURFACE, edgecolor='#2a2a38'))

plt.tight_layout()
plt.savefig('charts/01_revenue_vs_budget.png', dpi=150, bbox_inches='tight')
plt.close()
print("\n✅ Chart 1: Revenue vs Budget saved")

# ════════════════════════════════════════════════════════════
# CHART 2 — EBITDA Margin Trend
# ════════════════════════════════════════════════════════════
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), gridspec_kw={'height_ratios':[2,1]})
fig.patch.set_facecolor('#09090f')

# Margin line
ax1.plot(x, pl['EBITDA_Margin_Pct'], color=BLUE, linewidth=2.5, marker='s', markersize=5, label='EBITDA Margin %')
ax1.axhline(y=19.2, color=ORANGE, linewidth=1, linestyle=':', label='Industry Avg 19.2%')
ax1.fill_between(x, pl['EBITDA_Margin_Pct'], 19.2,
                 where=pl['EBITDA_Margin_Pct']>=19.2, alpha=0.1, color=BLUE)
ax1.set_xticks(x); ax1.set_xticklabels(['']*len(x))
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'{v:.1f}%'))
ax1.set_title('EBITDA Margin Trend vs Industry Average  |  FY 2024-25')
ax1.legend(loc='lower right')
ax1.grid(axis='y', alpha=0.4)
ax1.spines[['top','right','left','bottom']].set_visible(False)

# EBITDA absolute bars
colors = [GREEN if v > 0 else RED for v in pl['Actual_EBITDA']]
ax2.bar(x, pl['Actual_EBITDA'], color=colors, alpha=0.8, width=0.6)
ax2.set_xticks(x); ax2.set_xticklabels(pl['Month'], rotation=45, ha='right')
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'₹{int(v)}L'))
ax2.set_title('Absolute EBITDA (₹ Lakhs)', fontsize=10, pad=8)
ax2.grid(axis='y', alpha=0.4)
ax2.spines[['top','right','left','bottom']].set_visible(False)

plt.tight_layout()
plt.savefig('charts/02_ebitda_trend.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 2: EBITDA Trend saved")

# ════════════════════════════════════════════════════════════
# CHART 3 — Cost Breakdown Donut
# ════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor('#09090f')
ax.set_facecolor('#09090f')

cost_labels = ['Personnel','Technology','Marketing','Admin','Compliance','Other']
cost_vals   = [38, 22, 16, 10, 9, 5]
colors_donut= [GOLD, BLUE, GREEN, PURPLE, ORANGE, MUTED]

wedges, texts, autotexts = ax.pie(
    cost_vals, labels=None, colors=colors_donut,
    autopct='%1.0f%%', pctdistance=0.78,
    wedgeprops=dict(width=0.52, edgecolor='#09090f', linewidth=2),
    startangle=90
)
for at in autotexts:
    at.set_fontsize(9); at.set_color('#e8e8f0')

ax.text(0, 0.06, '₹38.2Cr', ha='center', va='center',
        fontsize=16, fontweight='bold', color='#e8e8f0')
ax.text(0, -0.18, 'Total OPEX', ha='center', va='center',
        fontsize=9, color=MUTED)

legend_patches = [mpatches.Patch(color=c, label=f'{l} ({v}%)')
                  for c,l,v in zip(colors_donut, cost_labels, cost_vals)]
ax.legend(handles=legend_patches, loc='lower center',
          ncol=3, bbox_to_anchor=(0.5, -0.06), framealpha=0)
ax.set_title('Operating Cost Breakdown  |  FY 2024-25')

plt.tight_layout()
plt.savefig('charts/03_cost_breakdown.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 3: Cost Breakdown saved")

# ════════════════════════════════════════════════════════════
# CHART 4 — Segment Revenue & YoY Growth
# ════════════════════════════════════════════════════════════
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
fig.patch.set_facecolor('#09090f')

seg_colors = [GOLD, BLUE, GREEN, PURPLE, ORANGE]
xi = np.arange(len(seg))

# Grouped bars
bars1 = ax1.bar(xi - 0.22, seg['FY25_Rev'], 0.4, color=seg_colors, alpha=0.9, label='FY25')
bars2 = ax1.bar(xi + 0.22, seg['FY24_Rev'], 0.4, color=seg_colors, alpha=0.4, label='FY24')
ax1.set_xticks(xi)
ax1.set_xticklabels(seg['Segment'], rotation=20, ha='right', fontsize=9)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'₹{int(v)}L'))
ax1.set_title('Revenue by Segment  |  FY25 vs FY24  (₹ Lakhs)')
ax1.legend()
ax1.grid(axis='y', alpha=0.4)
ax1.spines[['top','right','left','bottom']].set_visible(False)

for bar, val in zip(bars1, seg['FY25_Rev']):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 15,
             f'₹{val}L', ha='center', fontsize=8, color='#e8e8f0')

# YoY Growth horizontal bars
growth_colors = [GREEN if v > 0 else RED for v in seg['YoY_Growth']]
ax2.barh(seg['Segment'], seg['YoY_Growth'], color=growth_colors, alpha=0.85, height=0.5)
ax2.axvline(x=0, color=MUTED, linewidth=0.8)
ax2.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'{v:.0f}%'))
ax2.set_title('YoY Revenue Growth %  |  FY25 vs FY24')
ax2.grid(axis='x', alpha=0.4)
ax2.spines[['top','right','left','bottom']].set_visible(False)

for i, (val, seg_name) in enumerate(zip(seg['YoY_Growth'], seg['Segment'])):
    ax2.text(val + (0.5 if val >= 0 else -0.5), i,
             f'{val}%', va='center', ha='left' if val>=0 else 'right',
             fontsize=9, color=GREEN if val>=0 else RED, fontweight='bold')

plt.tight_layout()
plt.savefig('charts/04_segment_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 4: Segment Analysis saved")

# ════════════════════════════════════════════════════════════
# CHART 5 — Budget Variance Waterfall
# ════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor('#09090f')

items  = var['Line_Item'].tolist()
variances = var['Variance'].tolist()
bar_colors = []
for i, (item, v) in enumerate(zip(items, variances)):
    is_cost = item not in ['Total Revenue', 'EBITDA', 'Net Profit']
    if is_cost:
        bar_colors.append(GREEN if v < 0 else RED)   # cost saving = good
    else:
        bar_colors.append(GREEN if v > 0 else RED)   # revenue beat = good

xi = np.arange(len(items))
bars = ax.bar(xi, variances, color=bar_colors, alpha=0.85, width=0.6, edgecolor='#09090f', linewidth=1.5)
ax.axhline(y=0, color=MUTED, linewidth=0.8)

for bar, val in zip(bars, variances):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + (0.02 if val >= 0 else -0.06),
            f'{"+" if val>0 else ""}₹{val:.2f}Cr',
            ha='center', fontsize=9,
            color=GREEN if val >= 0 else RED, fontweight='bold')

ax.set_xticks(xi)
ax.set_xticklabels(items, rotation=20, ha='right', fontsize=9)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'₹{v:.2f}Cr'))
ax.set_title('Budget Variance Analysis — Actuals vs Budget  |  Q4 FY25  (₹ Crores)')
ax.grid(axis='y', alpha=0.4)
ax.spines[['top','right','left','bottom']].set_visible(False)

fav = mpatches.Patch(color=GREEN, label='Favourable')
adv = mpatches.Patch(color=RED,   label='Adverse')
ax.legend(handles=[fav, adv], loc='upper right')

plt.tight_layout()
plt.savefig('charts/05_variance_waterfall.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 5: Variance Waterfall saved")

# ════════════════════════════════════════════════════════════
# CHART 6 — 3-Scenario Forecast
# ════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor('#09090f')

xf = np.arange(len(fc['Month']))
ax.plot(xf, fc['Best_Case'],  color=GREEN, linewidth=2,   label='Best Case',  marker='o', markersize=4)
ax.plot(xf, fc['Base_Case'],  color=BLUE,  linewidth=2.5, label='Base Case',  marker='s', markersize=5)
ax.plot(xf, fc['Worst_Case'], color=RED,   linewidth=2,   label='Worst Case', marker='v', markersize=4)

ax.fill_between(xf, fc['Best_Case'], fc['Worst_Case'], alpha=0.07, color=BLUE, label='Scenario Range')

# Annotate endpoints
for col, color, label in [('Best_Case', GREEN,'Best'), ('Base_Case', BLUE,'Base'), ('Worst_Case', RED,'Worst')]:
    val = fc[col].iloc[-1]
    ax.annotate(f'₹{val}L', xy=(len(xf)-1, val), xytext=(len(xf)-0.5, val),
                fontsize=9, color=color, va='center', fontweight='bold')

ax.set_xticks(xf)
ax.set_xticklabels(fc['Month'], rotation=45, ha='right')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'₹{int(v)}L'))
ax.set_title('12-Month Revenue Forecast — Scenario Analysis  |  FY 2025-26  (₹ Lakhs)')
ax.legend(loc='upper left')
ax.grid(axis='y', alpha=0.4)
ax.spines[['top','right','left','bottom']].set_visible(False)

plt.tight_layout()
plt.savefig('charts/06_forecast_scenarios.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 6: Forecast Scenarios saved")

# ════════════════════════════════════════════════════════════
# KPI SUMMARY — Pandas Analysis + Export
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 55)
print("  KPI SUMMARY REPORT — FY 2024-25")
print("=" * 55)

total_rev    = pl['Actual_Rev'].sum()
total_budget = pl['Budget_Rev'].sum()
total_var_   = total_rev - total_budget
ytd_margin   = (pl['Actual_EBITDA'].sum() / total_rev * 100)
best_month   = pl.loc[pl['Actual_Rev'].idxmax(), 'Month']
worst_month  = pl.loc[pl['Rev_Variance'].idxmin(), 'Month']

kpis = {
    'Total Revenue (₹ Lakhs)'    : f"₹{total_rev:,}L",
    'Total Budget (₹ Lakhs)'     : f"₹{total_budget:,}L",
    'Revenue Variance'           : f"{'▲' if total_var_>0 else '▼'} ₹{abs(total_var_)}L ({total_var_/total_budget*100:.1f}%)",
    'YTD EBITDA Margin'          : f"{ytd_margin:.1f}%",
    'Industry Avg EBITDA'        : "19.2%",
    'Outperformance vs Industry' : f"+{ytd_margin-19.2:.1f} pp",
    'Best Revenue Month'         : best_month,
    'Weakest Variance Month'     : worst_month,
    'Net Profit (Q4)'            : "₹7.21 Cr",
    'ROE'                        : "17.4%",
}

for k, v in kpis.items():
    print(f"  {k:<35} {v}")

# Export KPI to CSV
kpi_df = pd.DataFrame(list(kpis.items()), columns=['Metric', 'Value'])
kpi_df.to_csv('outputs/kpi_summary.csv', index=False)

# Export full analysis CSVs
pl.to_csv('outputs/monthly_pl_analysis.csv', index=False)
var.to_csv('outputs/variance_analysis.csv', index=False)
seg.to_csv('outputs/segment_analysis.csv', index=False)

print("\n" + "=" * 55)
print("  OUTPUT FILES")
print("=" * 55)
print("  charts/01_revenue_vs_budget.png")
print("  charts/02_ebitda_trend.png")
print("  charts/03_cost_breakdown.png")
print("  charts/04_segment_analysis.png")
print("  charts/05_variance_waterfall.png")
print("  charts/06_forecast_scenarios.png")
print("  outputs/kpi_summary.csv")
print("  outputs/monthly_pl_analysis.csv")
print("  outputs/variance_analysis.csv")
print("  outputs/segment_analysis.csv")
print("=" * 55)
print("\n  ✅ All analysis complete!")
