#matching String using Shell Wildcard pattern

from fnmatch import fnmatch, fnmatchcase

a = fnmatch('foo.txt','*.txt')
print(a)

b = fnmatch('foo.txt','?oo.txt')
print(b)

c = fnmatch('Dat45','Dat[0-9]*')
print(c)

names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
d = [name for name in names if fnmatch(name,'Dat*.csv')]
print(d)

address = [
    '5412 N CLARK ST',
    '1060 W ADDISION ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]

e = [addr for addr in address if fnmatchcase(addr,'*ST')]
print(e)

f = [addr for addr in address if fnmatchcase(addr,'54[0-9][0-9]*CLARK*')]
print(f)