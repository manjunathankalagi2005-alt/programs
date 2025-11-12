import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Step 1: Load the dataset 
df = pd.read_csv("Dataset .csv") 

#  Step 2: Clean and standardize relevant columns 
df['Has Online delivery'] = df['Has Online delivery'].astype(str).str.strip().str.title()
df['Has Table booking'] = df['Has Table booking'].astype(str).str.strip().str.title()

#  Step 3: Calculate percentage of restaurants offering online delivery per price range 
delivery_by_price = (
    df.groupby('Price range')['Has Online delivery']
    .value_counts(normalize=True)
    .unstack()
    .fillna(0) * 100
)

#  Step 4: Calculate percentage of restaurants offering table booking per price range 
booking_by_price = (
    df.groupby('Price range')['Has Table booking']
    .value_counts(normalize=True)
    .unstack()
    .fillna(0) * 100
)

#  Step 5: Plot - Online Delivery availability by Price Range 
plt.figure(figsize=(10, 5))
sns.barplot(x=delivery_by_price.index, y=delivery_by_price['Yes'], color='skyblue', edgecolor='black')
plt.title("Percentage of Restaurants Offering Online Delivery by Price Range", fontsize=13)
plt.xlabel("Price Range (1 = Low, 4 = High)")
plt.ylabel("Percentage Offering Online Delivery")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#  Step 6: Plot - Table Booking availability by Price Range 
plt.figure(figsize=(10, 5))
sns.barplot(x=booking_by_price.index, y=booking_by_price['Yes'], color='lightgreen', edgecolor='black')
plt.title("Percentage of Restaurants Offering Table Booking by Price Range", fontsize=13)
plt.xlabel("Price Range (1 = Low, 4 = High)")
plt.ylabel("Percentage Offering Table Booking")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#  Step 7: Create a summary DataFrame 
summary = pd.DataFrame({
    'Price Range': delivery_by_price.index,
    'Online Delivery (%)': delivery_by_price['Yes'].round(2),
    'Table Booking (%)': booking_by_price['Yes'].round(2)
})

#  Step 8: Display results 
print("\n💰 Price Range vs Online Delivery and Table Booking:")
print(summary)
