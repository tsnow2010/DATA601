# Movie.py for Project 1 (DATA 601)
# CAO 10/24/2024
# By: Tyler Snow

# This script defines Movie class and its functions to make requests to the OMDB and TMDB APIs, located at 'http://www.omdbapi.com' and 'https://api.themoviedb.org', and writes data to a .csv to later analyze
# ratings from IMDB, Rotten Tomatos, Metacritic, and TMDB.

import requests
import json
import csv
import threading
import re
from bs4 import BeautifulSoup


class Movie:

    # Creates instance of Movie with title and year.
    def __init__(self, title,year):
        self.title = title
        self.year = year

    # Pulls title and year from provided HTML files
    @staticmethod
    def get_titles_from_html(files, write_file):

        with open (write_file,'a') as file2:
            writer = csv.writer(file2,delimiter=',')

            for file in files:
                year = file[60:64]
        
                # Pulls movie data from former HTML files obtained from Box Office Mojo using regex, and appends titles to movie_titles<list>
                movie_titles = []
                cleaned_movie_titles = []
        
                # Open HTML file and use regex to pull movie titles and writes this data to movie_year_from_1972_2023.csv
                with open (file,'r') as file1:
                    for line in file1:
                        # Skips lines with no movie titles
                        if (re.findall('_+[0-9]{1,3}.{2,60}</a{1}',line)) == []:
                            continue
                        # Splits lists with multiple movie titles and appends to list
                        elif len(re.findall('_+[0-9]{1,3}.{2,60}</a{1}',line)) > 1:
                            mult_movies = re.findall('_+[0-9]{1,3}.{2,60}</a{1}',line)
                            while len(mult_movies) != 0:
                                movie_titles.append([mult_movies.pop()])
                        # Appends all other movie titles to list
                        else:
                            movie_titles.append(re.findall('_+[0-9]{1,3}.{2,60}</a{1}',line))
        
                # Removes first item in list, as it's not wanted
                movie_titles.pop(0)
                
                # Cleans each title, removing unwanted marks
                for movie in movie_titles:
                    cleaned_movie_titles.append(movie[0][:-3].split('"')[1][1:])
                    
                    for title in cleaned_movie_titles:
                        writer.writerow([title,year])

    # This function pulls titles and years from file, 'us_released_movies_1972_to_2016.csv',
    # and writes this data to movie_year_from_1972_2023.csv.
    def get_titles_from_csv(file_names, write_file):
        csv_file = open(write_file,'w')
        writer = csv.writer(csv_file,delimiter=',')
        writer.writerow(['title','year'])

        files = [open(file_name, 'r') for file_name in file_names]
        
        for file in files:
            
            reader = csv.reader(file, delimiter=',')
            next(reader)
            
            for row in reader:
                writer.writerow([row[5],row[11]])
            
        for file in files: 
            file.close()
            
        csv_file.close()
        
    # Takes movie titles from Wikipedia pages, https://en.wikipedia.org/wiki/List_of_American_films_of_{year}, and appends to .csv file.
    def get_titles_from_webscraping(write_file):
            
        with open (write_file,'a') as file2:
            writer = csv.writer(file2,delimiter=',')
    
            # Parses text from Wikipedia webpages listing all domestic movies made a specific year.
            for year in range(1972,2024,1):
                url = f'https://en.wikipedia.org/wiki/List_of_American_films_of_{year}'
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
            
                all_text = soup.get_text()
                movie_set = set()
    
                # Finds titles starting with capital letter followed by lowercase letter.
                movies = re.findall('\n{2}[A-Z][a-z].+\n[A-Z]',all_text)
    
                # Finds titles starting with 1-3 numbers, i.e. 12 Years a Slave, 300, etc.
                movies2 = re.findall('\n{2}\d{1,3}.+\n[A-Z]',all_text)
                movies += movies2
    
                # Cleans movie titles from lines taken from previous step and adds clean titles to movie_set.
                for raw_movie in movies:
                    raw_movie = raw_movie[0:-1]
                    if '_' in raw_movie:
                         continue
                    elif ('(' in raw_movie) or (')' in raw_movie):
                         continue
                    elif '=' in raw_movie:
                         continue
                    elif ('[' in raw_movie) or (']' in raw_movie):
                        continue
                        
                    movie = re.findall('(?<=\n\n).+', raw_movie)               
                    movie_set.add(movie[0])
                    
                # Removes persistent non-titles in movie_set.
                movie_set.discard('Privacy policy')
                movie_set.discard('Rank')
    
                # Write movie titles with year to .csv file.
                for movie in movie_set:
                    writer.writerow([movie, year])
                    
                # Clear set for next iteration.
                movie_set.clear()
                    
# This function requests movie data from the OMDB for all movies made in a certain year.  It writes the results in 'movies_in_<year>.csv'.

    def get_movie_data(self):
        # Assigns API key to API URL
        OMDB_url = 'http://www.omdbapi.com/?apikey={}&'.format('7a34ecb8')
        TMDB_url = "https://api.themoviedb.org/3/search/movie" #API Key: 8179a3ac6c176723c5d4437365ec76e5.    https://api.themoviedb.org/3/authentication

        # Request movie data from OMDB using title and year made, and return in JSON format.
        request1 = requests.get(OMDB_url, params={'t': self.title, 'y': self.year, 'r': 'json', 'type':'movie'})
        request2 = requests.get(TMDB_url, params={'query': self.title, 'year': self.year, 'api_key': '8179a3ac6c176723c5d4437365ec76e5'})

        # Turns requests into JSON format.  Exception handling allows requests to repeat after 5-second delay.      
        try:
            request_JSON1 = request1.json()
        except:
            print(f"Error occurred with request to OMDB regarding {self.title,self.year}.")
            
        try:    
            request_JSON2 = request2.json()
        except:
            print(f"Error occurred with request to TMDB regarding {self.title,self.year}.")
            
        # - Assigns attributes to instance
        # - Below exception handling prevents index errors from interrupting function.
        # - Some movies do not have a rating from some DBs.
        try:
          self.genre = request_JSON1['Genre']
        except:
          self.genre = None
        try:
          self.imdb = request_JSON1['imdbRating']
        except:
          self.imdb = None
        try:
          self.rntm = str(request_JSON1['Ratings'][1]['Value'])[:-1]
        except:
          self.rntm = None
        try:
          self.meta = request_JSON1['Metascore']
        except:
          self.meta = None
        try:
          self.tmdb = request_JSON2['results'][0]['vote_average'] # Gets error, some movies not in database
        except:
          self.tmdb = None
        try:
          self.num_awards = request_JSON1["Awards"]
        except:
          self.num_awards = None
        try:
          self.num_imdb_votes = request_JSON1["imdbVotes"]
        except:
          self.num_imdb_votes = None
        try:
          self.box_office = request_JSON1["BoxOffice"]
        except:
          self.box_office = None
        try:
          self.media = request_JSON1["Type"]
        except:
          self.media = None # Is it a movie, show, mini-show, etc?
        try:
          self.directors = request_JSON1["Director"]
        except:
          self.directors = None
        try:
          self.origin = request_JSON1["Country"]
        except:
          self.origin = None

        # Opens new .csv file for writing data and names the file by year.  For an example for all movies made domestically in 1984, it will be named 'movies_in_1984'.  File will contain movie data made domestically in one year.
        file = open('movie_data.csv', 'a')

        # Writes title and movie ratings in the order of the dict made above and closes the file.
        new_csv = csv.writer(file)
        new_csv.writerow([self.title,
                          self.year,
                          self.genre,
                          self.imdb,
                          self.rntm,
                          self.meta,
                          self.tmdb,
                          self.num_imdb_votes,
                          self.num_awards,
                          self.box_office,
                          self.media,
                          self.directors,
                          self.origin]
                          )
        print('This was written to movie_data.csv:', self.title, self.year)

        # Un-comment below to see the results from the API requests:

        #print(json.dumps(request_JSON1, indent=2))
        #print(json.dumps(request_JSON2, indent=2))
        file.close()
