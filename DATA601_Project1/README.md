# Title: Domestic Movie Analysis from 1972-2016<br>
# DATA601: Project 1

## Introduction

>* Not a few people believe that U.S. domestic movies have deteriorated in quality.  Original blockbusters like "The Godfather," "The Terminator," the Star Wars Episodes IV-VI, and more seem to be a thing of the past.  Studios and producers appear to be more interested in making animations, plot-absent, visually entertaining films, and neverending sequels than making truly original, creative films.

## Proposed Project

### Problem:

>* While many people may feel, by experience, that domestic cinema has deteriorated, comprehensive research and data analysis proving this claim lacks.  Put simply, the proposed research aims to answer the following: Have domestic films deteriorated in quality in the last five decades, or not? <br>
>
>* Suggested data analysis includes the following:<br>

# JOEL/STATS INFO

# NEED TO CLEAN THE SECTION BELOW (WOULD BE GOOD FOR LAYING OUT HOW WE PLAN TO FULFILL CRITERIA)

### Fulfilling Project Criteria:

Other criteria required in the project (3 out of 11):
	1. Object oriented code - creating object with Movie data where cleaning, transformation, and analysis will be performed 
	2. Intricate file management/manipulation (not just simply reading and writing of 1-2 files)
		a. Combining data from multiple sources via APIs
	3. Data cleaning and/or Data transformation
	4. Numerical computation / Mathematical processing
		a. Create binary or multilevel rating categories
		b. Convert Gross Box Office income to US$ year 2000 for comparison
			i. Normalize data if varies widely by decade
		c. Create overall/combined rating
			i. Evaluate rating centrality and spread
			ii. Transform/normalize ratings to they can be combined without 1 system dominating
	5. Regular Expression
		a. If we incorporate directors, cast members or titles in our analysis, we may need to clean up different spellings
	6. Intricate data gathering process (e.g through Web-scrapping)
		a. Using APIs to gather data from different sources
	7. Statistical analysis
		a. Evaluate temporal trends by decade
			i. Number of Movies
				1) "Good" Movies
				2) "Bad" movies
			ii. Ratings
				1) IMDB
				2) Rotten Tomatoes
				3) Metacritic
			iii. Gross BO income
			iv. Movie length
				1) Long movies
				2) Short movies
			v. Sequels?
			vi. Awards (Oscars in major categories)
			vii. Genre
			viii. Season of release
	8. Linear Regression and variants (e.g ridge regression, lasso regression)
		a. Ratings by decade, by year
		b. Subset analysis
			i. Genre
			ii. Awards
			iii. Box office
	9. Logistic Regression and variants (e.g perceptron)
		a. Dichotomize good vs. bad movies
	10. Graphical User Interface
Using APIs in your project -using APIs![image](https://github.com/user-attachments/assets/6215b806-61e2-43bf-bd18-14424a9d9c12)

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






