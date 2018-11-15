# ---------------------------------------------------------------------
# - Python Regexps Summary:
# ---------------------------------------------------------------------

'''
- Why?:
  - Strand processing (DNA, RNA...)
  - Biopython libs
  - Awk (-> Perl -> Python, Ruby, many langs...)
  - Parsing files, Scraping web pages
  - Systems programming


- Python regexp lib:
  - Docs      -> https://docs.python.org/3/library/re.html
  - Tutorial  -> https://docs.python.org/3/howto/regex.html


- Regex Tutorials:
  - Basics: https://regexone.com/
  - Python: https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial
  - Debugger: https://regex101.com/
'''


# - Basic functions:
# ---------------------------------------------------------------------
# r'...' -> Raw string. Does not interpret backslashes.

import re

txt = 'Hola a todos! Hola de verdad!'
reg = r'Hola'
pat = re.compile(reg)

# Two main uses: Search and substitute.

# 1. Search
pat.search(txt)   # Only first match. Returns MatchObject. Can be None.
pat.finditer(txt) # Multiple matches. Returns iter of MatchObjects.

# 2. Substitute
pat.sub('Adiós', txt)      # Returns new string


# MatchObj
# m.start()
# m.end()     # End NOT included! Like slices!
# m.group()   # No param = Group 0 = The whole match; Group 1 = First subgroup, etc.


# MatchObj Examples:
[(m.start(0), m.end(0), m.group(0)) for m in pat.finditer(txt)]

for m in pat.finditer(txt):
  print(m.start(0), m.end(0), m.group(0))



# - More functions:
# ---------------------------------------------------------------------

# Ignore Case
txt = 'Hola a todos! Hola de verdad!'
reg = r'hola'
pat = re.compile(reg)
[(m.start(0), m.end(0), m.group(0)) for m in pat.finditer(txt)]

txt = 'Hola a todos! Hola de verdad!'
reg = r'hola'
pat = re.compile(reg, re.IGNORECASE)
[(m.start(0), m.end(0), m.group(0)) for m in pat.finditer(txt)]


# Groups
txt = '¡Hola!'
reg = r'(Ho)(la)'
pat = re.compile(reg)
match = pat.search(txt)

print(match.start(0), match.end(0), match.group(0))
print(match.start(1), match.end(1), match.group(1))
print(match.start(2), match.end(2), match.group(2))


# Substitution using groups
txt = 'ejercicio.txt'
reg = r'(\w*)\.(\w*)'
pat = re.compile(reg)

[(m.start(0), m.end(0), m.group(0)) for m in pat.finditer(txt)]
[(m.start(1), m.end(1), m.group(1)) for m in pat.finditer(txt)]
[(m.start(2), m.end(2), m.group(2)) for m in pat.finditer(txt)]

sub = r'\1-de-pablo.\2'
pat.sub(sub, txt) # => Returns a new string


# Substitution using raw + template strings
# https://www.python.org/dev/peps/pep-0498/
# https://docs.python.org/3/library/string.html
# https://docs.python.org/3/library/string.html#template-strings
for i in range(4):
  sub = rf'\1-{i:#02}.\2'
  print(pat.sub(sub, txt))



# - Regex Flags:
# ---------------------------------------------------------------------

# Unexpected result:
txt = 'Hello\nWorld!'
reg = r'^.*$'
pat = re.compile(reg)
matches = pat.finditer(txt)
print([(m.start(0), m.end(0), m.group(0)) for m in matches])
# => []


# - re.DOTALL: '.' matches any character including newlines.
#              By default newlines aren't.
txt = 'Hello\nWorld!'
reg = r'^.*$'
pat = re.compile(reg, re.DOTALL)
matches = pat.finditer(txt)
print([(m.start(0), m.end(0), m.group(0)) for m in matches])
# => [(0, 12, 'Hello\nWorld!')]


# - re.MULTILINE:
#   - ^ Matches the beginning of every line, not only of txt
#   - $ Matches the end of every line, not only of txt
txt = 'Hello\nWorld!'
reg = r'^.*$'
pat = re.compile(reg, re.MULTILINE)
matches = pat.finditer(txt)
print([(m.start(0), m.end(0), m.group(0)) for m in matches])
# => [(0, 5, 'Hello'), (6, 12, 'World!')]


# - Pipe: The pipe ('|') allows using several options (bitwise OR)
txt = 'Hello\nWorld!'
reg = r'^.*$'
pat = re.compile(reg, re.DOTALL | re.MULTILINE)
matches = pat.finditer(txt)
print([(m.start(0), m.end(0), m.group(0)) for m in matches])
# => [(0, 12, 'Hello\nWorld!')]



# - Lazy matches:
# ---------------------------------------------------------------------
# https://www.rexegg.com/regex-quantifiers.html
# https://docs.python.org/3/library/re.html

txt = 'aaa'
reg = r'a*'
pat = re.compile(reg)
print([(m.start(), m.end(), m.group(0)) for m in pat.finditer(txt)])
# => [(0, 3, 'aaa')]

txt = 'aaa'
reg = r'a*?'
pat = re.compile(reg)
print([(m.start(), m.end(), m.group(0)) for m in pat.finditer(txt)])
# => [(0, 0, ''), (1, 1, ''), (2, 2, ''), (3, 3, '')]

txt = 'aaa'
reg = r'a+?'
pat = re.compile(reg)
print([(m.start(), m.end(), m.group(0)) for m in pat.finditer(txt)])
# => [(0, 1, 'a'), (1, 2, 'a'), (2, 3, 'a')]

txt = 'AxxxZxxxZxxxZ'
reg = r'A.*Z'
pat = re.compile(reg)
print([(m.start(), m.end(), m.group(0)) for m in pat.finditer(txt)])
# => [(0, 13, 'AxxxZxxxZxxxZ')]

txt = 'AxxxZxxxZxxxZ'
reg = r'A.*?Z'
pat = re.compile(reg)
print([(m.start(), m.end(), m.group(0)) for m in pat.finditer(txt)])
# => [(0, 5, 'AxxxZ')]



# - Overlapping Regexes:
# ---------------------------------------------------------------------

# Capture the text 'TAT'.
txt = 'TAT'
reg = r'TAT'
pat = re.compile(reg)
matches = pat.finditer(txt)

for m in matches:
    print(m.start(0), m.end(0), m.group(0))


# Same as before. The regex can't return overlapping sequences.
# This problem has to be solved with a lookahead.
txt = 'TATAT'
reg = r'TAT'
pat = re.compile(reg)
matches = pat.finditer(txt)

for m in matches:
    print(m.start(0), m.end(0), m.group(0))


# Example of a Lookahead.
# - Lookaheads do not consume input.
# - Lookaheads do not form a group.
txt = 'Hola Pablo Picasso'
reg = r'Pablo (?=Picasso)'
pat = re.compile(reg)
matches = pat.finditer(txt)

for m in matches:
    print(m.start(0), m.end(0), m.group(0))


# Regexp that returns overlapping matches using a lookahead.
# - The empty string matches every position in txt.
# - The lookahead filters the matches.
# - Make a group inside the lookahead to capture its contents.
txt = 'TATAT'
reg = r'(?=(TAT))'
pat = re.compile(reg)

# Group 0 = ''
matches = pat.finditer(txt)
for m in matches:
    print(m.start(0), m.end(0), m.group(0))

# Group 1 = 'TAT'
matches = pat.finditer(txt)
for m in matches:
    print(m.start(1), m.end(1), m.group(1))



# - Iterators:
# ---------------------------------------------------------------------
# Remember that you can't reuse an iterator!

txt = 'Blue Blue'
reg = r'Blue'
pat = re.compile(reg)
matches = pat.finditer(txt)


# Prints correctly
print([(m.start(0), m.end(0), m.group(0)) for m in matches])

# Prints nothing
print([(m.start(0), m.end(0), m.group(0)) for m in matches])

# Prints correctly again
matches = pat.finditer(txt)
print([(m.start(0), m.end(0), m.group(0)) for m in matches])

print()


# Analyzing iterators
matches = pat.finditer(txt)
dir(matches)
matches.__next__()
matches.__next__()
# matches.__next__()  # StopIteration


# Dump the results of the iterator into an array to be safe:
matches = list(pat.finditer(txt))

# Prints correctly
print([(m.start(0), m.end(0), m.group(0)) for m in matches])

# Prints correctly
print([(m.start(0), m.end(0), m.group(0)) for m in matches])

# Prints correctly
print([(m.start(0), m.end(0), m.group(0)) for m in matches])

# ---------------------------------------------------------------------

