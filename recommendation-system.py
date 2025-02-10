import numpy as np

# Step 1: Create a sample user-item rating matrix (movies and users)
# Rows: Movies, Columns: Users
ratings = np.array([
    [5, 3, 4, 4, 0],  # Dilwale Dulhania Le Jayenge (DDLJ)
    [3, 1, 2, 3, 3],  # Kabhi Khushi Kabhie Gham
    [4, 3, 4, 3, 5],  # 3 Idiots
    [4, 3, 4, 5, 4],  # Lagaan
    [1, 5, 1, 3, 4]   # Zindagi Na Milegi Dobara
])

# Bollywood movies list
movies = [
    'Dilwale Dulhania Le Jayenge (DDLJ)',
    'Kabhi Khushi Kabhie Gham',
    '3 Idiots',
    'Lagaan',
    'Zindagi Na Milegi Dobara'
]

# Step 2: Compute cosine similarity between items (movies)
def cosine_similarity(matrix):
    # Normalize the ratings (centering the matrix)
    norm_matrix = matrix - np.mean(matrix, axis=1, keepdims=True)
    
    # Compute cosine similarity between items (movies)
    similarity = np.dot(norm_matrix, norm_matrix.T)  # Dot product between items
    norms = np.linalg.norm(norm_matrix, axis=1)  # Norm of each movie's rating vector
    similarity /= np.outer(norms, norms)  # Normalize similarity
    
    return similarity

# Calculate cosine similarity matrix
item_similarity = cosine_similarity(ratings)

# Step 3: Recommend movies based on an item the user likes
def recommend_items(movie_index, num_recommendations=3):
    # Get similarity scores for the chosen movie
    similar_scores = item_similarity[movie_index]
    
    # Sort the items by similarity (in descending order)
    sorted_indices = np.argsort(similar_scores)[::-1]
    
    # Get the top N recommendations, excluding the movie itself
    recommendations = sorted_indices[sorted_indices != movie_index][:num_recommendations]
    
    return recommendations

# Example: Recommend movies based on Dilwale Dulhania Le Jayenge (DDLJ) (index 0)
movie_index = 0
recommended_movie_indices = recommend_items(movie_index)

# Display recommended movies
recommended_movies = [movies[i] for i in recommended_movie_indices]
print(f"Recommended Movies based on {movies[movie_index]}: {recommended_movies}")
