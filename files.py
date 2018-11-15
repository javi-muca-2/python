# ---------------------------------------------------------------------
# - Python Files Summary:
# ---------------------------------------------------------------------

'''
- Naming:
  - Don't use the 'file' word.
  - It's classified as an identifier (just reserved, not in use).
'''


# - Opening and closing files:
# ---------------------------------------------------------------------

# Modes:
# r -> read; w -> overwrite;  a -> append; r+ -> read and write;

txt = 'Hello\nWorld!\n'

# Unsafe method
text_file = open('hello.txt','w')
text_file.write(txt)
text_file.close()

# Safe method
try:
    text_file = open('hello.txt','w')
    text_file.write(txt)
finally:
    text_file.close()

# Safe and automatic. Recommended!
with open('hello.txt','w') as text_file:
    text_file.write(txt)



# - Reading and Writing functions:
# ---------------------------------------------------------------------
# Check them in ipython.

# text_file.read()      # All contents, with all newlines.
# text_file.readline()  # A string ending in a newline, except if EOF.
# text_file.readlines() # Array of strings with newlines, except maybe the last one (EOF).

# text_file.write()       # Writes the string. Doesn't add a newline.
# text_file.writelines()  # Writes the array of strings. Doesn't add a newlines.



# - Big data:
# ---------------------------------------------------------------------
# Read line by line to avoid memory consumption.

# While loop
with open('hello.txt','r') as text_file:
    line = text_file.readline()
    while line:
        print(line, end='')
        line = text_file.readline()


# Shorter form
with open('hello.txt','r') as text_file:
    for line in text_file:
        print(line, end='')


# - Newlines:
# ---------------------------------------------------------------------

# Reading:
# - All read(), readline() and readlines() keep the newline in the string.

# Removing newlines:
# .rstrip() -> Remove whitespace characters like `\n` at the end of each line
# .strip() -> Remove whitespace characters both at the beginning and the end

with open('hello.txt','r') as text_file:
    lines = [line.rstrip('\n') for line in text_file]
    print(lines)


# Writing:
# - Just write '\n' in strings. Python will convert it according to the OS:
#   - \n (Linux)
#   - \r\n (Windows)
#   - \r (Mac)


# - Removing files:
# ---------------------------------------------------------------------

import os
os.remove('hello.txt')

# ---------------------------------------------------------------------

