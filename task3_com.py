import pandas as pd
# Load the Excel file and select sheet named as 'dataset_3'
file_path = 'data/Bayesian_Risk_Data.xlsx'
data = pd.ExcelFile(file_path)
df = data.parse('dataset_3')

# Rank assets based on the 'Target Probability'
df_sorted = df.sort_values(by='Target Probability ', ascending=False).reset_index(drop=True)

# Provide insights into which assets are most vulnerable
most_vulnerable = df_sorted.head(3)
least_vulnerable = df_sorted.tail(3)

print("Most Vulnerable Assets:")
print(most_vulnerable[['Asset ', 'Target Probability ']])

print("\nLeast Vulnerable Assets:")
print(least_vulnerable[['Asset ', 'Target Probability ']])
