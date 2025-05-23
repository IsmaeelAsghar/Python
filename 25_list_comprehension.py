# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name
# Without list comprehension you will have to write a for statement with a conditional test inside
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# With list comprehension you can do all that with only one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in fruits]
print(newlist)


# Iterable
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
# Set the values in the new list to upper case:
nlist = [x.upper() for x in fruits]
print(nlist)

# Set all values in the new list
newlist = ['hello' for x in fruits]
print(newlist)

# Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orrange" for x in fruits]
print(newlist)

