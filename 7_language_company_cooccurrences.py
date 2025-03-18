# Task (4):
# Count the co-occurrences of each language with each company 

# Import necessary modules
import json 
from pathlib import Path
from collections import defaultdict

# Set path for source directory and output file
source_directory= Path.cwd()/"eligible_profiles"
output_file = Path.cwd()/"cooccurrence_data.json"

# Create a dictionary to store co-occurrence counts
co_occurrence_count = defaultdict(lambda:defaultdict(int))

# Iterate over JSON files in the source directory
for file in source_directory.glob("*.json"):
    with file.open("r") as f:
        data= json.load(f)
        
        # Extract languages amd companies from each profile
        languages = data.get("skills")
        companies = data.get("companies")
        
        #Iterate over each language and company pair 
        for language in languages:
            for company in companies:
                co_occurrence_count[language][company] += 1


# Create nested dictionary
nested_dict= {"Co-occurrence Counts of Languages with Companies": dict(co_occurrence_count)}

# Write nested dictionary to output file
with output_file.open("w") as x: 
    json.dump(nested_dict, x, indent=2 )

# Print completion message to user
print("<< Language and Company co-occurrence counts have been obtained >>")

# This print statement is for aesthetic purposes :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 

