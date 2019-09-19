from collections import defaultdict, namedtuple, Counter, deque
from urllib.request import urlretrieve
import csv
import random

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)
