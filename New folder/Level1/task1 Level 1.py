import pandas as pd

#  Step 1: Load the dataset 
df = pd.read_csv("Dataset .csv")  

#  Step 2: Split cuisines if multiple cuisines are listed in one cell 
df['Cuisines'] = df['Cuisines'].astype(str).str.split(',')

#  Step 3: Explode the 'Cuisines' column so each cuisine is a separate row 
df_exploded = df.explode('Cuisines')

#  Step 4: Clean up whitespace 
df_exploded['Cuisines'] = df_exploded['Cuisines'].str.strip()

#  Step 5: Count occurrences of each cuisine 
cuisine_counts = df_exploded['Cuisines'].value_counts()

#  Step 6: Get the top 3 most common cuisines 
top3_cuisines = cuisine_counts.head(3)

#  Step 7: Calculate percentage of restaurants serving each cuisine 
total_restaurants = len(df)
percentages = (top3_cuisines / total_restaurants) * 100

#  Step 8: Create a result DataFrame 
result = pd.DataFrame({
    'Cuisine': top3_cuisines.index,
    'Count': top3_cuisines.values,
    'Percentage (%)': percentages.values.round(2)
})

#  Step 9: Display the result 
print("\nTop 3 Most Common Cuisines:")
print(result)
