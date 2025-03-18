# Task (2): 
# Step (2): Load and filter all provided JSON files to only include profiles with fewer than 3 companies or no programming languages

# Import necessary modules
import shutil
import json
from pathlib import Path

# Set paths for source and destination directories
source_directory= Path.cwd() / "profiles" 
destination_directory= Path.cwd() / "ineligible_profiles" 

# Create the destination directory if it doesn't exist
Path("ineligible_profiles").mkdir(exist_ok=True) 

# Iterate over JSON files in the source directory
for file in source_directory.glob("*.json"):
   with file.open("r") as x:
      data = json.load(x) 
      
      # Check if the profile meets the filtering criteria and if it does copy it to destination directory
      if len(data["companies"]) < 3 or len(data["skills"]) == 0: 
         shutil.copy(file, destination_directory) 