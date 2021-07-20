# Stripping Unwanted Characters from Strings

# White Space stripping
s = '   hello world \n'
s1 = s.strip()
print(s1)
s2 = s.rstrip()
print(s2)

# Character Stripping
t = '--------hello======'
s3 = t.lstrip('-')
print(s3)

s4 = t.strip('-=')
print(s4)

s = '   hello world \n'
s5 = s.replace(' ', ' ')
print(s5)

import re
s6 =re.sub('\s+','', s)
print(s6)