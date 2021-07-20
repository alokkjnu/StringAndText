# Interpolating Variables in String

s = '{name} has {n} message.'
a = s.format(name = 'alok' , n =25)
print(a)

name = 'alok'
n = 25
b = s.format_map(vars())
print(b)

class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n

a1 = Info('alok',25)
b1 = s.format_map(vars(a1))
print(b1)

class SafeSub(dict):
    def __missing__(self,key):
        return '{'+key+'}'

del n
c1 = s.format_map(SafeSub(vars()))
print(c1)

import sys
def sub(text):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))

name = 'alok'
n = 25
color = 'red'
print(sub('Hello,{name}'))
print(sub("you have {n} messages"))
print(sub('your fav color is {color}'))
