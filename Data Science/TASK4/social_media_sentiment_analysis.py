import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob

# Load dataset
df = pd.read_csv("twitter_training.csv")

# Display basic information
print(df.info())
print(df.head())

# Rename columns for clarity
df.columns = ['Tweet_ID', 'Entity', 'Sentiment', 'Tweet']

# Drop unnecessary columns
df = df[['Sentiment', 'Tweet']]

# Sentiment distribution
plt.figure(figsize=(8,5))
sns.countplot(x='Sentiment', data=df, palette='coolwarm')
plt.title('Sentiment Distribution')
plt.show()

# Text Preprocessing Function
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['Polarity'] = df['Tweet'].apply(get_sentiment)

# Sentiment Analysis Visualization
plt.figure(figsize=(10,5))
sns.histplot(df['Polarity'], bins=30, kde=True, color='blue')
plt.title('Sentiment Polarity Distribution')
plt.show()

# Word Cloud for Positive Sentiment
positive_text = " ".join(df[df['Sentiment'] == 'Positive']['Tweet'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Positive Sentiment Word Cloud')
plt.show()

# Word Cloud for Negative Sentiment
negative_text = " ".join(df[df['Sentiment'] == 'Negative']['Tweet'])
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(negative_text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Negative Sentiment Word Cloud')
plt.show()
