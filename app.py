import pandas as pd
import streamlit as st
import pickle


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  ##fetching the index of the given movie.
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    #recommended_movies_poster=[]
    for i in movies_list:
        #movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        #recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies#, recommended_movies_poster


movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')#creating heading

#makeing a block
selected_movie_name = st.selectbox(
'ENETER THE MOVIE NAME:',
movies['title'].values)

#  making button
if st.button('Recommend'):
   recommendation= recommend(selected_movie_name)
   for i in recommendation:
       st.write(i)


