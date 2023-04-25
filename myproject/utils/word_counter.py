import re

def count_words(text):
    words = re.findall(r'\w+', text)
    return len(words)
