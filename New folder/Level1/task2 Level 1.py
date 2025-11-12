import pandas as pd

#  Step 1: Load the dataset 
# Replace with your file path
df = pd.read_csv("Dataset .csv")   

#  Step 2: Identify the city with the highest number of restaurants 
city_counts = df['City'].value_counts()
 # City with the most restaurants
top_city = city_counts.idxmax()        
# Number of restaurants in that city
top_city_count = city_counts.max()      

#  Step 3: Calculate average rating for restaurants in each city 
city_avg_rating = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

#  Step 4: Find the city with the highest average rating 
best_rated_city = city_avg_rating.idxmax()
best_rated_value = city_avg_rating.max()

#  Step 5: Create a summary DataFrame 
summary = pd.DataFrame({
    "City": [top_city, best_rated_city],
    "Metric": ["Most Restaurants", "Highest Average Rating"],
    "Value": [top_city_count, round(best_rated_value, 2)]
})

#  Step 6: Display results 
print("City Analysis Results:\n")
print(summary)

#  Step 7 (Optional): Also print detailed average ratings per city 
print("\nAverage Ratings by City:")
# Show top 10 for quick view
print(city_avg_rating.head(10))  
