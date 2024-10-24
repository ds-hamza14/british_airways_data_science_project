from textblob import TextBlob
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('cleaned_british_airways_reviews.csv')

# Function to calculate sentiment polarity
def get_sentiment(review):
    analysis = TextBlob(review)
    return analysis.sentiment.polarity

# Apply sentiment analysis to the reviews
df['Sentiment'] = df['Review'].apply(get_sentiment)

# Classify reviews based on polarity
df['Sentiment_Type'] = df['Sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

# Save the results
df.to_csv('sentiment_british_airways_reviews.csv', index=False)

# Save sentiment counts to a CSV file
sentiment_counts = df['Sentiment_Type'].value_counts()
sentiment_counts.to_csv('sentiment_counts.csv', header=True)
print("Sentiment counts saved to 'sentiment_counts.csv'.")

# Display sentiment breakdown
print(sentiment_counts)
