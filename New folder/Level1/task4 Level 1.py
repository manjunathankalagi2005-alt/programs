import pandas as pd

#  Step 1: Load the dataset 
df = pd.read_csv("Dataset .csv")  

#  Step 2: Clean and normalize the 'Has Online delivery' column 
df['Has Online delivery'] = df['Has Online delivery'].astype(str).str.strip().str.title()

#  Step 3: Calculate percentage of restaurants that offer online delivery 
online_delivery_counts = df['Has Online delivery'].value_counts()
online_delivery_percentage = (online_delivery_counts / len(df)) * 100

#  Step 4: Compare average ratings for restaurants with/without online delivery 
avg_ratings = df.groupby('Has Online delivery')['Aggregate rating'].mean()

#  Step 5: Create summary DataFrames 
percentage_df = pd.DataFrame({
    'Online Delivery Option': online_delivery_counts.index,
    'Restaurant Count': online_delivery_counts.values,
    'Percentage (%)': online_delivery_percentage.round(2)
})

ratings_comparison = avg_ratings.reset_index().rename(columns={'Aggregate rating': 'Average Rating'})

#  Step 6: Display results 
print("\n📊 Online Delivery Distribution:")
print(percentage_df)

print("\n⭐ Average Ratings Comparison:")
print(ratings_comparison)
