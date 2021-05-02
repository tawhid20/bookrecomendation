# **Data Science Project Proposal**

**Group – 90**

**Members:** Ugur Menekse(ID: 46535837) **,** Tawhidur Rahman Abir(ID:46219285) **,** Ayyan Muzaffar(ID: 44330723
) **,** Romil Rajendra Sawant(ID: 46171282)

## _Book Recommender System_

![](library.jpg)


Nowadays, the amount of information on the internet is growing at a fast pace, so finding appropriate information has become of utmost importance. New technologies are emerging to tackle this problem and one such tool is the recommendation system. It helps to navigate quickly and receive the necessary information. This project will implement a quick and intuitive book recommendation system that assists readers in finding an appropriate book to read using content-based filtering. 

### Our Aim

The project will be arranged into several parts:

1.	Collecting Data: Even though there are plenty of useful book datasets, these rarely have automatic updating feature, thereby are often outdated. On top of that, they are missing some fundamental information like book descriptions, awards, prices, and some key insight such as whether the book has been produced into a movie. These features are essential for our goal of building a recommendation system for books. So, for that job, we will have to build web scrapers.

2. Analyzing and pre-processing data: We will analyze different trends in books. For instance, are people shifting to a new genre? Or is there a change in the author's book rating? Or is there a correlation between the authors and publishers, etc. The data needs to be processed; we plan to change the book description to features for the recommendation engine. 

1. Prediction: We will make 2 applications.

* Prediction whether a book will be made into a movie or not.

* A book recommendation system that will be taken in the input of a book title and will find similar books based on the description, author, and genre.

### Our Data

Initially, we will start by using [Good-Reads](https://www.kaggle.com/jealousleopard/goodreadsbooks). The dataset from Kaggle which comes as a CSV format with approximately 10,000 books and info.

[Title, authors, average rating, ISBN, isbn13, language, number of pages, rating count, text reviews count, publication date, and publisher].

As our base Dataset, we will add more features by scraping data from different sources like Good-Reads [website](https://www.goodreads.com/) or Amazon and also adding new data to the dataset.

### Analysis Techniques

Classification: Logistic regression for the prediction of movies or not. Then use Random Forrest Classifier and Naive Bayes.

Recommendation System: We will first use TF-IDF to find cosine similarities. Then use Word2vec.

### Milestones

Milestone 1 (Gathering and Preprocessing)

- Build a Scraper.
- Join the data to the existing data.
- Analyze the data to show different trends and relationships.

Milestone 2 (Building the Applications)

- Process our data by lemmatization then try to build the recommendation system with different algorithms and try to improve performance by adding more features.
- For the classification App, we will train in the models of google collab.
- For the recommendation app we will use Google's pre-trained word2vec model, as it becomes computationally expensive to train a model.

### Previous Relevant work:

There have been previous works on a book recommendation system that uses collaborative filtering from user ratings to make a recommendation system and some that use content-based filtering that only uses the features provided in the dataset.


### reference: 
* Kurmashov, Nursultan & Latuta, Konstantin & Nussipbekov, Abay. (2015). Online book recommendation system. 1-4. 10.1109/ICECCO.2015.7416895.

