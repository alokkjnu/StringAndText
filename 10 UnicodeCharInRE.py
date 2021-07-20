# Working with Unicode Charactes in Regular Expression

import re
num = re.compile('\d+')
#ASCII Digits
n1 = num.match('123')
print(n1)

arabic = re.compile('[\u0600-\u06ff-\u0750-\u077f-\u08a0-\u08ff]+')
print(arabic)
