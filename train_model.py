import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from scipy.sparse import hstack
import joblib

# Load data
papers = pd.read_csv("papers.csv")
interactions = pd.read_csv("user_paper_interactions.csv")

# Merge datasets on paper_id
data = interactions.merge(papers, on="paper_id")
data['text'] = data['title'] + " " + data['abstract'] + " " + data['keywords']

# Encode user_id
user_encoder = LabelEncoder()
data['user_encoded'] = user_encoder.fit_transform(data['user_id'])

# TF-IDF vectorization
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
X_text = tfidf.fit_transform(data['text'])

# Combine TF-IDF features with user encoding
X = hstack([X_text, data['user_encoded'].values.reshape(-1, 1)])

y = data['liked']

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save the model, vectorizer, and user encoder
joblib.dump(model, "recommendation_model.pkl")
joblib.dump(tfidf, "tfidf_vectorizer.pkl")
joblib.dump(user_encoder, "user_encoder.pkl")

print("Models saved: recommendation_model.pkl, tfidf_vectorizer.pkl, user_encoder.pkl")
