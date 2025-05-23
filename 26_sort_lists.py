# Sort Lists
# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default

list = ["orange", "mango", "kiwi", "pineapple", "banana"]
list.sort()
print(list)

# Sort the list numerically
list = [100, 50, 65, 82, 23]
list.sort()
print(list)

# Sort Descending
# To sort descending, use the keyword argument reverse = True
list = ["orange", "mango", "kiwi", "pineapple", "banana"]
list.sort(reverse = True)
print(list)

# Customize Sort Function
# Sort the list based on how close the number is to 50

def func(n):
    return abs(n - 50)
list = [100, 50, 65, 82, 23]
list.sort( key = func)
print(list)

# Case Insensitive Sort
# Case sensitive sorting can give an unexpected result
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# So if you want a case-insensitive sort function, use str.lower as a key function
list = ["banana", "Orange", "Kiwi", "cherry"]
list.sort(key = str.lower)
print(list)


# Reverse Order

# The reverse() method reverses the current sorting order of the elements.
list = ["banana", "Orange", "Kiwi", "cherry"]
list.reverse()
print(list)