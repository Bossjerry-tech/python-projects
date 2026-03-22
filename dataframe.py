#Exercise 1

import pandas as pd

# Create the df
data = {
    'Student': ['Jerry', 'Steru', 'Mesh', 'Arnold'],
    'Grade': [88, 92, 79, 85],
    'Subject': ['Math', 'English', 'Science', 'History']
}
df_students = pd.DataFrame(data)
df_students.set_index('Student', inplace=True)
print(df_students)

#Exercise 2
#df using dict
data_cities = {
    'City': ['Nairobi', 'Mombasa', 'Kisumu'],
    'Population': [4397000, 1510000, 489000],
    'Country': ['Kenya', 'Kenya', 'Kenya']
}
df_cities = pd.DataFrame(data_cities)

print(df_cities.head(2))
df_cities.info()

#using a list
data_list = [
    ['Apple', 120, 0.5],
    ['Banana', 80, 0.2],
    ['Cherry', 200, 1.5]
]

df_fruit = pd.DataFrame(data_list, columns=['Fruit', 'Quantity', 'Price'])

print(f"Shape: {df_fruit.shape}")
print(df_fruit.dtypes)

#inspect df
print(df_fruit.head(3))
print(df_fruit.tail(2))
print(df_fruit.dtypes)


#Exercise 3
#select and filter datA

#Column selecting
fruit_col = df_fruit['Fruit']
subset_cols = df_fruit[['Fruit', 'Price']]

#Row selecting
second_row = df_fruit.iloc[1]
df_fruit_indexed = df_fruit.set_index('Fruit')
cherry_row = df_fruit_indexed.loc['Cherry']
selection = df_fruit.iloc[0:2, 0:2]


#Filtering Booleans

high_qty = df_fruit[df_fruit['Quantity'] > 100]
filter_and = df_fruit[(df_fruit['Price'] > 0.5) & (df_fruit['Quantity'] < 150)]
filter_or = df_fruit[(df_fruit['Price'] < 1) | (df_fruit['Quantity'] > 150)]

#Copy and views

fruit_subset = df_fruit[['Fruit', 'Price']].copy()
fruit_subset['Price'] = fruit_subset['Price'] * 1.1
print("Subset with 10% increase:\n", fruit_subset)
print("\nOriginal DataFrame (Unchanged):\n", df_fruit)
