def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = sentence.lower()
    for letter in alphabet:
        if (s.find(letter) == -1):
            return False
    return True
