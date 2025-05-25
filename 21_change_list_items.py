# Change list items

# To change the value of a specific item, refer to the index number:
list = ["apple", "banana", "cherry"]
list[1] = "mango"
print(list)

# Change the range of item values
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list[2:4] = ["watermelon", "blackcurrant"]
print(list)

# Change the second value by replacing it with two new values
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list[1:2] = ["watermelon", "blackcurrant"]
print(list)

# Change the second and third value by replacing it with one value
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list[1:3] = ["watermelon"]
print(list)

# The insert() method inserts an item at the specified index
list = ["apple", "banana", "cherry"]
list.insert(2, "orange")
print(list)
