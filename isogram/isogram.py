import re 

#returns a boolean
def is_isogram(string):
    stripped_string = re.sub(r"[^a-zA-Z]+", "", string.lower())
    set_string = set([char for char in stripped_string])
    if(len(stripped_string) > len(set_string)):
        return False
    return True
