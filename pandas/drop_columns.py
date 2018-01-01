import pandas as pd

data = pd.read_csv('5000_movies.csv')

original_columns = data.columns
print(original_columns)

columns_to_be_dropped = ['budget', 'genres', 'homepage']
columns_to_be_dropped = [c for c in columns_to_be_dropped if c in list(data.columns)]

data = data.drop(columns_to_be_dropped, axis=1)

print('\n')
print(data.columns)