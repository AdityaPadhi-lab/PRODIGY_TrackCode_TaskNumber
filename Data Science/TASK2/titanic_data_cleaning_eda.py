import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("titanic.csv")

# Display basic information
print(df.info())
print(df.describe())
print(df.head())

# Handling missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)  # Too many missing values

# Convert categorical variables
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# Exploratory Data Analysis (EDA)
plt.figure(figsize=(8,5))
sns.countplot(x='Survived', data=df, palette='pastel')
plt.title('Survival Count')
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(df['Age'], bins=30, kde=True, color='blue')
plt.title('Age Distribution')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='Pclass', y='Age', data=df, palette='coolwarm')
plt.title('Age vs Passenger Class')
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x='Pclass', hue='Survived', data=df, palette='Set2')
plt.title('Survival Rate by Passenger Class')
plt.show()

print(df.corr())
