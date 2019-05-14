import re

def word_count(phrase):
    word_list = re.findall(r"([\da-zA-Z]+[']?[\da-zA-Z]+|[\da-zA-Z]+)", phrase.lower())
    word_counts = {}
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
