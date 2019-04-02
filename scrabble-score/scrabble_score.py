'''
Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
'''
def score(word):
    word = word.upper()
    values = (1, 2, 3, 4, 5, 8, 10)
    letter_groups = [('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'), ('D', 'G'), ('B', 'C', 'M', 'P'), ('F', 'H', 'V', 'W', 'Y'), ('K'), ('J', 'X'), ('Q', 'Z')]
    score_dict = dict(zip(values, letter_groups))
    letter_values = [value for char in word for value, group in score_dict.items() if char in group]
    return sum(letter_values) if letter_values else 0


