# How to define Python classes
# Example of working with classes

""" To define class we need to consider the following points:
	1. In Python, classes are defined by the "Class" keyword.
	2. Inside classes, we can define functions or methods that are part of
	   the class.
	3. The "self" argument refers to the object itself. Hence the use of the
	   word slef. So inside this method, self will refer to the specific
	   instance of this object that's being operated on.
	4. Self is the name preferred by convention in Python to indicate the first
	   parameter of instance method in Python. It is the part of the Python syntax
	   to access members of objects. """
	
class myClass():
    def method1(self):
        print("Hello")

    def method2(self, someString):
        print("Software Testing:" + someString)


def main():
    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2(" Testing is fun")

main()
print('\n')

# How Inheritance works
# Example of working with classes
# Python Inheritance Syntax
""" class DerivedClass(BaseClass):
        body_of_derived_class"""

class myClass():
    def method1(self):
        print("Hello")


class childClass(myClass):
    # def method1(self):
    # myClass.method1(self);
    # print "childClass Method1"

    def method2(self):
        print("childClass method2")


def main():
    # exercise the class methods
    c2 = childClass()
    c2.method1()
    c2.method2()


if __name__ == "__main__":
    main()
