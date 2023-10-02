# Declare a variable and initialize it

f = 0
print(f)
print('\n')

#re-declaring the variable works
f = "Hello"
print(f)
print('\n')

#Concatenation of variables
a = "Hello"
b = 99
# print(a+b) Error
print(a+str(b))
print('\n')

# Declare a variable and initialize it
f = 101
print(f)
print('\n')

# Global vs. Local Variable in functions
def someFunction():
    f = "I am learning Python" # global f
    print(f)
someFunction()
print(f)
print('\n')

f = 101
print(f)
# Global vs. Local variables in functions
def someFunctions():
    global f
print(f)
print('\n')

f= "changing global variable"
someFunction()
print(f)
print('\n')
