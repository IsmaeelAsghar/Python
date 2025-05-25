# Global Variables
# Variables that are created outside of a function

x = "awesome"
def func():
    print("Python is " + x )

func()

# When you create the variable inside the function that is local variable and only access withen the function
x = "Object oriented lenguage"
def func():
    x = "funtestic"
    print("Python is " + x )
func()
print("Python is " + x )

# If use the global keyword the varible belongs to the global scope

def func():
    global x

    x = "OOP"
func()
print("Python is " + x)

# To change the value of global variable inside the function refers the variable by using the global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

