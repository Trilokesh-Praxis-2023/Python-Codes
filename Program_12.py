# How to use "while loop"
# Example of working with loops

def main():
    x = 0
    # define a while loop
    while (x < 4):
        print(x)
        x = x + 1

main()
print('\n')

# How to use "for loop"
# Example of working with loops

def main():
    x = 0

#define a while loop
#	while(x <4):
#		print x
#		x = x+1

# Define a for loop
for x in range(2, 7):
    print(x)

main()
print('\n')

# How to use For Loop for String
def main():
    # use a for loop over a collection
    Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for m in Months:
        print(m)

main()
print('\n')

# How to use break statements in for Loop
def main():
    # use a for loop over a collection
    # Months = ["Jan","Feb","Mar","April","May","June"]
    # for m in Months:
    # print m

    # use the break and continue statements
    for x in range(10, 20):
        if (x == 15): break
        # if (x % 2 == 0) : continue
        print(x)

main()
print('\n')

# How to use "continue statement" in For Loop
def main():
    # use a for loop over a collection
    # Months = ["Jan","Feb","Mar","April","May","June"]
    # for m in Months:
    # print m

    # use the break and continue statements
    for x in range(10, 20):
        # if (x == 15): break
        if (x % 5 == 0): continue
        print(x)

main()
print('\n')

# How to use "enumerate" function for "For Loop"
# Returns the index number along with the elements
def main():
    # use a for loop over a collection
    Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for i, m in enumerate(Months):
        print(i,m)

main()
print('\n')

def main():
    # use the break and continue statements
    for x in range (10,20):
        if (x == 15): break
        if (x % 5 == 0) : continue
        print(x)

main()
print('\n')
