import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulate traffic data for 24 hours
hours = list(range(24))
np.random.seed(42)
traffic_volume = np.random.poisson(lam=[30 + 50 * np.sin(h * np.pi / 12) for h in hours])

# Create DataFrame
df = pd.DataFrame({
    'Hour': hours,
    'Traffic Volume': traffic_volume
})

# Plotting
plt.figure(figsize=(12, 6))

# Scatter Plot
plt.scatter(df['Hour'], df['Traffic Volume'], color='red', label='Scatter: Traffic Volume')

# Line Chart
plt.plot(df['Hour'], df['Traffic Volume'], color='blue', linestyle='-', linewidth=2, label='Line: Traffic Trend')

# Plot Decorations
plt.title('Traffic Volume Pattern Over 24 Hours')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Vehicles')
plt.xticks(range(0, 24))
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()
