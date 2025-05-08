import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Background image
bg_img_url = "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bW92aWUlMjByZXZpZXd8ZW58MHx8MHx8fDA%3D"

# Custom styles
custom_style = f"""
<style>
    .stApp {{
        background-image: url("{bg_img_url}");
        background-size: cover;
        background-position: center;
    }}
    h1 {{
        color: red !important;
        font-size: 3rem !important;
        text-align: center;
    }}
    .custom-subheader {{
        color: white;
        font-size: 2.2rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 5px black;
    }}
    .recommend-title {{
        color: yellow;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
        text-shadow: 2px 2px 4px black;
    }}
    .stMarkdown h3 {{
        color: pink;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
    }}
    div[data-baseweb="select"] > div {{
        width: 100% !important;
        margin: auto;
        font-size: 1.2rem;
        color:black;
        font-weight: bold;


    }}
    button[kind="primary"] {{
        background-color: red !important;
        color: white !important;
        font-weight: bold;
        text-align:center
        width: 200px;
        display: block;
        margin: 20px auto;
    }}
</style>
"""
st.markdown(custom_style, unsafe_allow_html=True)

# Title
st.title('🎥 Movie Recommender System')
st.markdown('<div class="custom-subheader">Select a movie you like:</div>', unsafe_allow_html=True)

# Selection box
selected_movie_name = st.selectbox('', movies['title'].values)

# Recommend button
if st.button('Recommend'):
    names = recommend(selected_movie_name)
    st.markdown('<div class="recommend-title">🎬 Top 5 Recommended Movies:</div>', unsafe_allow_html=True)
    for name in names:
        st.markdown(f'<h3>{name}</h3>', unsafe_allow_html=True )