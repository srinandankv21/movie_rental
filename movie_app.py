# movie_app.py

from datetime import date

class Review:
    def __init__(self, review_id, movie_id, user_id, rating, review_text):
        self.review_id = review_id
        self.movie_id = movie_id
        self.user_id = user_id
        self.rating = rating
        self.review_text = review_text

    def get_review_details(self):
        return {
            "review_id": self.review_id,
            "movie_id": self.movie_id,
            "user_id": self.user_id,
            "rating": self.rating,
            "review_text": self.review_text,
        }


class Movie:
    def __init__(self, movie_id, title, description, release_date):
        self.movie_id = movie_id
        self.title = title
        self.description = description
        self.release_date = release_date
        self.rating = 0.0
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)
        self.calculate_average_rating()

    def calculate_average_rating(self):
        if not self.reviews:
            self.rating = 0.0
        else:
            total = sum(review.rating for review in self.reviews)
            self.rating = total / len(self.reviews)


class User:
    def __init__(self, user_id, username, password, email):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.favorites = []

    def search_movies(self, movies, keyword):
        return [movie for movie in movies if keyword.lower() in movie.title.lower()]

    def add_to_favorites(self, movie):
        if movie not in self.favorites:
            self.favorites.append(movie)

    def rate_movie(self, movie, rating, review_text):
        movie.add_review(Review(f"rev-{len(movie.reviews) + 1}", movie.movie_id, self.user_id, rating, review_text))


class Admin:
    def __init__(self, admin_id, username, password):
        self.admin_id = admin_id
        self.username = username
        self.password = password

    def manage_movies(self, movie_list, movie):
        movie_list.append(movie)

    def delete_movie(self, movie_list, movie_id):
        movie_list[:] = [movie for movie in movie_list if movie.movie_id != movie_id]


# Sample movie data (in-memory)
movies = [
    Movie("1", "Inception", "A mind-bending thriller", date(2010, 7, 16)),
    Movie("2", "Interstellar", "A journey through space and time", date(2014, 11, 7)),
]
