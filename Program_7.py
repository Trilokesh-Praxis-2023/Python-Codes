# Python TUPLE - Pack, Unpack, Compare, Slicing, Delete, Key

""" A tuple is just like a list of a sequence of immutable python objects.
The difference between list and tuple is that list are declared in square brackets
and can be changed while tuple is declared in parentheses and cannot be changed.
However, you can take portions of existing tuples to make new tuples."""

""" To write an empty tuple, we need to write as two parenthese containing nothing.
tup1 =();

For writing tuple for a single value, you need to include a comma, even though there
is a single value. Also at the end you need to write semicolon as shown below.
tup1 = (50,);

Tuple indices begin at 0, and they can be concatenated, sliced and so on.

In this tutorial, we will learn:
	Packing and Unpacking
	Comparing tuples
	Using tuples as keys in dictionaries
	Deleting tuples
	Slicing of tuple
	Built-in functions with tuples
	Advantages of tuples over lists"""

tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])
print(tup2[1:4]) # calling the elements between 1 and 4 including the one at 1
print('\n')

# Packing and Unpacking
# In packing, we place value into a new tuple while in unpacking, we extract the value
x = ("Hello", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)
print('\n')

# Comparing tuples
# A comparison operator in Python works with tuples.
# The comparison starts with the first elements of each tuple. 

# case 1
a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")
print('\n')

# case 2
a=(5,6)
b=(5,4)
if (a>b):print("a is bigger")
else: print("b is bigger")
print('\n')

# case 3
a=(5,6)
b=(6,4)
if (a>b):print("a is bigger")
else: print("b is bigger")
print('\n')

# Tuples and dictionary
""" Since tuples are hashable, and list is not, we must use the tuple as the
key if we need to create a composite key to use in a dictionary.
Tuples are immutable and cannot be deleted, but deleting tuple entirely is possible
by using the keyword "del". """
a = {'x':100, 'y':200}
b = a.items()
print(b)
print('\n')

# Slicing of Tuple
""" To fetch specific sets of sub-elements from tuple or list, we use this unique
function called slicing. Slicing is not only applicable to tuple but also for array
and list."""
x = ("a", "b","c", "d", "e")
print(x[2:4])
print('\n')

"""Advantages of tuples over list:
	Iterating through tuple is faster than with list, since tuples are immutable.
	Tuples that consist of immutable elements can be used as key for dictionary, which
	is not possiblw with list
	If we have data that is immutable, implementing it as a tuple will guarantee that
	it remians write-protected"""
	
