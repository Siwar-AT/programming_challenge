# Main program used to automatically run all scripts sequentially
import subprocess

# Task (1):
# Run the archive unpacking
subprocess.run(["python3", "1_extracting_profiles.py"], check= True)

# Task (2), Step (1):
# Run filtering of eligible profiles
subprocess.run(["python3", "2_filtering_eligible_profiles.py"], check= True)

# Task (2), Step (2):
# Run filtering of ineligible profiles
subprocess.run(["python3", "3_filtering_ineligible_profiles.py"], check= True)

# Task (2), Step (3):
# Run validation of filtering process
subprocess.run(["python3", "4_validation_of_filtering.py"], check= True)

# Task (3), Step (1):
# Run extraction of companies
subprocess.run(["python3", "5_company_extraction.py"], check= True)

# Task (3), Step (2):
# Run calculations of company occurrences
subprocess.run(["python3", "6_company_occurrences.py"], check= True)

# Task (4):
# Run calculations of language-company co-occurrences 
subprocess.run(["python3", "7_language_company_cooccurrences.py"], check= True)

# Task (5):
# Run calculations of conditional probabilities
subprocess.run(["python3", "8_conditional_probability.py"], check= True)