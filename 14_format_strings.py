# Format Strings
# we cannot combine strings and numbers

# Wrong format
age = 30
txt = "my name is johan, my age is:" + age
print(txt)

# use F-String
age = 30
txt = f"my name is johan, my age is {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:

txt = f"The price is {2*4} dollars"
print(txt)