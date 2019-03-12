import re

def abbreviate(words):
    results = re.findall("(?:[^a-zA-Z]*([a-zA-Z])[a-zA-Z']*)", words)
    acronym = "".join(results)
    return acronym.upper() 