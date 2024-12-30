import pandas as pd

url ='https://raw.githubusercontent.com/tidyverse/datascience-box/refs/heads/main/course-materials/lab-instructions/lab-03/data/nobel.csv'
df = pd.read_csv(url)
df.head()

df.to_csv('Chengdongxia/nobel.csv')


import pandas as pd
# Load the data from the CSV file
file_path = "Chengdongxia/nobel.csv"  # Assuming the file is saved here
nobel_df = pd.read_csv(file_path)

# Task 1: Get the number of observations and variables
num_observations, num_variables = nobel_df.shape
print(f'num_observations: {num_observations}, num_variables: {num_variables}')
print("Each row represents an individual who has received a Nobel Prize. \n",
        "The row includes details such as their name, year of award, category, affiliation, country, \n",
        "birth and death dates, and motivation for the award.")

        nobel_living = nobel_df[(nobel_df['country'].notna()) &
                        (nobel_df['gender'] != 'org') &
                        (nobel_df['died_date'].isna())]
print(f'nobel_living shape: {nobel_living.shape}')
nobel_living.head()

# Task 3: Find the most common country for Nobel laureates' affiliations when they won their prizes
most_common_country = nobel_df['country'].mode().iloc[0] if not nobel_df['country'].empty else None
print(f'most_common_country: {most_common_country}')

from skimpy import skim

titanic_df = pd.read_csv("Chengdongxia/titanic.csv")

# Display summary with skimpy
skim(titanic_df)

# Display the first few rows to understand the structure
titanic_df.head()

# Get a concise summary of the DataFrame
titanic_df.info()

# Check for any missing values in each column
titanic_df.isnull().sum()

# Summary statistics for numerical columns
titanic_df.describe()

# Summary statistics for categorical columns
titanic_df.describe(include="object")

# Count unique values in each categorical column
titanic_df['Sex'].value_counts()
titanic_df['Embarked'].value_counts()

# Survival rate by class
titanic_df.groupby('Pclass')['Survived'].mean()

# Survival rate by sex
titanic_df.groupby('Sex')['Survived'].mean()

# Percentage of missing values in each column
missing_percentage = (titanic_df.isnull().mean() * 100).sort_values(ascending=False)
missing_percentage