# Title: Domestic Movie Analysis from 1970-2023<br>
# DATA 601 Project

## Introduction

>* Not a few people believe that U.S. domestic movies have deteriorated in quality.  Original blockbusters like "The Godfather," "The Terminator," the Star Wars Episodes IV-VI, and more seem to be a thing of the past.  Studios and producers appear to be more interested in making animations, plot-absent, visually entertaining films, and neverending sequels than making truly original, creative films.

## Proposed Project

## Documentation
- _main.ipynb_: Provides visualization of data compiled from APIs through comprehensive lists of movies.
- _src folder_
  - _Movie.py_: Provides OOP and API functionality for movie_collection.ipynb.
  - _movie_collection.ipynb_:
    - Provides steps to extract and compile movie titles and release years from various lists and puts into no_dups_movie_year_from_1972_2023.csv.
    - Using complete .csv file, it requests data on movies from OMDB and TMDB APIs.
- _data folder-
  - _no_dups_movie_year_from_1972_2023.csv_: Complete list of movie titles and release years to be used for API requests.
  - _movie_data.csv_: Complete list of all movies titles and data compiled from APIs.
  - Various HTML lists of movie titles and release years from IMDB for web-scraping.

### APIs Used
> * Online Movie Database (OMDB) at https://www.omdbapi.com/
> * The Movie Database (TMDB) at https://developer.themoviedb.org/docs/getting-started
