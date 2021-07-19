#Searching and Replacing Text
import re
from calendar import month_abbr
text = 'yeah, but no, but yeah, but no, but yeah'
replace = text.replace('yeah','yep')
print(replace)

text1 = 'Today is 11/12/2021. PyCon starts 3/13/2013'
t1 = re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2', text1)
print(t1)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
t2 = datepat.sub(r'3-\1-\2',text1)
print(t2)
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))

t3 = datepat.sub(change_date,text1)
print(t3)

newtext, n = datepat.subn(r'\3-\1-\2',text1)
print(newtext)
print(n)