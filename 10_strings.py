# Python strings

# strings in python 'hello' and "hello" are same

# Quotes Inside Quotes
print("He is called 'Jonnhy'")
print("It's all right")

# Multiline String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String as array
a = "Hello world"
print(a[1])

# Loop through string
for x in "banana":
    print(x)

# String Length
a = "Jonnhy"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("yes, 'free' is present")

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

