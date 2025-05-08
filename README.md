
# Movie Recommender System 🎥

A **Content-Based Movie Recommender System** built using **Streamlit** for the frontend, **Pandas** for data processing, and **Scikit-learn** for vectorization and similarity computation. This system takes user input (a movie name), processes the data, applies a content-based recommendation algorithm, and returns top movie recommendations.

## Features 🌟
- **Movie Selection**: Users can select a movie from a dropdown list.
- **Content-Based Recommendation**: The system suggests movies based on the similarity of content (e.g., descriptions, genres, etc.).
- **Streamlit Frontend**: A clean and interactive UI where users can interact with the recommender system.
- **ML Model**: The recommendation system uses **content-based filtering**, where movies are recommended based on their similarity to the selected movie.

## Tech Stack 🛠️
- **Streamlit**: For building the interactive web interface.
- **Pandas**: For data loading, cleaning, and processing.
- **Scikit-learn**: For vectorization (TF-IDF) and computing similarity scores.
- **Pickle**: For loading pre-trained models and similarity matrix.
- **NumPy**: For numerical operations during vectorization.

## How It Works 🔍
1. **Data Preprocessing**: The raw movie data is processed using Pandas. Key features, like descriptions and genres, are extracted and vectorized into numerical representations.
2. **Content-Based Filtering**: Using **TF-IDF vectorization** and **cosine similarity**, the system computes the similarity between movies based on their content (e.g., movie descriptions, genres).
3. **Recommendation**: When a user selects a movie, the system retrieves the top 5 most similar movies based on the cosine similarity of their content.

## Application Workflow 📊
- **User Interface**:
  - The user selects a movie from a dropdown list.
  - Upon clicking the **"Recommend"** button, the system processes the input and displays the top 5 recommended movies based on content similarity.
- **Backend Process**:
  - The system uses **TF-IDF vectorization** to convert movie descriptions and features into numerical representations.
  - **Cosine similarity** is computed between the vectors to suggest movies with the highest content-based similarity.

