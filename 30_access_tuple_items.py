# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

tuple = ("apple", "banana", "cherry")
print(tuple[1])

# Negative Indexing
# Print the last item of the tuple:
tuple = ("apple", "banana", "cherry")
print(tuple[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple1[2:5])

# Range of Negative Indexes
tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple[-4:-1])


# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword

tuple = ("apple", "banana", "cherry")
if "apple" in tuple:
    print("yes")