from pathlib import Path
from collections import Counter

def count_occurrences(input):
    counts = Counter(input.get("List of Companies"))
    counts_dict= {"Company Occurrence Counts":dict(counts)}
    return (counts_dict)