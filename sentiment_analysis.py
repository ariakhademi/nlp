import pandas as pd
import os
import kagglehub
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import nltk

df = pd.read_csv(path + "/IMDB Dataset.csv")
df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})

pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words='english', tokenizer=word_tokenize, lowercase=True)),
    ('model', MultinomialNB())
])

# train/test split
x = df['review']
y = df['sentiment']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

pipeline.fit(x_train, y_train)

# Function to predict the sentiment of new reviews
def predict_sentiment(new_review):
    if not new_review.strip():
        return 'neutral'
    prediction = pipeline.predict([new_review])
    if prediction[0] == 1:
        return 'positive'
    else:
        return 'negative'

# Example usage
new_review = "I love it."
print(predict_sentiment(new_review))  # Output: positive
new_review = "This movie was terrible. I hated it."
print(predict_sentiment(new_review))  # Output: negative

y_pred = pipeline.predict(x_test)
acc = accuracy_score(y_pred, y_test)
print(f'accuracy: {acc}')