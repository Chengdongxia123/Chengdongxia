import pandas as pd

# Load the Seattle pet licenses data
file_path = './Chengdongxia/seattle_pet_licenses.csv'
seattle_pets_df = pd.read_csv(file_path)

# Task 1: Count the total number of pets
num_pets = seattle_pets_df.shape[0]
print(f"1. Total number of pets in the dataset: {num_pets}")

# Task 2: Count the number of variables for each pet
num_variables = seattle_pets_df.shape[1]
print(f"2. Number of variables (columns) per pet: {num_variables}")

# Task 3: Find the three most common pet names in Seattle
top_three_pet_names = seattle_pets_df['animal_s_name'].value_counts().nlargest(3)
print("3. Three most common pet names in Seattle:")
for name, count in top_three_pet_names.items():
    print(f"   - {name}: {count} occurrences")