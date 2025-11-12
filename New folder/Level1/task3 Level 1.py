import pandas as pd
import matplotlib.pyplot as plt

#  Step 1: Load the dataset 

df = pd.read_csv("Dataset .csv")   

#  Step 2: Count the number of restaurants in each price range 
price_counts = df['Price range'].value_counts().sort_index()

#  Step 3: Calculate the percentage of restaurants per price range 
price_percentages = (price_counts / len(df)) * 100

#  Step 4: Combine into a DataFrame 
price_distribution = pd.DataFrame({
    'Price Range': price_counts.index,
    'Restaurant Count': price_counts.values,
    'Percentage (%)': price_percentages.round(2)
})

#  Step 5: Display table 
print("\nPrice Range Distribution:")
print(price_distribution)

#  Step 6: Create a bar chart (Histogram visualization) 
plt.figure(figsize=(8, 5))
plt.bar(price_distribution['Price Range'], price_distribution['Restaurant Count'], color='skyblue', edgecolor='black')
plt.title("Distribution of Restaurants by Price Range")
plt.xlabel("Price Range (1 = Low, 4 = High)")
plt.ylabel("Number of Restaurants")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
