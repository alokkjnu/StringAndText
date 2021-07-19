# Normalizing Unicode Text to a Standard Representation
import unicodedata
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalape\u0303o'
print(s1)
print(s2)
print(s1 == s2)

t1 = unicodedata.normalize('NFC',s1)
t2 = unicodedata.normalize('NFC',s2)
print(t1 == t2)
print(ascii(t1))

t3 = unicodedata.normalize('NFD',s1)
t4 = unicodedata.normalize('NFD',s2)

print(t3 == t4)