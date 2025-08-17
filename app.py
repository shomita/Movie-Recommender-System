# app.py
import streamlit as st
import pickle
import joblib

# ---- Load Data ----
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = joblib.load("similarity.pkl")

# ---- Recommendation Function ----
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# ---- Page Config ----
st.set_page_config(page_title="Movie Recommender 🎬", layout="wide")

# ---- Custom CSS Styling ----
st.markdown("""
    <style>
    .main-title {
        font-size:40px;
        text-align:center;
        color:#ff4b4b;
        font-weight:700;
        margin-bottom:30px;
    }
    .movie-box {
        background: linear-gradient(135deg, #2b2b52, #24243e);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-size: 18px;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        margin: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- App Title ----
st.markdown("<div class='main-title'>🎥 Movie Recommender System</div>", unsafe_allow_html=True)

# ---- Movie Selection ----
selected_movie = st.selectbox(
    "Search for a movie you like 👇",
    movies['title'].values
)

# ---- Recommend Button ----
if st.button("🔍 Recommend Movies"):
    names = recommend(selected_movie)

    st.subheader("✨ Recommended for You:")
    cols = st.columns(5)

    for col, name in zip(cols, names):
        with col:
            st.markdown(
                f"<div class='movie-box'>{name}</div>",
                unsafe_allow_html=True
            )
