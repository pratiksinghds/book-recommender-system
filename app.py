import os
import pickle
import streamlit as st
import numpy as np

# Set Header
st.header('Book Recommender System Using Machine Learning')

# Load Pickled Artifacts (paths relative to this file so it runs from any working directory)
ARTIFACTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'artifacts')
model = pickle.load(open(os.path.join(ARTIFACTS, 'model.pkl'), 'rb'))
books_name = pickle.load(open(os.path.join(ARTIFACTS, 'books_name.pkl'), 'rb'))
final_rating = pickle.load(open(os.path.join(ARTIFACTS, 'final_rating.pkl'), 'rb'))
book_pivot = pickle.load(open(os.path.join(ARTIFACTS, 'book_pivot.pkl'), 'rb'))


def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        # Fix HTTP to HTTPS Conversion
        if url.startswith('http://'):
            url = url.replace('http://', 'https://')
        poster_url.append(url)

    return poster_url


def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url = fetch_poster(suggestion[0])

    for i in range(len(suggestion[0])):
        books = book_pivot.index[suggestion[0][i]]
        books_list.append(books)

    return books_list, poster_url


selected_books = st.selectbox(
    "Type or select a book",
    books_name
)

if st.button('Show Recommendation'):
    recommendation_books, poster_url = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])

    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])

    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])

    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5])
