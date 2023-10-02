# Accessing Values in Strings

var1 = "Hello99!"
var2 = "Software Testing"
print("var1[0]:",var1[0])
print("var2[1:5]:",var2[1:5])
print('\n')

#Some more examples
x = "Hello World!"
print(x[:6])
print(x[0:6] + "Python3")
print('\n')

#Python String replace() Method
oldstring = 'I like world99'
newstring = oldstring.replace('like', 'love')
print(newstring)
print('\n')

#Changing upper and lower case strings
string="python at world99"
print(string.upper())
string="python at world99"
print(string.capitalize())
string="PYTHON AT WORLD99"
print(string.lower())
print('\n')

#Using "join" function for the string
print(":".join("Python"))
print('\n')

#Reversing String
string="12345"
print(''.join(reversed(string)))
print('\n')

#Split Strings
word="world99 career world99"
print(word.split(' '))
word="world99 career world99"
print(word.split('r'))
print('\n')

x = "World99"
x.replace("World99","Python")
print(x) # No changes observed. To make the change do the following
print('\n')

x = "World99"
x = x.replace("World99","Python")
print(x)
print('\n')
