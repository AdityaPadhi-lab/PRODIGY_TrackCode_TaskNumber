import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset: Age distribution
data = {
    'Age Group': ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81+'],
    'Population': [500, 700, 1200, 1500, 1300, 900, 600, 300, 100]
}

df = pd.DataFrame(data)

# Plot bar chart
plt.figure(figsize=(10, 5))
sns.barplot(x='Age Group', y='Population', data=df, palette='viridis')
plt.xlabel('Age Group')
plt.ylabel('Population Count')
plt.title('Age Distribution in Population')
plt.show()
