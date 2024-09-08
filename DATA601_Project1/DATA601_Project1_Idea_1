# This script lists functions to make requests to the OMDB API, located at 'http://www.omdbapi.com/?apikey=[yourkey]&', and writes data to a .csv to later analyze
# ratings from IMDB, Rotten Tomatos, and Metacritic.

import requests
import json
import csv

# This function requests movie data, at least ratings are expected, for all movies made in a certain year.  It writes the results in 'movies_in_<year>.csv'.

def get_movie_ratings(title: str, year: int, api_key: str):
    # Assigns API key to API URL
    updated_url = 'http://www.omdbapi.com/?apikey={}&'.format(api_key)
    
    print(updated_url)
    # Request movie data from title and year made, and return in JSON format.
    request_NaJSON = requests.get(updated_url, params={'t': title, 'y': year, 'r': 'json', 'type':'movie'})
    
    # Turns request into JSON format.
    request = request_NaJSON.json()

    # Look at formatting of dict
  

    # Makes dict with the movie's IMDB rating, Rotten Tomato rating, and Metascore rating.
    movie_ratings = {'imbd': request['imdbRating'], 'rotten_tom': str(request['Ratings'][1]['Value'])[:-1], 'metascore': request['Metascore']}
    
    # Opens new .csv file for writing data and names the file by year.  For an example for all movies made domestically in 1984, it will be named 'movies_in_1984'.  File will contain movie data made domestically in one year.
    file = open('movies_in_{}.csv'.format(year), 'w')

    # Writes title and movie ratings in the order of the dict made above and closes the file.
    new_csv = csv.writer(file)
    new_csv.writerow([title, movie_ratings['imbd'], movie_ratings['rotten_tom'], movie_ratings['metascore']])
    print('This was written to', 'movies_in_{}.csv'.format(year) + ':', "'" + title, movie_ratings['imbd'], movie_ratings['rotten_tom'], movie_ratings['metascore'] + "'")
    file.close()

# Test the functionality of method
get_movie_ratings("The Terminator", 1984, '7a34ecb8')

# Below commented lines can be used for testing.

#print(request_NaJSON.url)
#print(request_NaJSON.text)
#print(json.dumps(request, indent = 2))

# FOLLOW UP WORK:

# Need to get list of domestic movie titles and years made.
##### Movie titles and years may be found at https://www.imdb.com/list/ls057823854/?view=compact&sort=user_rating%2Cdesc.

#----------------------------------------------------------------------#
# Idea for Project 1_DATA 601
# CAO 09/08/2024
# By: Tyler Snow





                   
    
