# Title: Domestic Movie Analysis from 1970-2023<br>
# DATA 601 Project<br>

#### Authors: 
>* Tyler Snow
>* Brian Englum
>* Joel Wheatley
>* Manoj Kumar Pasupuleti

## Introduction

>* Many movie fans and film critics believe that U.S. domestic movies have deteriorated in quality over time. Classic blockbusters like "The Godfather," "The Terminator," and Star Wars Episodes IV-VI seem to be a thing of the past. Studios and producers appear to be more interested in making animations; plot-absent, visually entertaining films; and never-ending sequels than making truly original, creative films. Although viewers and critics may feel this way, little research has been done on the topic.
>* The goal of this project is to use statistical analysis and data science tools to explore this topic and answer the question of whether domestic movies have deteriorated in quality.  To view the topic from multiple angles, movie ratings, box office sales, and awards data from the Online Movie Database (OMDB) and The Movie Database (TMDB) APIs will all be used and analyzed.   

## Conclusion

>* Historically high ratings and box office sales were observed in the late 1970’s, and exceptional movie-rating highs, in the mid to late 2010's.  Additionally, theatre sales were observed to peak near 2002 and gradually decrease, until the COVID-19 pandemic and the streaming service surge of 2019, which both caused this decrease to plunge and never recover.  Nonetheless, despite these exceptions, very few consistent trends were observed through the decades analyzed.  In fact, apart from these exceptions, the quality of movies—when viewed from multiple angles — appears to go up and down randomly in periods of two or three years.  Therefore, in response to the project’s hypothesis that “domestic movies have gotten worse,” domestic cinema has simply not been observed to have gotten worse, at least through statistical analysis.  One explanation for why one may feel otherwise may be the phenomenon of "rosy retrospection", or nostalgia.   In this case, we only remember the best movies from the past and focus on the worst in the present.  So, we falsely associate the present as the worst when it has, in fact, been better than times in the past.  For instance, in recent history, the period between 2013 and 2019 produced many highly rated movies and was the longest observed since 1970.  

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

### References

1. Why 99 Percent Of Movies Today Are Garbage — Chris Gore | by Film Courage write.film.create | Film Courage | Medium [Internet]. [cited 2024 Sep 21]. <br>
Available from: https://medium.com/film-courage/why-99-percent-of-movies-today-are-garbage-chris-gore-37b19ecb2602

2. Are Movies Getting Better? : Planet Money : NPR [Internet]. [cited 2024 Sep 21]. <br>
Available from: https://www.npr.org/sections/money/2019/02/19/695758291/are-movies-getting-better

3. Why does Hollywood keep making the same movies, even when they flop? | Vox [Internet]. [cited 2024 Sep 21]. <br>
Available from: https://www.vox.com/culture/2017/9/7/16257426/box-office-global-domestic-china-mummy-furious-despicable-me-wolf-warrior

4. Are films getting better or worse? How do your favorite genres stack up? Do directors get better with experience? | by Kyle Millar-Corliss | Medium [Internet]. [cited 2024 Sep 21]. <br>
Available from: https://medium.com/@kylemcorliss/are-films-getting-better-or-worse-197ad9afbf6b

5. IMDb | Help [Internet]. [cited 2024 Sep 21].<br>
Available from: https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV?showReportContentLink=false#

6. About | Rotten Tomatoes [Internet]. [cited 2024 Sep 21]. <br>
Available from: https://www.rottentomatoes.com/about

7. How do you compute METASCORES? – Metacritic Support [Internet]. [cited 2024 Sep 21]. <br>
Available from: https://metacritichelp.zendesk.com/hc/en-us/articles/14478499933079-How-do-you-compute-METASCORES

8. Domestic Yearly Box Office - Box Office Mojo [Internet]. [cited 2024 Sep 21]. <br>
Available from: https://www.boxofficemojo.com/year/?grossesOption=totalGrosses 

9. All U.S. Released Movies: 1970-2016 [Internet]. [cited 2024 Sep 21]. <br>
Available from: https://www.imdb.com/list/ls057823854/ 

10. OMDb API - The Open Movie Database [Internet]. [cited 2024 Sep 21]. <br>
Available from: https://www.omdbapi.com/ 

11. About TMDB – The Movie Database (TMDB) [Internet]. [cited 2024 Oct 29]. <br>
Available from: ​https://www.themoviedb.org/about?language=en-USS 

12. The Oscar Award, 1927 – 2024 [Internet]. [cited 2024 Dec 8].  <br>
Available from: https://www.kaggle.com/datasets/unanimad/the-oscar-award

13. Streaming media | Definition, History, & Facts | Britannica. [cited 2024 Nov 11]. <br>
Available from: https://www.britannica.com/technology/streaming-media 

14. Rosy Introspection - The Decision Lab. [cited 2024 Dec 09]. <br>
Available from: https://thedecisionlab.com/biases/rosy-retrospection 

15. Bureau of Labor Statistics Data. [cited 2024 Dec 09]. <br>
Available from: https://data.bls.gov/timeseries/CUUR0000SA0L1E?output_view=pct_12mths 

16. The Movies Dataset. [cited 2024 Dec 09].  <br>
Available from: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?				                                                                resource=download&select=movies_metadata.csv 

17. Domestic Yearly Box Office | Box Office Mojo. [cited 2024 Dec 09]. <br>
Available from: https://www.boxofficemojo.com/year/?ref_=bo_nb_hm_secondarytab 
