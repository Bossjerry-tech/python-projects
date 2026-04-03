import pandas as pd
#Loading the dataset...use movies
df_movies = pd.read_excel(r"C:\Users\USER\Downloads\movies.xlsx")

#df_movies.head(10)

#using ".info"

#df_movies.info()
#df_movies.shape#for entries and no. of columns
#df_movies.describe()  

#df_movies[df_movies['imdb_rating']>10]
# Using distinct entries in column industry 
#df_movies['industry'] .unique() #functions as typeof
df_movies['industry'].value_counts()


#df_movies['studio'].value_counts()
#How to visualize the value counts
from matplotlib import pyplot as plt
df_movies['industry'].value_counts().plot(kind='pie')
#df_movies.duplicated().sum

#How to see duplicates
df_movies[df_movies.duplicated()]
df_movies[df_movies['movie_id'].isin([112,123])]
