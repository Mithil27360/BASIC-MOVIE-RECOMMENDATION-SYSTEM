# Movie Recommender

This is a simple Flask-based web application that recommends movies based on selected genres.

## Project Structure
movie_recommender/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── recommend.html
│
├── movies.csv
├── app.py
├── requirements.txt
└── README.md



## Features
- Select a genre and get top-rated movie recommendations.
- Displays movie details like title, rating, genre, description, and more.

## Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

## Setup Instructions
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/movie_recommender.git
    cd movie_recommender
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python app.py
    ```
4. Open your browser and go to `http://127.0.0.1:5000`.

## Dependencies
- Flask
- pandas

## License
This project is licensed under the MIT License - see the LICENSE file for details.
