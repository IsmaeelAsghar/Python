# Booleans represent one of two values: True or False.

print(10 > 9)
print(10 == 9)
print(10 < 9)

# print a message based on condition
a = 200
b = 150

if b > a:
    print("b is greater than a")
else:
    print("b is less than a")
    
# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return
print(bool(25))
print(bool("Hello"))

# Evaluate variables
x = 10
y = "Hello"
print(bool(x))
print(bool(y))

# Almost any value is evaluated to True, except
# Any string is True, except empty string
# Any number is True, except 0
# Any list, tuple, set or dictionary are True, except empty ones
print(bool(['apple', 'banana', 'cherry']))

# Some False values
bool(None)
bool(False)
bool(0)
bool(())
bool({})
bool([])
bool("")

# if you have an object that is made from a class with a __len__ function that returns 0 or False:
class demo():
    def __len__(self):
        return 0
obj = demo()
print(bool(obj))

# Functions can Return a Boolean
def myfunc():
    return True
print(bool(myfunc))

# you can execute code based on the Boolean answer of function
def function():
    return True
if function:
    print("YES")
else:
    print("NO")

# Check if an object is in an integer or not
a = 10
print(isinstance(a, int))


