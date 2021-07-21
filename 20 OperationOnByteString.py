# performing Text Operation on Byte Strings

data  = b'Hello World'
a = data[0:5]
print(a)
b = data.startswith(b'Hello')
print ( b )
c = data.split()
print(c)

d = data.replace(b'Hello',b'Hello Cruel')
print(d)

data = bytearray(b'Hello World')
e = data[0:5]
print(e)
f = data.startswith(b'Hello')
print(f)
g = data.split()
print(g)
h = data.replace(b'Hello',b'Hello Cruel')
print(h)