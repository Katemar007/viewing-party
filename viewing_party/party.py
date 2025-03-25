# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if not title or not genre or not rating:
        return None
    else:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data   

def watch_movie(user_data, movie):
    # If the movie is the watchlist, it's moved from the watchlist 
    # to the watched
    for i in range(len(user_data["watchlist"])):
        if movie == user_data["watchlist"][i]["title"]: 
            user_data["watched"].append(user_data["watchlist"][i])
            del user_data["watchlist"][i]
    return user_data    

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    count = 0
    sum_ratings = 0
    for movie in user_data["watched"]:
        sum_ratings += movie["rating"]
        count += 1
    avg_rating = sum_ratings/count

    return avg_rating

def get_most_watched_genre(user_data):
	
    from collections import Counter

    if not user_data["watched"]:
        return None

    genres = (g["genre"] for g in user_data["watched"])
    number_genres = Counter(genres)
    max_genre = max(number_genres, key=number_genres.get)
    
    return max_genre

def get_unique_watched(user_data):
    unique_watched = []
    set_user_mov_titles = set()
    set_mov_friends_titles = set()

    for fr_watched in user_data["friends"]:
        for mov in fr_watched["watched"]:
            set_mov_friends_titles.add(mov["title"])
    
    for movie in user_data["watched"]:
        set_user_mov_titles.add(movie["title"])

    unique_titles = set_user_mov_titles.difference(set_mov_friends_titles)

    for movie in user_data["watched"]:
        if movie["title"] in unique_titles:
            unique_watched.append(movie)

    return unique_watched






        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

