# app.py

import streamlit as st
from movie_app import User, Admin, Movie, Review, movies

# Create a sample user and admin for demonstration purposes
current_user = User("user1", "JohnDoe", "password123", "john@example.com")
admin = Admin("admin1", "Admin", "adminpass")

st.title("Movie App")

# Movie search
st.header("Search for Movies")
search_keyword = st.text_input("Enter movie title to search:")
if st.button("Search"):
    results = current_user.search_movies(movies, search_keyword)
    if results:
        for movie in results:
            st.subheader(movie.title)
            st.write(movie.description)
            st.write(f"Release Date: {movie.release_date}")
            st.write(f"Average Rating: {movie.rating:.1f}")
            
            if st.button(f"Add {movie.title} to Favorites"):
                current_user.add_to_favorites(movie)
                st.success(f"{movie.title} added to favorites!")

            rating = st.slider("Rate this movie:", 1, 5, key=movie.movie_id)
            review_text = st.text_input("Leave a review:", key=f"review_{movie.movie_id}")
            if st.button(f"Rate and Review {movie.title}"):
                current_user.rate_movie(movie, rating, review_text)
                st.success(f"Rated {movie.title} with {rating} and added review!")

    else:
        st.write("No movies found.")

# Viewing favorites
st.header("Your Favorites")
if current_user.favorites:
    for movie in current_user.favorites:
        st.subheader(movie.title)
        st.write(movie.description)
else:
    st.write("You have no favorite movies yet.")
