#!/usr/bin/env python
# coding: utf-8

# Importing the dependencies

# In[1]:


import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Data Collection and Pre-Processing

# In[3]:


movies_data = pd.read_csv('movies.csv')
selected_features = ['genres','keywords','tagline','cast','director']
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')


# In[13]:


combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)


# In[14]:


# converting the text data to feature vectors

vectorizer = TfidfVectorizer()


# In[15]:


feature_vectors = vectorizer.fit_transform(combined_features)


# Cosine Similarity

# Movie Recommendation Sytem

# In[19]:


def predictor(movie_name):
    movies=[]
    list_of_all_titles = movies_data['title'].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    close_match = find_close_match[0]

    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

    i = 1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index==index]['title'].values[0]
        if (i<30):
            movies.append(title_from_index)
        i+=1
    return movies


# In[ ]:




