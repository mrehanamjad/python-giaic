import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class PaperRecommender:
    def __init__(self, data_path):
        self.df = pd.read_json(data_path, lines=True)

        # Drop corrupted column if present
        if 'ti,tle' in self.df.columns:
            self.df.drop(columns=['ti,tle'], inplace=True)

        self.df['title'] = self.df['title'].fillna('')
        self.df['abstract'] = self.df['abstract'].fillna('')
        self.df['categories'] = self.df['categories'].fillna('')

        # Combine fields into a single content column
        self.df['content'] = self.df['title'] + " " + self.df['abstract'] + " " + self.df['categories']

        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['content'])

    def recommend(self, query, top_n=5):
        query_vec = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = cosine_similarities.argsort()[-top_n:][::-1]
        return self.df.iloc[top_indices][['title', 'abstract', 'categories']].reset_index(drop=True)
    


