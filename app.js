/* ============================================================
   FinAnalytica — app.js
   Charts, variance table, interactivity
   ============================================================ */

// ── Live date ──────────────────────────────────────────────
document.getElementById('live-date').textContent = new Date().toLocaleDateString('en-IN', {
  day: '2-digit', month: 'short', year: 'numeric'
});

// ── Chart defaults ─────────────────────────────────────────
Chart.defaults.color = '#686880';
Chart.defaults.font.family = "'DM Mono', monospace";
Chart.defaults.font.size = 11;

const GOLD = '#c9a84c';
const GREEN = '#2dd4a0';
const RED = '#f05a6e';
const BLUE = '#5b8def';
const SURFACE2 = '#18181f';

// ── Revenue vs Budget Chart ────────────────────────────────
const months = ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar'];
const actualRev = [620, 680, 710, 740, 760, 800, 820, 780, 850, 870, 920, 910];
const budgetRev = [640, 660, 700, 720, 750, 780, 800, 800, 820, 850, 880, 900];

new Chart(document.getElementById('revenueChart'), {
  type: 'line',
  data: {
    labels: months,
    datasets: [
      {
        label: 'Actual',
        data: actualRev,
        borderColor: GOLD,
        backgroundColor: 'rgba(201,168,76,0.08)',
        borderWidth: 2,
        pointBackgroundColor: GOLD,
        pointRadius: 4,
        pointHoverRadius: 6,
        tension: 0.4,
        fill: true,
      },
      {
        label: 'Budget',
        data: budgetRev,
        borderColor: 'rgba(150,150,170,0.5)',
        backgroundColor: 'transparent',
        borderWidth: 1.5,
        borderDash: [5, 4],
        pointRadius: 0,
        tension: 0.4,
      }
    ]
  },
  options: {
    responsive: true,
    interaction: { mode: 'index', intersect: false },
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: '#18181f',
        borderColor: 'rgba(255,255,255,0.08)',
        borderWidth: 1,
        titleColor: '#e8e8f0',
        bodyColor: '#9898b0',
        callbacks: {
          label: ctx => ` ₹${ctx.parsed.y} L`
        }
      }
    },
    scales: {
      x: { grid: { color: 'rgba(255,255,255,0.04)' }, border: { display: false } },
      y: {
        grid: { color: 'rgba(255,255,255,0.04)' },
        border: { display: false },
        ticks: { callback: v => `₹${v}L` }
      }
    }
  }
});

// ── Cost Donut Chart ───────────────────────────────────────
new Chart(document.getElementById('costChart'), {
  type: 'doughnut',
  data: {
    labels: ['Personnel', 'Technology', 'Marketing', 'Admin', 'Compliance', 'Other'],
    datasets: [{
      data: [38, 22, 16, 10, 9, 5],
      backgroundColor: [GOLD, BLUE, GREEN, '#a78bfa', '#f97316', '#94a3b8'],
      borderWidth: 0,
      hoverOffset: 6,
    }]
  },
  options: {
    cutout: '68%',
    responsive: true,
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          padding: 12,
          boxWidth: 10,
          boxHeight: 10,
          font: { size: 10 }
        }
      },
      tooltip: {
        backgroundColor: '#18181f',
        borderColor: 'rgba(255,255,255,0.08)',
        borderWidth: 1,
        callbacks: { label: ctx => ` ${ctx.label}: ${ctx.parsed}%` }
      }
    }
  }
});

// ── Segment Chart ──────────────────────────────────────────
new Chart(document.getElementById('segmentChart'), {
  type: 'bar',
  data: {
    labels: ['Retail\nBanking', 'Corporate\nLoans', 'Wealth\nMgmt', 'Insurance', 'Digital\nFinance'],
    datasets: [{
      label: 'Revenue (₹ Cr)',
      data: [28.4, 22.1, 14.6, 11.2, 8.3],
      backgroundColor: [
        'rgba(201,168,76,0.8)',
        'rgba(91,141,239,0.8)',
        'rgba(45,212,160,0.8)',
        'rgba(167,139,250,0.8)',
        'rgba(249,115,22,0.8)',
      ],
      borderRadius: 6,
      borderSkipped: false,
    }]
  },
  options: {
    indexAxis: 'y',
    responsive: true,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: '#18181f',
        borderColor: 'rgba(255,255,255,0.08)',
        borderWidth: 1,
        callbacks: { label: ctx => ` ₹${ctx.parsed.x} Cr` }
      }
    },
    scales: {
      x: { grid: { color: 'rgba(255,255,255,0.04)' }, border: { display: false }, ticks: { callback: v => `₹${v}` } },
      y: { grid: { display: false }, border: { display: false } }
    }
  }
});

// ── Forecast Chart ─────────────────────────────────────────
const fMonths = ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar'];
const best   = [920, 960, 995, 1020, 1050, 1080, 1110, 1090, 1130, 1160, 1200, 1220];
const base   = [880, 910, 940, 965, 990, 1010, 1030, 1010, 1050, 1070, 1100, 1110];
const worst  = [820, 840, 860, 880, 900, 910, 920, 905, 930, 945, 960, 970];

new Chart(document.getElementById('forecastChart'), {
  type: 'line',
  data: {
    labels: fMonths,
    datasets: [
      {
        label: 'Best Case',
        data: best,
        borderColor: GREEN,
        backgroundColor: 'rgba(45,212,160,0.05)',
        borderWidth: 2,
        pointRadius: 0,
        tension: 0.4,
        fill: false,
      },
      {
        label: 'Base Case',
        data: base,
        borderColor: BLUE,
        backgroundColor: 'rgba(91,141,239,0.07)',
        borderWidth: 2.5,
        pointRadius: 3,
        pointBackgroundColor: BLUE,
        tension: 0.4,
        fill: '+1',
      },
      {
        label: 'Worst Case',
        data: worst,
        borderColor: RED,
        backgroundColor: 'rgba(240,90,110,0.05)',
        borderWidth: 2,
        pointRadius: 0,
        tension: 0.4,
        fill: false,
      }
    ]
  },
  options: {
    responsive: true,
    interaction: { mode: 'index', intersect: false },
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: '#18181f',
        borderColor: 'rgba(255,255,255,0.08)',
        borderWidth: 1,
        callbacks: { label: ctx => ` ${ctx.dataset.label}: ₹${ctx.parsed.y}L` }
      }
    },
    scales: {
      x: { grid: { color: 'rgba(255,255,255,0.04)' }, border: { display: false } },
      y: { grid: { color: 'rgba(255,255,255,0.04)' }, border: { display: false }, ticks: { callback: v => `₹${v}L` } }
    }
  }
});

// ── Variance Table Data ─────────────────────────────────────
const varianceData = [
  { item: 'Total Revenue',       budget: 40.00, actual: 43.21, driver: 'Higher retail volumes' },
  { item: 'Personnel Expenses',  budget: 12.00, actual: 13.40, driver: 'Appraisal cycle advance' },
  { item: 'Technology & IT',     budget:  8.00, actual:  7.45, driver: 'Cloud migration savings' },
  { item: 'Marketing Spend',     budget:  5.00, actual:  4.70, driver: 'Campaign rescheduled' },
  { item: 'Compliance & Risk',   budget:  3.50, actual:  3.62, driver: 'Regulatory update cost' },
  { item: 'Admin & Facilities',  budget:  4.00, actual:  3.80, driver: 'WFH policy continued' },
  { item: 'EBITDA',              budget:  9.00, actual: 10.04, driver: 'Operational leverage' },
  { item: 'Net Profit',          budget:  6.50, actual:  7.21, driver: 'Revenue beat + cost ctrl' },
];

const tbody = document.getElementById('varianceTable');
varianceData.forEach((row, i) => {
  const variance = (row.actual - row.budget).toFixed(2);
  const varPct = ((row.actual - row.budget) / row.budget * 100).toFixed(1);
  const isFav = parseFloat(variance) >= 0;
  const isRev = i === 0 || i === 6 || i === 7;

  // For revenue-like lines, positive variance is favourable; for cost lines, negative is fav
  const favourable = isRev ? isFav : !isFav;

  let statusClass, statusLabel;
  if (Math.abs(parseFloat(varPct)) < 1) {
    statusClass = 'status-neu'; statusLabel = 'On Target';
  } else if (favourable) {
    statusClass = 'status-fav'; statusLabel = 'Favourable';
  } else {
    statusClass = 'status-adv'; statusLabel = 'Adverse';
  }

  const varClass = isFav ? 'td-var-pos' : 'td-var-neg';
  const sign = isFav ? '+' : '';

  const tr = document.createElement('tr');
  tr.innerHTML = `
    <td class="td-name">${row.item}</td>
    <td>₹${row.budget.toFixed(2)}</td>
    <td>₹${row.actual.toFixed(2)}</td>
    <td class="${varClass}">${sign}${variance}</td>
    <td class="${varClass}">${sign}${varPct}%</td>
    <td><span class="status-badge ${statusClass}">${statusLabel}</span></td>
    <td style="color:var(--text-muted);font-size:11px">${row.driver}</td>
  `;
  tbody.appendChild(tr);
});

// ── Sidebar nav active highlighting ────────────────────────
const navItems = document.querySelectorAll('.nav-item');
navItems.forEach(item => {
  item.addEventListener('click', () => {
    navItems.forEach(n => n.classList.remove('active'));
    item.classList.add('active');
  });
});

// ── KPI bar animation on load ──────────────────────────────
document.querySelectorAll('.kpi-fill').forEach(el => {
  const target = el.style.width;
  el.style.width = '0%';
  setTimeout(() => { el.style.width = target; }, 300);
});
