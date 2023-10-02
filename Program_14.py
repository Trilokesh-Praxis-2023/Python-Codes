# Example of w+ and ^ Expression

""" A regular expression in a programming language is a special text string used for describing
a search pattern. It is extremely useful for extracting information from text such as code,
file, log, spreadsheets or even documents.

While using the regular expression the first thing is to recognize is that everything is
essentially a character, and we are writing patterns to match a specific sequence of characters
also referred to as string. ASCII and Latin letters are those that are on our keyboards and
Unicode is ised to match the foreign text. It includes digits and punctuation and all special
characters like $, #, @, !, % etc.

Regular Expression Syntax

    "re" module included with Python primarily used for string searching and manipulation.
    Also used frequently for web page "Scraping" (extract large amount of data from website)

Example of w+ and ^ expression
    "^": this expression matches the start of a string
    "w+": this expression matches the alphanumeric character in the string
"""

import re
xx = "Hello,education is fun"
r1 = re.findall(r"^\w+",xx)
r2 = re.findall(r"^\w",xx) # We remove the +sign, the output will only be the first letter "H" 
print(r1)
print(r2)


# Example of \s expression in re.split function
""" "s": this expression is used for creating a space in the string.
    '\s': allows us to parse each word in a string separately.
    When we remove "\" from s, there is no 's' letter in the ouput, this is because we have
    removed '\' from the string, and it evaluates "s" as a regular character and thus strips
    the words wherever it finds "s" in the string.
"""

import re
xx = "Hello,education is fun"
r1 = re.findall(r"^\w+", xx)
print((re.split(r'\s','we are splitting the words')))
print((re.split(r's','split the words')))


# Using re.findall for text
import re

list = ["Hello99 get", "Hello99 give", "Hello Selenium"]
for element in list:
    z = re.match("(g\w+)\W(g\w+)", element)
if z:
    print((z.groups()))

patterns = ['software testing', 'guru99']
text = 'software testing is fun?'
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
    if re.search(pattern, text):
        print('found a match!')
else:
    print('no match')
abc = 'hHello99@google.com, careerHello99@hotmail.com, users@yahoomail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails:
    print(email)

# Example of re.M or Multiline Flags
import re
xx = """Hello99 
careerguru99	
selenium"""
k1 = re.findall(r"^\w", xx)
k2 = re.findall(r"^\w", xx, re.MULTILINE)
print(k1)
print(k2)
