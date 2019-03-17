import re 

#returns a boolean
def is_isogram(string):
    # Instead of using regex to strip all chars that are not letters, 
    # remove only whitespace and hyphen (specified in problem and tests)
    # using a list comprehension
    stripped_string = [char for char in string.lower() if char not in ('-', ' ')]
    set_string = set(stripped_string)
    return (len(stripped_string) == len(set_string))
