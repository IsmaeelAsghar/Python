# Tuples
# Tuple items are ordered, unchangeable, and allow duplicate values.

tuples = ("apple", "banana", "orange")
print(tuples)

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
# To determine how many items a tuple has, use the len() function:
tuple = ("apple", "banana", "cherry")
print(len(tuple))

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1))