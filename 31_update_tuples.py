# # Update Tuples
# # Once a tuple is created, you cannot change its values.
# # convert the tuple into a list, change the list, and convert the list back into a tuple.

# x = ("apple", "banana", "cherry")
# print(x)
# y = list(x)
# print(y)

# y[1] = "kivi"
# print(y)

# x = tuple(y)
# print(x)

# # Add Items
# # Convert the tuple into a list, add "orange", and convert it back into a tuple
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# y = list(thistuple)
# print(y)

# y.append("orrange")
# print(y)

# thistuple = tuple(y)
# print(thistuple)

# # Add tuple to a tuple
# # Create a new tuple with the value "orange", and add that tuple
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)


# Remove Items
# Convert the tuple into a list, remove "apple", and convert it back into a tuple
thistuple = ("apple", "banana", "cherry")

y = list(thistuple)
print(y)

y.remove("apple")
print(y)

thistuple = tuple(y)
print(thistuple)