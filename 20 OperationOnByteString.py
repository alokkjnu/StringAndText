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