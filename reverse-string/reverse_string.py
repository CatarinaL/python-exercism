def reverse(text):
    chars = [x for x in text]
    inverse = []
    while chars:
        inverse.append(chars.pop())
    return "".join(inverse)
