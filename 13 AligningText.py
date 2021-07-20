# Aliging Text Strings

text = 'Hello World'
a = text.ljust(20)
print(a)
b = text.rjust(20)
print(b)
c = text.center(20)
print(c)

d = text.rjust(20,'=')
print(d)
e = text.center(20,'*')
print(e)

f = format(text,'>20')
print(f)
g = format(text,'=>20')
print(g)
h = format(text,'*^20')
print(h)

a1 = '{:>10s} {:>10s}'.format('Hello','World')
print(a1)

x = 1.2345
a2 = format(x,'>10')
print(a2)

a3 = format(x,'>10.2f')
print(a3)

a4 = '%-20s' % text
print(a4)
a5 = '%20s' % text
print(a5)
a6 = '%-+20s' % text
print(a6)
a7 = '%+20s' % text
print(a7)
