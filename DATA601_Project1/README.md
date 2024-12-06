# Title: Domestic Movie Analysis from 1970-2023<br>
# DATA601 Project

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






### Available Data Sets
> * Online Movie Database API at https://www.omdbapi.com/
> * "All Released Movies: 1972-2016", https://www.imdb.com/list/ls057823854/
> * "Domestic Yearly Box Office", https://www.boxofficemojo.com/year/?grossesOption=totalGrosses

## Related Work

### Previous Research and Opinions

> * One data scientist embarked on a similar research topic.  His main conclusion was that the average ratings per movie have actually been increasing since the 2000’s (Millar-Corliss, 2018).  However, Millar-Corliss only analyzed IMDB ratings and commented that including Rotten Tomatoes and Metacritic may provide a more robust conclusion.  Additionally, he focused mainly on movies’ ratings and number of votes for his analysis.  He added that, for further insight on the subject, analyzing box office sales and gross revenue for movies against movie ratings would be insightful.
> * As for those that believe our cinema has deteriorated, based only on experience, one has proposed a theory that domestic studios have begun to cater more to the international audience than the domestic (Wilkinson, 2017).  Wilkinson’s answer to the “why” is that the international audience, especially China, simply brings in more revenue.  For instance, she compared the domestic and foreign box office sales of the top twenty domestic movies worldwide as of September 2017.  All but one of the movies had more sales internationally than domestically and by large differences. 
> * Film Courage interviewed Chris Gore, an outspoken film critic, and Gore also acknowledged the pressure of film studios to attract international viewers.  However, he also pointed out political pressures, poor studio executives, and a lack of originality in filmmaking as contributors to the problem (2021). <br>

### Background on Rating Metrics
> * First, ratings from the Internet Movie Database (IMDB), are on a point scale of 1 to 10, higher meaning a better score— and are simple averages of all votes received from IMDB members.  IMDB members can be anyone, but only one vote is permitted per user.  Interestingly, a voter may also change their vote on a movie, and the previous vote will be overwritten (IMDB, 2023).<br>

> * Next, Metacritic states that its Metascore—a point scale of 0 to 100, higher meaning a better score—is calculated by taking the weighted average of select critic reviews and publications.  Depending on the source of the reviews, those reviews will get a higher or lower weight associated with them.  Additionally for movies, the weighted averages are normalized, or graded on a curve, in order to further emphasize exceptionally good or bad scores (Metacritic Support, 2023).<br>

> * The last movie rating metric, Rotten Tomatoes, called, the “Tomatometer,” is also distinctly unique.  Similar to Metacritic, Rotten Tomatoes only takes reviews from trusted critics; however, unlike Metacritic, it uses a percentage scale based on a binary scoring system, either “positive” or “negative.”  So, if 5 out of 10 critics viewed the movie as “positive,” it would get a 50% rating.  Rotten Tomatoes also appears to have more critic reviews than Metacritic.  The rating for “The Terminator,” for instance, was calculated from 71 reviews, 50 more than Metacritic’s rating (Rotten Tomatoes; Metacritic, n.d.)<br>

>Bibliography
>
>Film Courage. (2021, May 12). Why 99% Of Movies Today Are Garbage - Chris Gore. <br>Retrieved September 2024, from YouTube web site: https://www.youtube.com/watch?v=12f0ligwS5s&t=1s<br>
>IMDB. (2023, August 18). Ratings FAQ.<br> Retrieved from IMDB Help web site: https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV?showReportContentLink=false#<br>
>Metacritic Support. (2023). How do you compute METASCORES? <br>Retrieved from Metacritic Help web site: https://metacritichelp.zendesk.com/hc/en-us/articles/14478499933079-How-do-you-compute-METASCORES
>Metacritic. (n.d.). The Terminator. <br>Retrieved from Metacritic web site: https://www.metacritic.com/movie/the-terminator/<br>
>Millar-Corliss, K. (2018, September 12). Are films getting better or worse? How do your favorite genres stack up? Do directors get better with experience?<br> Retrieved from Medium web site: https://medium.com/@kylemcorliss/are-films-getting-better-or-worse-197ad9afbf6b<br>
>Rotten Tomatoes. (n.d.). About Rotten Tomatoes.<br> Retrieved from Rotten Tomatoes web site: https://www.rottentomatoes.com/about<br>
>Rotten Tomatoes. (n.d.). The Terminator.<br> Retrieved from Rotten Tomatoes web site: https://www.rottentomatoes.com/m/terminator<br>
>Wilkinson, A. (2017, September 7). Why Hollywood keeps making the same kinds of movies, in one chart.<br> Retrieved from Vox web site: https://www.vox.com/culture/2017/9/7/16257426/box-office-global-domestic-china-mummy-furious-despicable-me-wolf-warrior<br>






