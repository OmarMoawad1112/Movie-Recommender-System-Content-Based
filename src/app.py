import streamlit as st
import pickle

movies = pickle.load(open('../artifacts/movies.pkl','rb'))
similarity = pickle.load(open('../artifacts/similarity.pkl','rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

st.title("Movie Recommender System")

selected_movie = st.selectbox("Choose a movie", movies['title'].values)

if st.button("Recommend"):
    results = recommend(selected_movie)

    st.subheader("Top Picks 🍿")

    cols = st.columns(3)

    for i, movie in enumerate(results):
        with cols[i % 3]:
            st.info(f"🎬 {movie}")