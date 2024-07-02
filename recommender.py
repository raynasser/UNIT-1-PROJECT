

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity





def get_recommendations(chosen_movie, movie_data):

    try:

        # Filter out the selected movie
        filtered_data = movie_data[(movie_data['title'] != chosen_movie['title']) | 
                                   (movie_data['genre'] != chosen_movie['genre']) | 
                                   (movie_data['year'] != chosen_movie['year'])
                                ]

        # Handle Nulls
        filtered_data = filtered_data.dropna(subset=['description'])
        filtered_data['description'] = filtered_data['description'].fillna('')

        # Vectorizing
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(filtered_data['description'])

        query_vec = tfidf.transform([chosen_movie['description']])

        cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()

        sim_scores = list(enumerate(cosine_sim))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[:10]

        movie_indices = [i[0] for i in sim_scores]

        return filtered_data.iloc[movie_indices][['title', 'genre', 'country', 'year']].sort_values(
            by='year', ascending=False).to_dict(orient='records')
    


    except Exception as e:
        print(f"An error occurred in the recommender system: {e}")
        return []
    