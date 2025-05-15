import shutil 
import json
from pathlib import Path
from collections import defaultdict
from company_occurrence_module import count_occurrences 
from language_company_cooccurrence_module import count_cooccurrences
from conditional_probability_module import calculate_probability

# Task (1): Unpack the archive to extract the directory containing the profiles.
print("Unpacking archive...") # These print statements were added to update the user, so that the screen doesn't stay blank 
archive_file = Path.cwd()/"profiles.tar.gz"
extract_dir = Path.cwd()
archive_format = "gztar"
shutil.unpack_archive(archive_file, extract_dir, archive_format) 
source_directory= Path.cwd()/"profiles"  

# Task (2): Extract the companies from all profiles 
# Didn't create a module for this step because it would have unnecessarily complicated the code  
print("Extracting companies...")
list_of_companies= []
for file in source_directory.glob("*.json"): 
    with file.open("r") as f:
        data= json.load(f)
        if len(data["companies"]) >=3 and len(data["skills"])> 0: 
           companies = data.get("companies")  
           list_of_companies.extend(companies)
company_data= {"List of Companies": list_of_companies}

# Task (3): Count the ocurrences of each company 
print("Counting company occurrences...")
company_occurrences= count_occurrences(company_data)

# Task (4): Calculate the co-occurrences of each language with each company 
print("Counting language-company cooccurrences...") 
final_cooccurrences = defaultdict(lambda: defaultdict(int))
for file in source_directory.glob("*.json"):
    with file.open("r") as f:
        data= json.load(f)
        if len(data["companies"]) >=3 and len(data["skills"])> 0:
           cooccurrences = count_cooccurrences(data)
           for lang, companies in cooccurrences.items():
              for company, count in companies.items():
                 final_cooccurrences[lang][company] += count      
lang_comp_cooccurrence= {"Co-occurrence Counts of Languages with Companies": {lang: dict(companies) for lang, companies in final_cooccurrences.items()}}

# Task (5): Calculate the conditional probabilities
print("Calculating conditional probabilities...") 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # Added to make the screen more organised (not necessary)
conditional_probabilities = calculate_probability(company_occurrences, lang_comp_cooccurrence)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          
output_file = Path.cwd()/"conditional_probabilities.json"  # Stores the conditional probability results for easy access 
with output_file.open("w") as f:
    json.dump(conditional_probabilities, f, indent = 2)   
print("<< The conditional probabilities have been stored in 'conditional_probabilities.json' >>")