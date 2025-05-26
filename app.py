import streamlit as st
import pandas as pd
import joblib
from scipy.sparse import hstack

# Load data and models
papers = pd.read_csv("papers.csv")
interactions = pd.read_csv("user_paper_interactions.csv")

model = joblib.load("recommendation_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")
user_encoder = joblib.load("user_encoder.pkl")

st.title("📚 Research Paper Recommender")

# User selects their user ID
user_ids = interactions['user_id'].unique()
user_id = st.selectbox("Select your User ID:", user_ids)

# Encode user
user_encoded = user_encoder.transform([user_id])[0]

# Find papers the user already interacted with
seen_paper_ids = interactions[interactions['user_id'] == user_id]['paper_id'].unique()

# Filter unseen papers
unseen_papers = papers[~papers['paper_id'].isin(seen_paper_ids)].copy()
unseen_papers['text'] = unseen_papers['title'] + " " + unseen_papers['abstract'] + " " + unseen_papers['keywords']

# Prepare features for prediction
X_text = tfidf.transform(unseen_papers['text'])
X_user = [[user_encoded]] * X_text.shape[0]
X = hstack([X_text, X_user])

# Predict probabilities
unseen_papers['score'] = model.predict_proba(X)[:, 1]

# Show top 10 recommendations
recommendations = unseen_papers.sort_values(by='score', ascending=False).head(10)

st.subheader("Top Recommended Papers for You")
for idx, row in recommendations.iterrows():
    st.markdown(f"### {row['title']}")
    st.markdown(f"**Score:** {row['score']:.2f}")
    st.markdown(f"{row['abstract'][:300]}...")
    st.markdown("---")
