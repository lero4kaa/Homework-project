""""
This module was made to show that movies.csv and ratings.csv files
have the information I need for the project. The result of the
execution is file with first 100 000 rows of the data frame,
where movie`s title, rating, genre, and user`s id are merged together.
"""
import pandas as pd


pd.set_option('display.max_columns', 10)

data_ratings = pd.read_csv('ratings.csv')

data_movies = pd.read_csv('movies.csv')

data_merged = pd.merge(data_ratings, data_movies, on='movieId')
data_merged.head(100000).to_csv('result.csv')
