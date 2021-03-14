my_list = [2, 4, 5, 6]

for index, value in enumerate(my_list):
    print(index, value)

# Create an array with 10 zeros.
my_list = [0] * 10

# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0

# Loop from 0 up to the number of elements
# in the array:
for index in range(len(my_list)):
    # Add element 0, next 1, then 2, etc.
    list_total += my_list[index]

# Print the result
print(list_total)

# Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Loop from 0 up to the number of elements
# in the array:
for index in range(len(my_list)):
    # Modify the element by doubling it
    my_list[index] = my_list[index] * 2

# Print the result
print(my_list)
"""
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
print(months[n * 3 - 3:n * 3])
"""

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(ord(c), end=" ")

plain_text = "This is a test. ABC abc"

for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    print(c2, end="")

plain_text = "This is a test. ABC abc"

encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)

plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)

x = {}

# Add some stuff to it
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1

# Fetch and print an item
print(x["fred"])
print(x)