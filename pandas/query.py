import pandas as pd

# This is good for dynamic query building

data = pd.read_csv('5000_movies.csv')

filtered_data = data.query("runtime >= 150 and (original_language == 'ja' or original_language == 'fr')")

print(filtered_data)