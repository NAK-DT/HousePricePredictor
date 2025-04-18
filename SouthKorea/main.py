import pandas as pd

df = pd.read_csv('seoul_real_estate.csv', encoding='euc-kr')
print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())
