import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

url = 'https://data.cityofnewyork.us/api/views/2yzn-s2s3/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)

print(df.head())
print(df.columns)
print(df.info())

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df.drop_duplicates(inplace=True)
df.dropna(subset=['dba', 'boro', 'cuisine_description', 'violation_description'], 
inplace=True)

major_violations = df['violation_description'].value_counts().nlargest(10).index
print("Major Violations:\\n", major_violations)

boro_violations = df['boro'].value_counts()
print("Borough Violations:\\n", boro_violations)

plt.figure(figsize=(10,6))
sns.plot(y=major_violations, x=major_violations, palette='viridis') 
plt.title('Top 10 Major Violations')
plt.xlabel("No. of Violations")
plt.ylabel("Violation Description")
plt.show()

