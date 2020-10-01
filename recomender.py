import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
# from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# from nltk.stem import WordNetLemmatizer
# from nltk.tokenize import RegexpTokenizer
import re
import string
import random
from PIL import Image
import requests
from io import BytesIO


def recommend(title,data):
    # Matching the genre with the dataset and reset the index

    # Convert the index into series
    indices = pd.Series(data.index, index = data['title'])
    tf = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df = 1, stop_words='english')
    tfidf_matrix = tf.fit_transform(data['cleaned_desc'])
    sg = cosine_similarity(tfidf_matrix, tfidf_matrix)
    idx = indices[title]
    sig = list(enumerate(sg[idx]))
    sig = sorted(sig, key=lambda x: x[1], reverse=True)
    sig = sig[1:6]
    movie_indices = [i[0] for i in sig]
    rec = data[['title']].iloc[movie_indices]
    image=data[['image_link']].iloc[movie_indices]
    author=data[['author']].iloc[movie_indices]
    rating=data[['rating']].iloc[movie_indices]
    genre=data[['genre']].iloc[movie_indices]


    context={
        "title": list(rec['title']),
        "image":list(image['image_link']),
        "author":list(author['author']),
        "rating":list(rating['rating']),
        "genre":list(genre['genre']),

    }
    return context

# recommend(title,data)