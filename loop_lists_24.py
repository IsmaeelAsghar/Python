# Loop lists
# You can loop through the list items by using a for loop:
list = ["apple", "banana", "cherry", "banana"]
for item in list:
    print(item)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

list = ["apple", "banana", "cherry"]
for i in range(len(list)):
    print(list[i])

# Looping Using List Comprehension

# A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]