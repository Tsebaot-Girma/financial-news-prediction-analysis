# sentiment_analysis.py

from textblob import TextBlob

# Function to categorize sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis to headlines
def apply_sentiment_analysis(df, column='headline'):
    df['sentiment'] = df[column].apply(get_sentiment)
    return df
