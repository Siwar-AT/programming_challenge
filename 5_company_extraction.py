# Task (3):
# Step (1): Extract the list of companies from each profile

# Import necessary modules
import json 
from pathlib import Path

# Set paths for source directory and output file
source_directory= Path.cwd()/"eligible_profiles"
output_file = Path.cwd()/"list_of_companies.json"


# Create a list to store the companies
all_companies= []

# Iterate over JSON files in the source directory
for file in source_directory.glob("*.json"): 
    with file.open("r") as f:
        data= json.load(f)
        
        # Extract companies from each profile and add them to the list
        companies = data.get("companies")  
        all_companies.extend(companies)
        
# Create a dictionary to store the extracted companies
list_of_companies= {"List of Companies": all_companies}
        
# Write dictionary to output file
with output_file.open("w") as x:
    json.dump(list_of_companies, x, indent=2)

# Print completion message to user
print("<< Companies have been extracted >>")