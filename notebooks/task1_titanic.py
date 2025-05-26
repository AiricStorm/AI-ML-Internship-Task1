import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/titanic.csv')

# First 5 rows
print(df.head())

# Shape of the dataset
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Columns and data types
print(df.info())

# Basic statistics
print(df.describe(include='all'))

# Count missing values
print(df.isnull().sum())  #no missing values detected

#categorical_cols = df.select_dtypes(include='object').columns.tolist()
numerical_cols = df.select_dtypes(include=np.number).columns.tolist()

#print("Categorical:", categorical_cols)
print("Numerical:", numerical_cols)

df.drop(columns=['Name'], inplace=True)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
print(df.head())

for col in ['Age', 'Fare']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]

for col in ['Age', 'Fare']:
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()
    
df.to_csv('data/titanic_cleaned.csv', index=False)

    


