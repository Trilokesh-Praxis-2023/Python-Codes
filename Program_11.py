# If Statement
# Example of working with conditional statement

"""Summary: A conditional statement in Python is handled by if statement and we
will see various other ways we can use conditional statements like "if and else
in this tutorial.
	"if condition"  - it is used when we need to print out the result when
	one of the conditions is true or false
	"else condition" - it is used when we want to print out the statement when
	our one condition fails to meet the requirement.
	"elif condition" - it is used when we have third possibility as the outcome.
	We can use multiple elif conditions to check.
	We can use minimal code to execute conditional statements by declaring all
	condition in single statement to run the code
	If statement can be be nested."""
	

def main():
    x, y = 2, 8

    if (x < y):
        st = "x is less than y"
    print(st)
    print('\n')

main()


# How to use "else condition"
# Example of working with conditional statement

def main():
    x, y = 8, 4

    if (x < y):
        st = "x is less than y"
    else:
        st = "x is greater than y"
    print(st)
    print('\n')

main()


# When "else condition" does not work
# Example of working with conditional statement
#
def main():
    x, y = 8, 8

    if (x < y):
        st = "x is less than y"
    else:
        st = "x is greater than y"
    print(st)
    print('\n')

main()


# How to use "elif" condition
# Example of working with conditional statement
#
def main():
    x, y = 8, 8

    if (x < y):
        st = "x is less than y"

    elif (x == y):
        st = "x is same as y"

    else:
        st = "x is greater than y"
    print(st)
    print('\n')

main()


# How to execute conditional statement with minimal code

def main():
    x, y = 10, 8
    st = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print(st)
    print('\n')

main()

# Nested if statement

total = 100
# country = "US"
country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
    print("Shipping Cost is $25")
elif total <= 150:
    print("Shipping Costs $5")
else:
    print("FREE")
if country == "AU":
    if total <= 50:
        print("Shipping Cost is  $100")
else:
    print("FREE")
    print('\n')


# Switch statement

def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    argument = 1
    print(SwitchExample(argument))
