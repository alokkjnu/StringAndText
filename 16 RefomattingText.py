# Refomatting Text to a fixed Number of Columns

import textwrap
import os

s = " Look into my eyes, Look into my eyes, the eyes, the eyes, \
the eyes, not around my eyes, don't look around my eyes, \
look into my eyes, you're under."

print(textwrap.fill(s,70))
print(textwrap.fill(s,40))
print(textwrap.fill(s,40, initial_indent='  '))
print(textwrap.fill(s,40,subsequent_indent='    '))
print(os.get_terminal_size().columns)