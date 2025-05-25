import streamlit as st
import pandas as pd
import os
from recommender import PaperRecommender

# Streamlit Config
st.set_page_config(page_title="SmartScholar - Paper Recommender", layout="wide")
st.title("📚 SmartScholar - Research Paper Recommender")

st.markdown("""
Enter your research interests, keywords, or a paper abstract snippet below and get top paper recommendations based on NLP and similarity analysis.
""")

# Check if data file exists
data_file = "arxiv-metadata-oai-snapshot.json"
if not os.path.exists(data_file):
    st.error(f"""
    🚨 **Data file not found!**
    
    The file `{data_file}` is required but not found. This usually happens because:
    
    1. **Large file size**: The ArXiv dataset is typically very large (several GB) and cannot be uploaded to Streamlit Cloud directly.
    
    2. **Missing file**: The data file wasn't included in your repository.
    
    **Solutions:**
    
    - **Option 1**: Use a smaller sample dataset for demonstration
    - **Option 2**: Download the data programmatically (if size permits)
    - **Option 3**: Use cloud storage (AWS S3, Google Drive, etc.) to host the file
    - **Option 4**: Create a sample dataset for testing purposes
    
    Please add the data file to your repository or implement one of the solutions above.
    """)
    st.stop()

query = st.text_area("🔍 What are you looking for?", height=150)

# Initialize recommender with error handling
@st.cache_resource
def load_recommender():
    try:
        return PaperRecommender(data_file)
    except Exception as e:
        st.error(f"Error loading recommender: {str(e)}")
        return None

if 'recommender' not in st.session_state:
    with st.spinner("Loading paper database... This may take a moment."):
        st.session_state.recommender = load_recommender()

if st.session_state.recommender is None:
    st.error("Failed to load the paper recommender. Please check the data file.")
    st.stop()

if st.button("Get Recommendations"):
    if not query.strip():
        st.warning("Please enter some search text.")
    else:
        try:
            with st.spinner("Finding recommendations..."):
                results = st.session_state.recommender.recommend(query)
            
            if results.empty:
                st.info("No recommendations found. Try different keywords.")
            else:
                st.subheader("📄 Recommended Papers")
                for i, row in results.iterrows():
                    with st.expander(f"**{i+1}. {row['title']}**"):
                        st.markdown(f"**Abstract:** {row['abstract'][:500]}{'...' if len(row['abstract']) > 500 else ''}")
                        st.markdown(f"**Categories:** {row['categories']}")
        except Exception as e:
            st.error(f"Error getting recommendations: {str(e)}")