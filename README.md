# UNIT-1-PROJECT



## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI.
- Use your coding skills in Python accurately.
- Organize Your Code into modules & (or packages)




## MovieMate: Your Personal Movie Recommendation System 🌟

### Overview:

MovieMate is an interactive command-line interface (CLI) application designed to help you discover and explore movies. By searching for a movie title, you can view detailed information about the selected movie and receive personalized recommendations for similar movies. MovieMate reads data from a comprehensive movie dataset, providing a seamless and user-friendly experience.



## Features:
### As a user, you should be able to:
- Search for movies by title.
- View details of the selected movie (title, genre, country, year).
- Get recommendations based on the selected movie.
- Choose to continue searching for more movies or quit the application.



## Usage:
Explain to the user how to use your project:
- Type in the name of the movie when prompted to search for a movie.
- If multiple movies are found, type in the index of the movie you are interested in.
- If only one movie is found, it will be automatically selected.
- After viewing the movie details and recommendations, you will be asked if you want to search for another movie or quit the application.



## Code Organization:
### Modules:
- `main.py`: The main entry point for the application, handles user interaction and flow.
- `recommender.py`: Contains the logic for getting movie recommendations based on the selected movie.

### Functions:
- `main()`: Handles the main program logic, including user input and output.
- `color_genre()`: Applies color formatting to the genre for better visual distinction.
- `get_recommendations()`: Provides movie recommendations based on the selected movie.



## Dataset:
### Source:
The dataset used in this project is sourced from [FilmTV.it](https://www.filmtv.it) and was scraped as of October 21, 2023. It is available on [Kaggle](https://www.kaggle.com/datasets/stefanoleone992/filmtv-movies-dataset/data).

### Content:
Each row in the dataset represents a movie available on FilmTV.it, with the following attributes:

- `filmtv_id`: FilmTV ID (e.g., data for movie ID 2 was scraped from FilmTV).
- `title`: Movie original title.
- `year`: Movie year of release.
- `genre`: Movie genre.
- `description`: Movie description.
- `country`: Countries where the movie was filmed.

##### Their Usage:
title used for searching movies  |  year used for sorting and displaying movies  |  genre used for color coding in the CLI  |  description based recommendation.


###### Not used attributes
- `duration`: Movie duration (in minutes).
- `directors`: Name of movie directors.
- `actors`: Name of movie actors.
- `avg_vote`: Average rating, considering votes expressed by critics and the public.
- `critics_vote`: Average vote expressed by critics (if available).
- `public_vote`: Average vote expressed by the public (if available).
- `total_votes`: Total votes expressed by critics and the public.
- `notes`: Movie notes.
- `humor`: Movie humor score given by FilmTV.
- `rhythm`: Movie rhythm score given by FilmTV.
- `effort`: Movie effort score given by FilmTV.
- `tension`: Movie tension score given by FilmTV.
- `erotism`: Movie erotism score given by FilmTV.






## Packages Used:
### pandas
- **Description**: A powerful data manipulation and analysis library for Python. It provides data structures like DataFrames that are essential for handling and analyzing structured data.
- **Usage in Project**: Used to read, process, and manipulate the movie data from the CSV file.

### tabulate
- **Description**: A library to format tabular data in plain-text tables.
- **Usage in Project**: Utilized to display the list of movies and recommendations in a structured, visually appealing table format.

### colorama
- **Description**: A library for producing colored terminal text and cursor positioning on Windows, Linux, and Mac.
- **Usage in Project**: Used to add color to text in the terminal, making the CLI output more user-friendly and visually distinct by coloring movie genres and other messages.

### numpy
- **Description**: A fundamental package for scientific computing in Python, providing support for arrays and matrices, along with a collection of mathematical functions to operate on these data structures.
- **Usage in Project**: Used to handle NaN values in the dataset and perform numerical operations as needed.

