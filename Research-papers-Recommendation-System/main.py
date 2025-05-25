from recommender import PaperRecommender
from utils import get_user_query

def main():
    recommender = PaperRecommender("arxiv-metadata-oai-snapshot.json")
    query = get_user_query()
    results = recommender.recommend(query)

    print("\nTop Recommended Papers:\n")
    for i, row in results.iterrows():
        print(f"{i+1}. {row['title']}")
        print(f"   Abstract: {row['abstract'][:150]}...")
        print(f"   Categories: {row['categories']}\n")

if __name__ == "__main__":
    main()
