from re import sub

def encode(message):
	return sub(r'(.)\1+', lambda m: str(len(m.group(0))) + m.group(1), message)

def decode(message):
	return sub(r'(\d+)(.)', lambda m: m.group(2) * int(m.group(1)), message)
