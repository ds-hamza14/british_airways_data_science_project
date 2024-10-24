import pandas as pd
import matplotlib.pyplot as plt

# Load the sentiment data
df = pd.read_csv('sentiment_british_airways_reviews.csv')

# Plot sentiment distribution
sentiment_counts = df['Sentiment_Type'].value_counts()
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])

# Add labels and title
plt.title('Sentiment Analysis of British Airways Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')

# Show the plot
plt.show()
# Plot sentiment distribution as a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['green', 'red', 'gray'])
plt.title('Sentiment Analysis of British Airways Reviews')
plt.show()
from wordcloud import WordCloud

# Combine all reviews into a single string
text = " ".join(review for review in df.Review)

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.show()

# Plot a horizontal bar chart for sentiment counts
sentiment_counts.plot(kind='barh', color=['green', 'red', 'gray'])
plt.title('Number of Reviews by Sentiment Type')
plt.xlabel('Number of Reviews')
plt.ylabel('Sentiment Type')
plt.show()
# Plot a histogram of sentiment polarity
plt.figure(figsize=(10, 5))
plt.hist(df['Sentiment'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Sentiment Polarity')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.show()
