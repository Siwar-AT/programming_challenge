from collections import defaultdict

def count_cooccurrences(input):
    co_occurrence_count = defaultdict(lambda:defaultdict(int))
    languages = input.get("skills")
    companies = input.get("companies")
    for language in languages:
        for company in companies:
            co_occurrence_count[language][company] += 1
    return (co_occurrence_count)