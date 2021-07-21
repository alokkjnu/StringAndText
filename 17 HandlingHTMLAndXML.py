# Handling HTML and XML Entities in Text

import html
from html.parser import HTMLParser

s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))

# Disable escaping of quotes

print(html.escape(s, quote= False))

s1 = 'Spicy Jalapeño'
c = s1.encode('ascii',errors='xmlcharrefreplace')
print(c)

s2 = 'Spicy &quot;Jalape&#241;o&quot.'
d = html.unescape(s2)
print(d)

from xml.sax.saxutils import unescape
t = 'the prompt is &gt;&gt;&gt;'
e  =  unescape(t)
print(e)