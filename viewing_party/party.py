# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

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

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

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

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_watched = []
    set_user_mov_titles = set()
    set_mov_friends_titles = set()

    # create set of friends movies titles
    for fr_watched in user_data["friends"]:
        for mov in fr_watched["watched"]:
            set_mov_friends_titles.add(mov["title"])
        
    # create set of user movies titles
    for movie in user_data["watched"]:
        set_user_mov_titles.add(movie["title"])

    # compare sets to determine only those that only user have seen
    unique_titles = set_user_mov_titles.difference(set_mov_friends_titles)
    
    # add those unique movies to a list of movies based on title
    for movie in user_data["watched"]:
        if movie["title"] in unique_titles:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):
    unique_watched = []
    set_user_mov_titles = set()
    set_mov_friends_titles = set()

    # create set of friends movies titles
    for fr_watched in user_data["friends"]:
        for mov in fr_watched["watched"]:
            set_mov_friends_titles.add(mov["title"])

    # create set of user movies titles
    for movie in user_data["watched"]:
        set_user_mov_titles.add(movie["title"])

    # compare sets to determine only those that user have never seen
    unique_titles = set_mov_friends_titles.difference(set_user_mov_titles)

    # add those movies to the list based on titles
    for fr_watched in user_data["friends"]:
        for mov in fr_watched["watched"]:
            if mov["title"] in unique_titles and mov not in unique_watched:
                unique_watched.append(mov)
            
    return unique_watched
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_watched = get_friends_unique_watched(user_data)
    recommended_movies = []

    for movie in friends_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    # first get all recommended movies
    recommended_movies = get_friends_unique_watched(user_data)
    
    recommended_by_genre = []
    genres_count = {}
    
    # make a dictionary where genre is key and 
    # how many times genre watched is value
    if not user_data["watched"]:
        return []
    else:
        for movie in user_data["watched"]:
            genres_count[movie["genre"]] = genres_count.get(movie["genre"], 0) + 1
    
    # determine which genre is the most watched
    # using genres_count dictionary
    most_watched_genre = None
    times = 0
    for genre, count in genres_count.items():
        if count > times:
            most_watched_genre = genre
            times = count
    
    # make a list of recommendations by genre
    for movie in recommended_movies:
        if movie["genre"] == most_watched_genre:
            recommended_by_genre.append(movie)
    
    return recommended_by_genre

