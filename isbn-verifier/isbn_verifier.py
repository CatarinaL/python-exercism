import re


def verify(isbn):
    isbn_digits = isbn.replace("-", "")
    if re.match(r"[[\d]{9}(X|\d)$", isbn_digits) is None:
        return False
    
    return True

# validate ISBN-10 format - [\dX]*, 10 digits without hyphens
def valid_digits_length(isbn):
    isbn_digits = isbn.replace("-", "")
    if re.match(r"[\dX]{10}", isbn_digits) is None:
        return False

# convert each char to int, if X -> 10

# checksum