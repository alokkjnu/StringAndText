# Combining and Concatenating Strings

parts = ['Is','Chicago','Not','Chicago']
a = ' '.join(parts)
print(a)
b = ','.join(parts)
print(b)
c = ''.join(parts)
print(c)

a1 = 'Is Chicago'
b1 = 'Not Chicago?'
d = a1+ '' +b1
print(d)

print('{}{}'.format(a1,b1))
print(a1+''+b1)

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago'

text = ''.join(sample)
print(text)
for part in sample():
    f.write(parts)

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ' '.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)
for part in combine(sample(),32768):
    f.write(part)