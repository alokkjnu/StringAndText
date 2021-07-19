# Matching Text at the start or End of a String

filename = 'spam.txt'
f1 = filename.endswith('.txt')
print(f1)
f2 = filename.startswith('file:')
print(f2)
f3 = filename.startswith('spam:')
print(f3)
f4 = filename.startswith('spam')
print(f4)

url = 'http://www.python.org'
f5 = url.startswith('http')
print(f5)

#If you need to check against multiple choice, Simple provide a tuple of posibilities to startwith() or endwith()

import os

filesname = os.listdir('.')
print(filesname)
f6  = [name for name in filesname if name.endswith(('.c','.py','.java'))]
print(f6)
f7 = any(name.endswith('.py') for name in filesname)
print(f7)

#####################################

from urllib.request import urlopen
def read_data(name):
    if name.startswith('http:','https:','ftp:'):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choice = ['http:','ftp:']
url = 'http://www.python.org'
#f8 = url.startswith(choice)
f8 = url.startswith(tuple(choice))
print(f8)

#####################################

filename = 'spam.txt'
f9 = filename[-4:] == '.txt'
print(f9)

#####################################

url = 'http://www.python.org'
f10 = url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp'
print(f10)

#####################################
import re
f11 = re.match('http:|https:|ftp:', url)
print(f11)