import pandas as pd
import matplotlib.pyplot as plt

#  Step 1: Load the dataset 
df = pd.read_csv("Dataset .csv")  

#  Step 2: Extract latitude and longitude columns 
latitudes = df['Latitude']
longitudes = df['Longitude']

#  Step 3: Plot locations on a scatter map 
plt.figure(figsize=(10, 8))
plt.scatter(longitudes, latitudes, alpha=0.5, s=10, color='teal', edgecolors='black')
plt.title("Geographic Distribution of Restaurants", fontsize=14)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#  Step 4: Identify basic geographic boundaries 
geo_summary = pd.DataFrame({
    "Metric": ["Minimum Latitude", "Maximum Latitude", "Minimum Longitude", "Maximum Longitude"],
    "Value": [latitudes.min(), latitudes.max(), longitudes.min(), longitudes.max()]
})

#  Step 5: Display summary 
print("\n🌍 Geographic Analysis Summary:")
print(geo_summary)

# Optional: Check for clusters visually
# If points are very dense in certain longitude/latitude areas,
# that indicates clusters (e.g., multiple restaurants in specific cities or zones).
