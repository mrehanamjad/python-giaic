import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class PaperRecommender:
    def __init__(self, data_path):
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found: {data_path}")
        
        try:
            self.df = pd.read_json(data_path, lines=True)
        except Exception as e:
            raise Exception(f"Error reading JSON file: {str(e)}")

        # Drop corrupted column if present
        if 'ti,tle' in self.df.columns:
            self.df.drop(columns=['ti,tle'], inplace=True)

        # Fill missing values
        self.df['title'] = self.df['title'].fillna('')
        self.df['abstract'] = self.df['abstract'].fillna('')
        self.df['categories'] = self.df['categories'].fillna('')

        # Remove completely empty rows
        self.df = self.df[(self.df['title'] != '') | (self.df['abstract'] != '')]

        if self.df.empty:
            raise Exception("No valid data found in the dataset")

        # Combine fields into a single content column
        self.df['content'] = self.df['title'] + " " + self.df['abstract'] + " " + self.df['categories']

        try:
            self.vectorizer = TfidfVectorizer(
                stop_words='english',
                max_features=10000,  # Limit features to prevent memory issues
                ngram_range=(1, 2),  # Include bigrams for better matching
                min_df=2,  # Ignore terms that appear in less than 2 documents
                max_df=0.95  # Ignore terms that appear in more than 95% of documents
            )
            self.tfidf_matrix = self.vectorizer.fit_transform(self.df['content'])
        except Exception as e:
            raise Exception(f"Error creating TF-IDF matrix: {str(e)}")

    def recommend(self, query, top_n=5):
        if not query or not query.strip():
            return pd.DataFrame(columns=['title', 'abstract', 'categories'])
        
        try:
            query_vec = self.vectorizer.transform([query])
            cosine_similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
            
            # Get top indices, excluding those with zero similarity
            similarity_threshold = 0.01
            valid_indices = cosine_similarities > similarity_threshold
            
            if not valid_indices.any():
                return pd.DataFrame(columns=['title', 'abstract', 'categories'])
            
            valid_similarities = cosine_similarities[valid_indices]
            valid_idx_positions = valid_indices.nonzero()[0]
            
            # Get top N from valid results
            top_n = min(top_n, len(valid_similarities))
            top_positions = valid_similarities.argsort()[-top_n:][::-1]
            top_indices = valid_idx_positions[top_positions]
            
            return self.df.iloc[top_indices][['title', 'abstract', 'categories']].reset_index(drop=True)
            
        except Exception as e:
            raise Exception(f"Error during recommendation: {str(e)}")

    def get_stats(self):
        """Return basic statistics about the dataset"""
        return {
            'total_papers': len(self.df),
            'categories': list(set(','.join(self.df['categories']).split(','))),
            'sample_titles': self.df['title'].head(5).tolist()
        }