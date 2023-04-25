import re

def extract_tags(text, prefix='#'):
    pattern = re.compile(rf'{prefix}\w+')
    tags = pattern.findall(text)
    return tags
