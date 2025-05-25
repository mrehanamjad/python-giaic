import streamlit as st
import pandas as pd
from recommender import PaperRecommender

# Streamlit Config
st.set_page_config(page_title="SmartScholar - Paper Recommender", layout="wide")
st.title("📚 SmartScholar - Research Paper Recommender")

st.markdown("""
Enter your research interests, keywords, or a paper abstract snippet below and get top paper recommendations based on NLP and similarity analysis.
""")

query = st.text_area("🔍 What are you looking for?", height=150)

if 'recommender' not in st.session_state:
    st.session_state.recommender = PaperRecommender("./arxiv-metadata-oai-snapshot.json")

if st.button("Get Recommendations"):
    if not query.strip():
        st.warning("Please enter some search text.")
    else:
        results = st.session_state.recommender.recommend(query)
        st.subheader("📄 Recommended Papers")
        for i, row in results.iterrows():
            st.markdown(f"**{i+1}. {row['title']}**")
            st.markdown(f"*Abstract:* {row['abstract'][:500]}...")
            st.markdown(f"*Categories:* {row['categories']}")
            st.markdown("---")
            

