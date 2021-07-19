# Matching and Searching for Text Patterns

text = 'yeah, but no, but yeah, but no, but yeah'

#Exact Match

text == 'yeah'
#output : False
text.startswith('yeah')
#output : True
text.endswith('no')
#output : False

text1 = '11/27/2021'
text2 = 'Nov 27, 2021'

import re

#simple matching : \d+ means match one or more digits

if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')


if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text3 = 'Today is 19/07/2021. PyCon starts 3/13/2012'
t1 = datepat.findall(text3)
print(t1)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('19/07/2021')
print(m)

#Extract the contents of eaach group

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

# find all matches (splitting into tuples)
text4 = 'Today is 19/07/2021. PyCon starts 3/13/2012'
t2 = datepat.findall(text4)
print(t2)