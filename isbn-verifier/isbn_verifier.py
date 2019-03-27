import re


def verify(isbn):
    isbn_digits = isbn.replace("-", "")
    return is_valid_format(isbn_digits) and checksum(isbn_digits) == 0

# validate ISBN-10 format - [\dX]*, 10 digits without hyphens
def is_valid_format(isbn_digits):
    if re.match(r"[[\d]{9}(X|\d)$", isbn_digits) is None:
        return False
    return True

# convert each char to int, if X -> 10
# checksum
def checksum(isbn_digits):
    digits = zip(isbn_digits[:-1], range(10, 1, -1))
    digits = [int(x) * i for x, i in digits]
    return (sum(digits) + (10 if isbn_digits[-1] == 'X' else int(isbn_digits[-1]))) % 11


