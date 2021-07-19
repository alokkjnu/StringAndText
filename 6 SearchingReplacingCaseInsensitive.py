# Searching and replacing Case-Insensitive Text
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
t1 = re.findall('python',text, flags=re.IGNORECASE)
print(t1)
t2  = re.sub('python','snake',text, flags=re.IGNORECASE)
print(t2)

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

t3 = re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
print(t3)