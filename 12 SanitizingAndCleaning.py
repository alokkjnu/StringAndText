# Sanitizing and Cleaning Up Text

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap = {
    ord('\t'):' ',
    ord('\f'):' ',
    ord('\r'):None
}
a = s.translate(remap)
print(a)

import unicodedata
import sys
cmb_chars = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD',a)
print(b)

c = b.translate(cmb_chars)
print(c)

digitmap = { c: ord('0') + unicodedata.digit(chr(c))
for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'}
d = len(digitmap)
print(d)

print(a)
e = unicodedata.normalize('NFD',a)
f = e.encode('ascii','ignore').decode('ascii')
print(f)

def clean_space(s):
    s = s.replace('\r',' ')
    s = s.replace('\t',' ')
    s = s.replace('\f',' ')
    return s