def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = set([char for char in sentence.lower()])
    for letter in alphabet:
        if letter not in s:
            return False
    return True
