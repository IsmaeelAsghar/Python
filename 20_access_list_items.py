# Access list items 
a = [1, 2, 3, 4, 5]
print(a[1])
print(a[-1])

# Using List Comprehension
b = [10, 15, 20, 25, 30, 35, 40]
# create new list with item greater than 25
c = [item for item in b if item > 25]
print(c)

# Using loop
a = [10, 20, 30, 40, 50]
# Loop through the list and print each item
for item in a:
    print(item)

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# 4 index not included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Start form index 2 upto end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# return item from -4 to -1 but (-1 not included)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if item exists
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in list:
    print("YES")
else:
    print("NO")