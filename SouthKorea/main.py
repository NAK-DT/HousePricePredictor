import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\Projects\HousePricePredictor\SouthKorea\seoul - SeoulRealEstate.csv', encoding='euc-kr')
print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

plt.figure(figsize=(12, 6))
sns.histplot(df['avg_sales'], bins=50, kde=True)
plt.title('Seoul Housing Price Distribution')
plt.xlabel('Average Sales Price')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df[['m2', 'households', 'buildDate', 'score', 'avg_sales']].corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Matrix')
plt.show()