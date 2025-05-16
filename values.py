# Assign multiple values 

# Python allows to assign multiple values to multiple variables in one line

x, y, z = "apple", "banana", "orange"
print(x)
print(y)
print(z)

# Assign same value to multiple variables

x = y = z = "banana"
print(x)
print(y)
print(z)

# Unpack a collection
# if you have collection of variables in dictionary or tuples python can allow you the extract values into variables.

fruits = ['banana', 'apple', 'orange']

x, y, z = fruits
print(x)
print(y)
print(z)
