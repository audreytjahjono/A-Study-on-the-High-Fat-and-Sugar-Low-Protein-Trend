import pandas as pd
import ast
from urllib.parse import urlsplit

# read the CSV file
df = pd.read_csv('new_recipe_file.csv')

# convert string representations of dictionaries to actual dictionaries
df['nutr_values_per100g'] = df['nutr_values_per100g'].apply(lambda x: ast.literal_eval(x))

# fixing nutr_values_per100g column
# extract nutrient values from the 'nutr_values_per100g' column
df['energy'] = df['nutr_values_per100g'].apply(lambda x: x['energy'])
df['fat'] = df['nutr_values_per100g'].apply(lambda x: x['fat'])
df['protein'] = df['nutr_values_per100g'].apply(lambda x: x['protein'])
df['salt'] = df['nutr_values_per100g'].apply(lambda x: x['salt'])
df['saturates'] = df['nutr_values_per100g'].apply(lambda x: x['saturates'])
df['sugars'] = df['nutr_values_per100g'].apply(lambda x: x['sugars'])

# drop the original 'nutr_values_per100g' column
df.drop('nutr_values_per100g', axis=1, inplace=True)

# drop unnecessary column for analysis
df.drop('fsa_lights_per100g', axis=1, inplace=True)
df.drop('nutr_per_ingredient', axis=1, inplace=True)
df.drop('partition', axis=1, inplace=True)
df.drop('quantity', axis=1, inplace=True)
df.drop('unit', axis=1, inplace=True)
df.drop('weight_per_ingr', axis=1, inplace=True)

# instead of having different name of ingredients, I just want the number of ingredients in each recipe
df['ingredients'] = df['ingredients'].apply(lambda x: ast.literal_eval(x))

# count the number of 'text' keys in each ingredients dictionary
df['tot_ingredients'] = df['ingredients'].apply(lambda x: len(x))
df.drop('ingredients', axis=1, inplace=True)

# instead of having list of instructions, I just want the number of instructions in each recipe
df['instructions'] = df['instructions'].apply(lambda x: ast.literal_eval(x))

# count the number of 'text' keys in each instructions dictionary
df['tot_instructions'] = df['instructions'].apply(lambda x: len(x))
df.drop('instructions', axis=1, inplace=True)

# extracting the name of the website from the URLs 
df['website'] = df['url'].apply(lambda x: urlsplit(x).netloc)
df.drop('url', axis=1, inplace=True)

# removing the 'www.' and '.com' from the 'website' column
df['website'] = df['website'].str.replace('www\.', '').str.replace('\.com', '') 

# write the modified dataframe back to a CSV file
df.to_csv('final_recipe.csv', index=False)