import pandas as pd
from itertools import combinations
from collections import Counter

#  Step 1: Load the dataset 
df = pd.read_csv("Dataset .csv")   

#  Step 2: Clean and prepare cuisine data 
df['Cuisines'] = df['Cuisines'].astype(str).str.split(',')
df['Cuisines'] = df['Cuisines'].apply(lambda x: [c.strip() for c in x if c.strip() != ""])

#  Step 3: Generate combinations of cuisines (only for restaurants with 2+ cuisines) 
combo_list = []

for cuisines, rating in zip(df['Cuisines'], df['Aggregate rating']):
    if len(cuisines) > 1:
        for combo in combinations(sorted(cuisines), 2):
            combo_list.append((combo, rating))

#  Step 4: Count most common combinations 
combo_counter = Counter([c[0] for c in combo_list])
top_combos = combo_counter.most_common(5)  # top 5 combinations

#  Step 5: Calculate average rating for each top combination 
combo_ratings = {}
for combo, _ in top_combos:
    ratings = [r for (c, r) in combo_list if c == combo]
    combo_ratings[combo] = round(sum(ratings) / len(ratings), 2) if ratings else 0

#  Step 6: Create result DataFrame 
result = pd.DataFrame({
    'Cuisine Combination': [' & '.join(c) for c, _ in top_combos],
    'Count': [count for _, count in top_combos],
    'Average Rating': [combo_ratings[c] for c, _ in top_combos]
})

#  Step 7: Display results 
print("\n🍴 Most Common Cuisine Combinations and Their Ratings:")
print(result)

