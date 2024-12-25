import streamlit as st
from main import recommend, movies

# Streamlit app title
st.title("Movie Recommendation System 🎥")
st.write("Find movie recommendations and their posters based on your favorite movies!")

# Dropdown to select a movie
movie_option = st.selectbox("Select a movie:", movies['title'].values)

# Button to generate recommendations
if st.button("Recommend"):
    recommended_names, recommended_posters = recommend(movie_option)

    # Display recommendations
    if recommended_names:
        st.write(f"Recommendations for **{movie_option}**:")
        cols = st.columns(5)  # Create 5 columns for displaying posters
        for i, col in enumerate(cols):
            with col:
                st.text(recommended_names[i])
                st.image(recommended_posters[i])
    else:
        st.error("No recommendations found. Try another movie.")
