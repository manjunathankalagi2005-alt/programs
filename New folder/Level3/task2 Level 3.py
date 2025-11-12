import pandas as pd
import matplotlib.pyplot as plt

#  Step 1: Load the dataset 
df = pd.read_csv("Dataset .csv")   

#  Step 2: Identify restaurants with highest and lowest number of votes 
highest_votes = df.loc[df['Votes'].idxmax(), ['Restaurant Name', 'Votes', 'Aggregate rating']]
lowest_votes = df.loc[df['Votes'].idxmin(), ['Restaurant Name', 'Votes', 'Aggregate rating']]

print("🏆 Highest Voted Restaurant:")
print(highest_votes)
print("\n🔻 Lowest Voted Restaurant:")
print(lowest_votes)

#  Step 3: Analyze correlation between votes and rating 
correlation = df['Votes'].corr(df['Aggregate rating'])
print(f"\n📊 Correlation between Votes and Rating: {round(correlation, 3)}")

#  Step 4: Plot relationship between Votes and Ratings 
plt.figure(figsize=(8, 5))
plt.scatter(df['Aggregate rating'], df['Votes'], alpha=0.5, color='purple', edgecolor='black')
plt.title("Relationship Between Restaurant Votes and Ratings", fontsize=13)
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Votes")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#  Step 5: Summary DataFrame 
summary = pd.DataFrame({
    "Metric": ["Highest Voted Restaurant", "Lowest Voted Restaurant", "Correlation (Votes vs Rating)"],
    "Value": [highest_votes['Restaurant Name'], lowest_votes['Restaurant Name'], round(correlation, 3)]
})

print("\n📝 Votes Analysis Summary:")
print(summary)
