# CoreShield-JSON-Assignment
This document outlines the step-by-step approach to solve the assignment involving the processing and analysis of two JSON files. The goal is to merge the data, perform specific calculations, and extract insights. The technical stack used is Python, leveraging libraries such as JSON, PANDAS, and NUMPY.

Approach:-
This assignment typically involves 
•	Merging 2 JSON files(Locations.json & Metadata.json) based on a common id field.
•	Counting all the valid points per type (for example: cafes, restaurants & hotels).
•	Next we move on to calculating the average rating per type.
•	Once we are done with the Calculations we move on to identifying location with the highest number of reviews.
•	As a part of our bonus objective we also filter out the locations with the incomplete data.

Step By Step Approach for better understanding:-
1.	Create the Json files and then Load and Parse them Either in notepad or VScode 
We can do this either manually by entering json files in correct format with the help of notepad or vscode 
OR
We can directly create both the JSON files with the hel of python libraries which I have used to make the process more smooth and hassle free  directly in VS code 
 

Alternatively once created we can Load the JSON files into python and convert them into pandas DataFrames for easier manipulation .

Code:-
import json
import pandas as pd

# Load JSON files
with open('locations.json') as f:
    locations_data = json.load(f)

with open('metadata.json') as f:
    metadata_data = json.load(f)

# Convert to DataFrames
locations_df = pd.DataFrame(locations_data)
metadata_df = pd.DataFrame(metadata_data)


#	Once done with the validation and Loading of the Json files we move on to the merging stage based on ID:

Here we combine the two Dataframes Using id  column as the key .

Code:-
valid_points_per_type = merged_df['type'].value_counts()
print("Valid Points per Type:\n", valid_points_per_type)
 
# After merging both the JSON files we have our entire workbase ready with the data to work on based on the objectives thus we move on to the next phrase which is Counting Valid Points per Type
Here we Count the number of valid entries for each type (example: cafes,hotels and restaurants).
CODE:-
valid_points_per_type = merged_df['type'].value_counts()
print("Valid Points per Type:\n", valid_points_per_type)
 

# Next we need to maintain a record for Average Rating per Type 
Here we group the data by TYPE and calculate the average rating for each group 

CODE:-
average_rating_per_type = merged_df.groupby('type')['rating'].mean()
print("Average Rating per Type:\n", average_rating_per_type)

 
# Going onto the next step we need to identify the Location with the Highest Number of Reviews 

Here we find the location with the maximum value in the reviews column 

CODE:-
incomplete_data = merged_df[merged_df.isnull().any(axis=1)]
print("Locations with Incomplete Data:\n", incomplete_data)

 
# 	Finally as a part of the Bonus we move on the last step which is Identifying Locations with incomplete Data

Check for the Missing Values in the merged DataFrame.

CODE:
incomplete_data = merged_df[merged_df.isnull().any(axis=1)]
print("Locations with Incomplete Data:\n", incomplete_data)

 

 
