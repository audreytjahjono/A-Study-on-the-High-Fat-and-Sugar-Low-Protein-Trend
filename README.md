# A-Study-on-the-High-Fat-and-Sugar-Low-Protein-Trend
Analyzed Nutritional Imbalance in Recipes Found on the Internet

## Problem Statement
This project aims to evaluate the nutritional value of recipes to address the growing prevalence of obesity and diet-related diseases. The analysis will focus on the distribution of fats, sugars, and proteins in the recipes and will investigate if the publicly available recipes are high in fats and sugars but low in protein. By examining recipe data from various sources, this project will identify trends in the nutritional content of recipes. The findings will provide insights into the nutritional quality of recipes and will help individuals make informed decisions about their diet choices, ultimately contributing to the prevention of diet-related diseases.

## Dataset
This project utilized data from Recipe1M+ to analyze a large dataset of recipe data, including ingredient lists and nutritional information. The dataset contains over 51,000 rows in a JSON file format. The Pandas library in Python was used to efficiently clean and reformat the data, enabling the extraction of key insights and patterns in the recipe data.

The data cleaning process involved several steps to extract and manipulate the relevant data for analysis. These steps included:
- Converting string representations of dictionaries to actual dictionaries
- Extracting nutrient values and dropping unnecessary columns
- Counting the number of ingredients and instructions in each recipe
- Extracting website names from URLs
- Writing the modified data frame to a CSV file
After cleaning and reformatting the dataset using Python and the Pandas library, the data is now ready for analysis in SQL. This will allow for more efficient querying and processing of the data to extract key insights and patterns related to the nutritional content of recipes.

## Analysis
### What is the average fat (fat and saturates), flavor (salt and sugar), and protein content across all recipes in the dataset?
Understanding the average fat, flavor, and protein content of recipes in a dataset is important because it gives us an idea of the nutritional value of the recipes. It can also help identify possible health issues linked to the recipes, such as high levels of fat or salt, which could be problematic for people with certain health conditions. This makes it easier to identify healthier or more suitable recipes for specific dietary needs. It is evident that the average fat content across all recipes is 22.2, while the average protein content is 5.22. The average flavor content, which includes salt and sugar, is 18.96. These findings suggest that the recipes available in the public domain are high in fat, but relatively low in protein. This is a cause for concern, as diets high in fat and sugar have been linked to the increasing prevalence of obesity and diet-related diseases.

### What are the top 10 recipes with the highest fat and lowest protein content commonly found in online recipes?
These recipes all have a similar energy value of around 191 kcal per 100g and zero grams of protein, suggesting they are high in fat and likely to contribute to a higher calorie intake. The analysis identified that most recipes mention the ingredient "coconut." Therefore, further exploration is needed to understand better the fat percentage in recipes that do not contain coconut. 
This analysis examines the fat content of various recipes, with values ranging from 174.86 to 191.3 per 100g. The "Oreo biscuits - no baked healthy choice!" and "Easy coconut cream concentrate makes 121g" recipes have the highest fat content, while the "Whole-Wheat Pie Crust" and "My Anzac Biscuits" recipes have the lowest. The study also notes that some recipes with high fat content have no protein. It is interesting to observe that the "Oreo biscuits - no baked healthy choice!" recipe, despite its name, contains high fat and zero protein. Similarly, the "Orange Creamsicle Protein Balls" recipe has high fat content but very little protein. This shows a wide range of fat content in publicly available recipes, and some recipes labeled as "healthy" may contain high levels of fat and little to no protein.

### Is there a correlation between the word “healthy” and “protein” in a recipe and its fat content?
Based on the analysis of the selected recipes, there seems to be a correlation between the use of the words "healthy" and "protein" in a recipe and its fat content. Of the five recipes analyzed, the ones with the highest fat content also had the lowest protein content. The highest protein content was found in the recipe with the lowest fat content. However, it is important to note that this is a small sample size and may not be representative of all recipes containing the word "healthy" and "protein". Further analysis with a larger dataset is necessary to draw a more definitive conclusion.

### What percentage of the recipes contain enough protein based on the recommended daily intake?
To answer this question, we need to determine the recommended daily protein intake and compare it to the amount of protein in each recipe. The recommended daily intake of protein varies depending on factors such as age, sex, weight, and physical activity level. However, in general, the recommended daily intake of protein for adults is around 0.8 grams per kilogram of body weight or about 56 grams per day for a sedentary man and 46 grams per day for a sedentary woman. For this analysis, let's assume that the recommended daily protein intake is 50 grams.
The analysis of the recipes showed that only 4% contain enough protein based on the recommended daily intake of 50 grams. This indicates a potential gap in the nutritional value of publicly available recipes and highlights the importance of considering protein intake in meal planning.

### Among commonly found recipes on the internet, what are the top 5 websites has the highest mean amount of fats and sugars in their recipes?
According to the SQL query, Land O'Lakes, Food Republic, Online Cookbook, Chowhound, and Food are the top five websites with the highest mean amount of fats and sugars in their recipes. This suggests that these websites' recipes may contribute to the prevalence of diet-related diseases due to their high fat and sugar content. Individuals looking to maintain a healthy diet should be cautious when using recipes from these websites. They may seek alternative sources with lower fats and sugars in their recipes. We can visualize this exploratory data in Tableau.
