# Splitting Strings on Any of Multiple Delimiters
import re

line = 'asdf fjdk; afed, fjek,asdf,   foo'
re.split(r'[;,\s]s*',line)

fields = re.split(r'(;|,|\s)s*',line)
print(fields)

values = fields[::2]
delimiters = fields[1::2]+['']
print(values)
print(delimiters)

#Reform the line using same Delimiters
reform = ''.join(v+d for v,d in zip(values,delimiters))
print(reform)

delimit = re.split(r'(?:,|;|s)\s*',line)
print(delimit)