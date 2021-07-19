# Specifying a Regualar Expression for the Shortest Match

import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
t1 = str_pat.findall(text1)
print(t1)
text2 = 'Computer says "no." Phone says "yes."'
t2 = str_pat.findall(text2)
print(t2)

str_pat = re.compile(r'\"(.*?)"')
t3 = str_pat.findall(text2)
print(t3)