import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load dataset
df = pd.read_csv("US_Accidents.csv")

# Display basic information
print(df.info())
print(df.head())

# Handling missing values
df.dropna(subset=['Start_Lat', 'Start_Lng'], inplace=True)  # Drop rows with missing location data

# Accident distribution by time of day
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour
plt.figure(figsize=(10, 5))
sns.histplot(df['Hour'], bins=24, kde=True, color='blue')
plt.title('Accident Distribution by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.show()

# Weather condition impact on accidents
plt.figure(figsize=(12, 6))
sns.countplot(y=df['Weather_Condition'], order=df['Weather_Condition'].value_counts().index[:10], palette='coolwarm')
plt.title('Top 10 Weather Conditions Leading to Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.show()

# Create accident heatmap
map_center = [df['Start_Lat'].mean(), df['Start_Lng'].mean()]
heatmap_map = folium.Map(location=map_center, zoom_start=5)
heat_data = df[['Start_Lat', 'Start_Lng']].values.tolist()
HeatMap(heat_data).add_to(heatmap_map)

# Save the heatmap
heatmap_map.save("accident_heatmap.html")
print("Accident heatmap saved as 'accident_heatmap.html'")
