import pandas as pd

# Load the dataset
df = pd.read_csv('british_airways_reviews.csv')

# Remove duplicates (if any)
df.drop_duplicates(subset="Review", inplace=True)

# Check for missing data
df.dropna(inplace=True)

# Display the cleaned data
print(df.head())

# Save the cleaned data
df.to_csv('cleaned_british_airways_reviews.csv', index=False)

print(f"Cleaned data saved. Total reviews: {len(df)}")
