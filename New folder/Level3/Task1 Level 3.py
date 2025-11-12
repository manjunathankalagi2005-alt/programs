import pandas as pd
import matplotlib.pyplot as plt

#  Step 1: Load the dataset 
df = pd.read_csv("Dataset .csv")   

#  Step 2: Check available review-related columns 
print("Available columns:", df.columns)

#  Step 3: Analyze Rating Text Distribution 
rating_text_counts = df['Rating text'].value_counts()

# Plot rating text distribution
plt.figure(figsize=(8,5))
plt.bar(rating_text_counts.index, rating_text_counts.values, color='lightgreen', edgecolor='black')
plt.title("Distribution of Rating Texts (Customer Review Sentiment)")
plt.xlabel("Rating Text Category")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#  Step 4: Identify most common positive & negative keywords 
# Based on the 'Rating text' column
positive_keywords = ['Excellent', 'Very Good']
negative_keywords = ['Average', 'Poor', 'Not rated']

positive_count = df[df['Rating text'].isin(positive_keywords)].shape[0]
negative_count = df[df['Rating text'].isin(negative_keywords)].shape[0]

print(f"👍 Positive Reviews: {positive_count}")
print(f"👎 Negative Reviews: {negative_count}")

#  Step 5: Calculate average 'Votes' for popularity 
avg_votes = df['Votes'].mean().round(2)
print(f"\n📊 Average number of votes per restaurant: {avg_votes}")

#  Step 6: Relationship between Rating and Votes 
plt.figure(figsize=(8,5))
plt.scatter(df['Aggregate rating'], df['Votes'], alpha=0.5, color='teal')
plt.title("Relationship Between Rating and Popularity (Votes)")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Votes")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

#  Step 7: Print Summary 
summary = pd.DataFrame({
    "Metric": ["Most Common Positive Keywords", "Most Common Negative Keywords", "Average Votes per Restaurant"],
    "Value": [", ".join(positive_keywords), ", ".join(negative_keywords), avg_votes]
})

print("\n📝 Restaurant Reviews Summary:")
print(summary)
