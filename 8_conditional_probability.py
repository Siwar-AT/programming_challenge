# Task (5):
# Calculate the conditional probability of each language with each company (P(language|company))

# Formula used:
# P(language|company)= P(language ∩ company) / P(company)
#                    = (co-occurrences of language with company/total profiles) / (occurrences of company/total profiles) 
#                    = co-occurrences of language with company / occurrences of company 


# Import necessary modules
import json 
from pathlib import Path

# Set path for input and output files
input_file1 = Path.cwd()/"company_occurrence_data.json" 
input_file2 = Path.cwd()/"cooccurrence_data.json" 
output_file = Path.cwd()/"conditional_probabilities.json"

# Define dictionary to store conditional probabilities
probabilities ={}
             
# Load company occurrence data from input file
with input_file1.open("r") as f:
    occurrence_data= json.load(f)
    occurrences= occurrence_data.get("Company Occurrence Counts", {}) 

# Load co-occurrence data of language and company from input file       
with input_file2.open("r") as c:
    cooccurrence_data= json.load(c)
    cooccurrences= cooccurrence_data.get("Co-occurrence Counts of Languages with Companies", {})

# Print message to screen 
print("Calculating conditional probabilities...")
print(" ")

# Iterate through the co-occurrence data for each programming language
for language, cooccurrences_dict in cooccurrences.items():
        
    # Iterate through each company and obtain its occurrence data
    for company, count in cooccurrences_dict.items():
        company_occurrences= occurrences.get(company)
            
        # Calculate conditional probability
        conditional_probability= round(count / company_occurrences, 2)
            
        # Print conditional probabilities to screen
        print(f" P({language}|{company}) = {conditional_probability}")
            
        # Store conditonal probabilities in the defined dictionary 
        probabilities[f" P({language}|{company})"]= conditional_probability

# Write the dictionary containing conditional probabilities to output file           
with output_file.open("w") as f:
    json.dump(probabilities, f, indent = 2)

print(" ")
print("<< The conditional probability calculation results have been stored in 'conditional_probabilities.json' >>")

# This print statement is also for aesthetic purposes :)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 