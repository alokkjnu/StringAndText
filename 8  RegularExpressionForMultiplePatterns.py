# Writing a Regular Expression for Multiple Patterns

import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is comment */'
text2 = '''/* this is a
                 multiline comment */
                 '''

t1 = comment.findall(text1)
print(t1)
t2 = comment.findall(text2)
print(t2)
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
t3 = comment.findall(text2)
print(t3)


comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
t4  = comment.findall(text2)
print(t4)

