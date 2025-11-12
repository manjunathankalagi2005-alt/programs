import pandas as pd
import matplotlib.pyplot as plt

#  Step 1: Load the dataset 
df = pd.read_csv("Dataset .csv")   

#  Step 2: Analyze the distribution of aggregate ratings 
rating_counts = df['Aggregate rating'].value_counts().sort_index()

#  Step 3: Plot histogram for rating distribution 
plt.figure(figsize=(8, 5))
plt.bar(rating_counts.index, rating_counts.values, color='skyblue', edgecolor='black')
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#  Step 4: Determine the most common rating value 
most_common_rating = rating_counts.idxmax()
most_common_count = rating_counts.max()

#  Step 5: Calculate the average number of votes per restaurant 
avg_votes = df['Votes'].mean().round(2)

#  Step 6: Display summary results 
summary = pd.DataFrame({
    'Metric': ['Most Common Rating', 'Restaurants with that Rating', 'Average Votes per Restaurant'],
    'Value': [most_common_rating, most_common_count, avg_votes]
})

print("\n⭐ Restaurant Ratings Analysis:")
print(summary)
