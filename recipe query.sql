SELECT * FROM recipes;

SELECT ROUND(AVG(fat + saturates),2) AS avg_fat, 
	   ROUND(AVG(salt + sugars),2) AS avg_flavor, 
	   ROUND(AVG(protein),2) AS avg_protein
FROM recipes;

SELECT title, 
	   ROUND(fat+saturates,2) AS fat, 
	   ROUND(protein,2) AS protein
FROM recipes
WHERE title NOT LIKE '%Coconut%'
ORDER BY fat DESC, protein ASC
LIMIT 10;

WITH cte AS (
    SELECT COUNT(*) AS total_recipes,
           COUNT(CASE WHEN protein >= 50 THEN 1 END) AS high_protein_recipes
    FROM recipes
)
SELECT ROUND(high_protein_recipes * 100.0 / total_recipes, 2) AS percentage
FROM cte;

SELECT title, 
	   ROUND(fat+saturates,2) AS fat, 
	   ROUND(protein,2) AS protein
FROM recipes
WHERE (title LIKE '%Healthy%')
  AND (title LIKE '%Protein%')
ORDER BY fat DESC;

SELECT website, AVG(fat + sugars) AS mean_fat_sugars
FROM recipes
GROUP BY website
ORDER BY mean_fat_sugars DESC
LIMIT 5;