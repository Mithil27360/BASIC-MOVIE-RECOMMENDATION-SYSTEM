# app.py
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)


def load_movies():
    df = pd.read_csv('movies.csv')
    # Clean the Title column to remove year
    df['Title'] = df['Title'].str.extract(r'(.*?)(?:\s*\([^)]*\))?$')[0]
    return df


@app.route('/')
def index():
    movies_df = load_movies()
    genres = movies_df['Genre'].str.split(', ').explode().unique()
    return render_template('index.html', genres=sorted(genres))


@app.route('/recommend', methods=['POST'])
def recommend():
    selected_genre = request.form.get('genre')

    # Load and filter movies
    movies_df = load_movies()
    # Filter movies that contain the selected genre
    filtered_movies = movies_df[movies_df['Genre'].str.contains(selected_genre, na=False)]

    # Sort by rating (descending)
    recommended_movies = filtered_movies.sort_values('Rate', ascending=False)

    return render_template('recommend.html',
                           movies=recommended_movies.to_dict('records'),
                           selected_genre=selected_genre)


if __name__ == '__main__':
    app.run(debug=True)