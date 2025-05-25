# Remove list items

# The remove() method removes the specified item.
list = ["apple", "banana", "cherry"]
list.remove("banana")
print(list)

# remove() method removes the first occurrence
list = ["apple", "banana", "cherry", "banana", "kiwi"]
list.remove("banana")
print(list)

# Remove Specified Index
# The pop() method removes the specified index.
list = ["apple", "banana", "cherry", "banana", "kiwi"]
list.pop(1)
print(list)

# If you do not specify the index, the pop() method removes the last item.
list = ["apple", "banana", "cherry", "banana", "kiwi"]
list.pop()
print(list)

# The del keyword also removes the specified index:
list = ["apple", "banana", "cherry", "banana", "kiwi"]
del list[0]
print(list)

# The del keyword can also delete the list completely.
# del list

# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content
list = ["apple", "banana", "cherry", "banana", "kiwi"]
list.clear()
print(list)