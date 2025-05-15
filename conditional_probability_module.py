# Formula used to calculate conditional probability:
# P(language|company)= P(language ∩ company) / P(company)
#                    = (co-occurrences of language with company/total profiles) / (occurrences of company/total profiles) 
#                    = co-occurrences of language with company / occurrences of company 

def calculate_probability(x, y):
    probabilities ={}
    occurrences= x.get("Company Occurrence Counts", {})
    cooccurrences= y.get("Co-occurrence Counts of Languages with Companies", {})
    for language, cooccurrences_dict in cooccurrences.items():
        for company, count in cooccurrences_dict.items():
            company_occurrences= occurrences.get(company)
            conditional_probability= round(count / company_occurrences, 2)
            print(f" P({language}|{company}) = {conditional_probability}")
            probabilities[f" P({language}|{company})"]= conditional_probability
    return (probabilities)