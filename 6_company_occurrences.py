# Task (3):
# Step (2): Count the occurrences of each company

# Import necessary modules
import json 
from pathlib import Path
from collections import Counter

# Set paths for input and output files
input_file = Path.cwd()/"list_of_companies.json"
output_file = Path.cwd()/"company_occurrence_data.json"

# Open and read the input file
with input_file.open("r") as f:
    data= json.load(f)

# Count company occurrences
company_count = Counter(data.get("List of Companies"))

# Create nested dictionary
nested_dict= {"Company Occurrence Counts":dict(company_count)}

# Write nested dictionary to output file
with output_file.open("w") as y:
    json.dump(nested_dict, y, indent=2)
  
    
# Print completion message to user
print("<< Company occurrence counts have been obtained >>")