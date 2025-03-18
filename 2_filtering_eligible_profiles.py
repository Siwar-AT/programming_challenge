# Task (2): 
# Step (1): Load and filter all provided JSON files to exclude profiles with fewer then 3 companies and no programming languages

# Import necessary modules
import shutil
import json
from pathlib import Path


# Set paths for source and destination directories
source_directory= Path.cwd() / "profiles" 
destination_directory= Path.cwd() / "eligible_profiles" 

# Create the destination directory if it doesn't exist
Path("eligible_profiles").mkdir(exist_ok=True) 

# Iterate over JSON files in the source directory
for file in source_directory.glob("*.json"): 
   with file.open("r") as x:
      data = json.load(x)
      
      # Check if the profile meets the filtering criteria and if it does copy it to destination directory
      if len(data["companies"]) >=3 and len(data["skills"])> 0: 
         shutil.copy(file, destination_directory)
         
# Print completion message to user
print("<< Profiles have been filtered >>")
