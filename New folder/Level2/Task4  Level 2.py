import pandas as pd

#  Step 1: Load the dataset 
df = pd.read_csv("Dataset .csv")   

#  Step 2: Identify restaurant chains (same name appearing multiple times) 
chain_counts = df['Restaurant Name'].value_counts()
# Only names appearing more than once
restaurant_chains = chain_counts[chain_counts > 1]   

#  Step 3: Filter dataset to include only restaurant chains 
chain_df = df[df['Restaurant Name'].isin(restaurant_chains.index)]

#  Step 4: Analyze average rating and popularity for each chain 
chain_analysis = (
    chain_df.groupby('Restaurant Name')
    .agg({
        # Average rating of the chain
        'Aggregate rating': 'mean',  
         # Total votes = popularity 
        'Votes': 'sum',
        # Number of branches              
        'Restaurant ID': 'count'      
    })
    .rename(columns={
        'Aggregate rating': 'Average Rating',
        'Votes': 'Total Votes',
        'Restaurant ID': 'Number of Branches'
    })
    .sort_values(by='Number of Branches', ascending=False)
    # Show top 10 chains
    .head(10)  
)

#  Step 5: Display results 
print("\n🏪 Top Restaurant Chains Analysis:")
print(chain_analysis.reset_index())
