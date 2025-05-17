# String Methods

# capitalize
# Upper case the first letter in this sentence
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

txt = "36 is my age."
x = txt.capitalize()
print (x)


# String casefold() Method
# Make the string lower case:
# The casefold() method returns a string where all the characters are lower case.
a = "Hello, And Welcome To My World!"
b = a.casefold()
print(b)


# String center() Method
txt = "banana"
x = txt.center(20)
print(x)

# String count() Method
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# String split() Method
txt = "welcome to the jungle"
x = txt.split()
print(x)


txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)


# String index() Method
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# Where in the text is the first occurrence of the letter "e"?
txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10
txt = "Hello, welcome to my world."
x = txt.index('e', 5, 10)
print(x)

