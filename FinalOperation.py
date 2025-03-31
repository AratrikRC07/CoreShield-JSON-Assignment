import json
import pandas as pd
with open('locations.json') as f:
    locations_data = json.load(f)
with open('metadata.json') as f:
    metadata_data = json.load(f)
locations_df = pd.DataFrame(locations_data)
metadata_df = pd.DataFrame(metadata_data)
merged_df = pd.merge(locations_df, metadata_df, on='id', how='inner')

valid_points_per_type = merged_df['type'].value_counts().reset_index()
valid_points_per_type.columns = ['Type', 'Count']

average_rating_per_type = merged_df.groupby('type')['rating'].mean().reset_index()
average_rating_per_type.columns = ['Type', 'Average Rating']

location_with_max_reviews = merged_df.loc[merged_df['reviews'].idxmax()]
incomplete_data = merged_df[merged_df.isnull().any(axis=1)]


print("\n=== Valid Points per Type ===")
print(valid_points_per_type.to_string(index=False))

print("\n=== Average Rating per Type ===")
print(average_rating_per_type.to_string(index=False))

print("\n=== Location with Highest Reviews ===")
print(pd.DataFrame(location_with_max_reviews).T.to_string(index=False))

print("\n=== Locations with Incomplete Data ===")
if incomplete_data.empty:
    print("No incomplete data found.")
else:
    print(incomplete_data.to_string(index=False))
