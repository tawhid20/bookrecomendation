# Group Project
## Group No: 90

##### Members:
Student Name:   Tawhidur Rahman Abir
Student ID:  46219285

Student Name: Ayyan Muzaffar
Student ID: 44330723

Student Name: Romil Rajendra Sawant 
Student ID: 46171282

Student Name: Ugur Menekse
Student ID: 46535837

## Project Description:

### Introduction: 
   Books are sometimes considered a person's best friend, to whom you can always return to get away from the harshness of reality. Every time we take a book into our hands and we close ourselves to a small world of dreams. Reading makes us forget our sorrows while we read those of others. George R.R. Martin-One of the most influential writers in recent time, best know for his epic fantasy novel "A Song of Ice and Fire"  once said “A reader lives a thousand lives before he dies . . . The man who never reads lives only one.”
   
   In this project, we will dive deep into the world of books, 
   * We will collect data on books from several different sources
   * Analyse and find out several interesting insights from them
   * Solve two very real-world problems 
   
### Structure
The project is mainly divided into three parts.

##### Data Collection(  project_files/Data accumulation and formatting.ipnb  ):
The Datasets we used are 
* GoodReads data       (link : https://www.kaggle.com/jealousleopard/goodreadsbooks)
* UCSD data       (link : https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home?authuser=0)
    reference:
    * Mengting Wan, Julian McAuley, "Item Recommendation on Monotonic Behavior Chains", in RecSys'18.  [bibtex]
    * Mengting Wan, Rishabh Misra, Ndapa Nakashole, Julian McAuley, "Fine-Grained Spoiler Detection from Large-Scale Review Corpora", in ACL'19. [bibtex]
We have also created Scraper to scrape data directly from https://www.goodreads.com/.

In this part, we collect data from different sources and also clean them to a format which can be further used for Analysis of the data.

##### Data Analysis(  project_files/Data analysis.ipnb  ):
In this part, we use the formatted data we got from the data collection part and do extensive data analysis.
We find several interesting insights, like are people shifting to a new genre? Or is there a change in the author's book rating over the years? Or is there a correlation between the authors and publishers, etc.

##### Problem statement(  project_files/Recommender system.ipnb  ):
In this part of the project, we will tackle two real-world issues,

* We will build a Recommender System: Suppose you read a very exciting book that falls in love with now, and now you want to find books similar to that, this project implements several approached to build a recommender system to find similar books.

* There is time a book is so good, that it is adapted into a movie. Great books like the Harry Potter series, Lord of the rings all have movie adaptations. We build and analyzed several different models that predict if a book will receive a movie adaptation or not.


### Web Application:
 We also made our recommender system into a web application using flask that is currently deployed in Heroku, and ready to use. 
 The dataset we used on the application contains fewer entries compared to that in the project as it's just a prototype, but can be turned into a full-fledged application in the future.
 
##### Application Link : https://bookapp-tawhid.herokuapp.com/auto

##### Application Code : https://github.com/tawhid20/bookrecomendation.git

### Conclusion:
So, while working on the project we have learned various things like joining the datasets, selecting a particular amount of data from the datasets.While working on the project  issues were encountered but they were resolved by the team effort. Improvements include planning ahead, starting early and investing more time into project.Knowledge gained include technical skills such as Python and softs skills which includes communication, teamwork, problem solving and leadership.Overall the project was challenging but the knowledge gained from this project both technical and soft skills can be used as future engineers in the work industry.
 











