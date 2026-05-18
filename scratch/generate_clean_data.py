import pandas as pd
import numpy as np
import os

# Set seed for reproducibility
np.random.seed(42)

# Date range: 1 year
dates = pd.date_range(start='2023-01-01', end='2023-12-31')
n_days = len(dates)

# 1. INVESTMENT DATA
channels = ['Google Search', 'Facebook Ads']
investment_data = []

for date in dates:
    for channel in channels:
        base_inv = 1000 if channel == 'Google Search' else 600
        # Add some natural variation
        investment = base_inv + np.random.normal(0, 50)
        
        # INJECT A CLEAN CAUSAL EVENT (Big Spike in Google Search in June)
        if channel == 'Google Search' and date >= pd.Timestamp('2023-06-01') and date <= pd.Timestamp('2023-06-14'):
            investment *= 3  # 200% increase
            
        investment_data.append({'dates': date.strftime('%Y-%m-%d'), 'product_group': channel, 'total_revenue': round(max(0, investment), 2)})

inv_df = pd.DataFrame(investment_data)
inv_df.to_csv('sample_data/investment.csv', index=False)

# 2. PERFORMANCE DATA (KPI)
# Relationship: KPI = Baseline + 0.5*GoogleSearch + 0.3*FacebookAds + Trends + Noise
perf_data = []
for date in dates:
    google_inv = inv_df[(inv_df['dates'] == date.strftime('%Y-%m-%d')) & (inv_df['product_group'] == 'Google Search')]['total_revenue'].values[0]
    fb_inv = inv_df[(inv_df['dates'] == date.strftime('%Y-%m-%d')) & (inv_df['product_group'] == 'Facebook Ads')]['total_revenue'].values[0]
    
    baseline = 500
    # Add seasonality (higher in Dec)
    seasonality = 1.2 if date.month == 12 else 1.0
    
    # Trends effect
    trend_val = 100 + (date.dayofyear / 2) # gradual growth
    
    # Marketing effect (cleaner relationship)
    kpi = (baseline + (google_inv * 0.4) + (fb_inv * 0.2) + trend_val) * seasonality
    
    # Add VERY LITTLE noise to ensure high R-squared
    kpi += np.random.normal(0, 10)
    
    perf_data.append({'date': date.strftime('%Y-%m-%d'), 'Purchases': max(0, int(kpi))})

perf_df = pd.DataFrame(perf_data)
perf_df.to_csv('sample_data/performance.csv', index=False)

# 3. TRENDS DATA
trends_data = []
for date in dates:
    # Trend follows the same logic as the KPI's trend component
    trend_val = 100 + (date.dayofyear / 2) + np.random.normal(0, 5)
    trends_data.append({'Day': date.strftime('%Y-%m-%d'), 'Smartphone Searches': max(0, int(trend_val))})

trends_df = pd.DataFrame(trends_data)
trends_df.to_csv('sample_data/trends.csv', index=False)

print("✅ Sample data regenerated with cleaner relationships for better model fit.")
