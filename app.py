import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


st.title("Recommendation System")
search = st.selectbox("Select a movie :" , movies["title"])


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

if st.button("Recommend"):
    recommended_movie_names = recommend(search)
    st.write("Recommended Movies:")
    for i in recommended_movie_names:
        st.write(f"{i}")
    