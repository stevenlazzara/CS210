# --- PART 1: READING DATA ---

# 1.1
def read_ratings_data(f):
    movie_ratings = {}
    with open(f, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            movie_name = parts[0]
            rating = float(parts[1])
            if movie_name not in movie_ratings:
                movie_ratings[movie_name] = []
            movie_ratings[movie_name].append(rating)
    return movie_ratings

# 1.2
def read_movie_genre(f):
    movie_genre = {}
    with open(f, "r") as file:
        for line in file:
            genre, _, movie = line.strip().split("|")
            movie_genre[movie.strip()] = genre.strip()
    return movie_genre

# --- PART 2: PROCESSING DATA ---

# 2.1
def create_genre_dict(d):
    genre_movie_dict = {}
    movie_genre_dict = d
    for movie, genre in movie_genre_dict.items():
        if genre in genre_movie_dict:
            genre_movie_dict[genre].append(movie)
        else:
            genre_movie_dict[genre] = [movie]
    return genre_movie_dict

# 2.2
def calculate_average_rating(d):
    avg_ratings_dict = {}
    ratings_dict = d
    for movie, ratings in ratings_dict.items():
        avg_rating = sum(ratings) / len(ratings)
        avg_ratings_dict[movie] = avg_rating
    return avg_ratings_dict

# --- PART 3: RECOMMENDATION ---

# 3.1
def get_popular_movies(d, n=10):
    avg_ratings_dict = d
    sorted_movies = sorted(avg_ratings_dict.items(), key=lambda x: x[1], reverse=True)
    if n > len(sorted_movies):
        n = len(sorted_movies)
    top_n_movies = dict(sorted_movies[:n])
    return top_n_movies

# 3.2
def filter_movies(d, thres_rating=3):
    avg_ratings_dict = d
    filtered_dict = {k: v for k, v in avg_ratings_dict.items() if v >= thres_rating}
    return filtered_dict

# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    genre_dict = genre_to_movies
    movie_ratings = movie_to_average_rating
    genre_movies = genre_dict.get(genre, [])
    genre_ratings = {movie: movie_ratings.get(movie, 0) for movie in genre_movies}
    sorted_movies = sorted(genre_ratings.items(), key=lambda x: x[1], reverse=True)
    top_movies = sorted_movies[:n] if len(sorted_movies) >= n else sorted_movies
    return dict(top_movies)




# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    genre_dict = genre_to_movies
    avg_rating_dict = movie_to_average_rating

    movies_in_genre = genre_dict.get(genre, [])
    ratings_of_genre = [avg_rating_dict.get(movie, 0) for movie in movies_in_genre]
    avg_rating_of_genre = sum(ratings_of_genre) / len(ratings_of_genre) if len(ratings_of_genre) > 0 else 0
    return avg_rating_of_genre

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    genre_to_rating = {}
    for genre, movies in genre_to_movies.items():
        genre_rating = get_genre_rating(genre, genre_to_movies, movie_to_average_rating)
        genre_to_rating[genre] = genre_rating
    sorted_genres = sorted(genre_to_rating.items(), key=lambda x: x[1], reverse=True)
    if n is None or n > len(sorted_genres):
        n = len(sorted_genres)
    return dict(sorted_genres[:n])

# --- PART 4: USER FOCUSED ---

# 4.1
def read_user_ratings(f):
    user_ratings = {}
    with open(f, "r") as file:
        for line in file:
            movie, rating, user_id = line.strip().split("|")
            if user_id in user_ratings:
                user_ratings[user_id].append((movie, float(rating)))
            else:
                user_ratings[user_id] = [(movie, float(rating))]
    return user_ratings

# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    user_movie_ratings = user_to_movies
    movie_genre_dict = movie_to_genre
    user_ratings = user_movie_ratings.get(user_id, [])
    if not user_ratings:
        return None
    genre_rating = {}
    for movie, rating in user_ratings:
        genre = movie_genre_dict.get(movie)
        if not genre:
            continue
        if genre not in genre_rating:
            genre_rating[genre] = [rating]
        else:
            genre_rating[genre].append(rating)
    if not genre_rating:
        return None
    top_genre = max(genre_rating, key=lambda x: sum(genre_rating[x]) / len(genre_rating[x]))
    return top_genre

# 4.3
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    user_movies = user_to_movies
    movie_genre = movie_to_genre
    movie_ratings = movie_to_average_rating
    top_genre = get_user_genre(user_id, user_movies, movie_genre)
    unrated_movies = []
    for movie, genre in movie_genre.items():
        if genre == top_genre and movie not in [m[0] for m in user_movies[user_id]]:
            unrated_movies.append((movie, movie_ratings.get(movie, 0)))
    unrated_movies.sort(key=lambda x: x[1], reverse=True)
    return dict(unrated_movies[:3])


