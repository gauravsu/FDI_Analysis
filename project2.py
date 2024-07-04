import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv(r'C:\Users\HP\Desktop\New folder (2)\FDI data.csv')

# Display the first few rows of the dataset
print(df.head())

# Basic descriptive statistics
print(df.describe())

# Calculate total FDI for each year
yearly_fdi = df.drop(['Sector'], axis=1).sum()

# Plot total FDI for each year
plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_fdi)
plt.title('Total FDI in India (2000-01 to 2016-17)')
plt.xlabel('Year')
plt.ylabel('Total FDI (Crores)')
plt.xticks(rotation=45)
plt.show()

# Calculate total FDI for each sector
sector_fdi = df.set_index('Sector').sum(axis=1)

# Plot total FDI for each sector
plt.figure(figsize=(12, 6))
sector_fdi.sort_values(ascending=False).plot(kind='bar')
plt.title('Total FDI by Sector (2000-01 to 2016-17)')
plt.xlabel('Sector')
plt.ylabel('Total FDI (Crores)')
plt.xticks(rotation=90)
plt.show()

# Calculate year-over-year growth for each sector
df_growth = df.copy()
for col in df.columns[1:]:
    df_growth[col] = df[col].pct_change() * 100

# Display the year-over-year growth
print(df_growth)

# Correlation analysis
correlation_matrix = df.drop(['Sector'], axis=1).corr()

# Plot the heatmap for correlation
plt.figure(figsize=(12, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Year-wise FDI')
plt.show()

# Calculate CAGR for each sector
years = len(df.columns) - 1
cagr = ((df.set_index('Sector').iloc[:, -1] / df.set_index('Sector').iloc[:, 0]) ** (1/years) - 1) * 100

# Display the CAGR for each sector
print("Compound Annual Growth Rate (CAGR) for each sector:")
print(cagr)

# Summarize the findings
print("Summary of FDI Analysis:")
print("Total FDI across all sectors over the years:", yearly_fdi.sum())
print("Sector with highest FDI:", sector_fdi.idxmax(), "with", sector_fdi.max(), "crores")
print("Sector with lowest FDI:", sector_fdi.idxmin(), "with", sector_fdi.min(), "crores")
print("Year with highest total FDI:", yearly_fdi.idxmax(), "with", yearly_fdi.max(), "crores")
print("Year with lowest total FDI:", yearly_fdi.idxmin(), "with", yearly_fdi.min(), "crores")

# Highlight sectors with significant trends
print("Sectors with highest CAGR:", cagr.idxmax(), "with", cagr.max(), "%")
print("Sectors with lowest CAGR:", cagr.idxmin(), "with", cagr.min(), "%")

# Further insights and recommendations
# (This section can be filled with additional findings and actionable insights based on the analysis)
