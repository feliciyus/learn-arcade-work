"""

for i in range(10):
    print("*", end=" ")
print()
for i in range(5):
    print("*", end=" ")
print()
for i in range(20):
    print("*", end=" ")

"""

"""
for row in range(8):
    for column in range(10):
        print("*", end=" ")
    print()

for row in range(10):
    for column in range(5):
        print("*", end=" ")
    print()

for row in range(5):
    for column in range(20):
        print("*", end=" ")
    print()

"""
"""
for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()

for i in range(10):
    for j in range(10):
        print(i, end=" ")
    print()
"""

"""
for i in range(10):
    for j in range(i + 1):
        print(j, end=" ")
    print()
"""

"""
for i in range(10):
    for space in range(i):
        print(" ", end=" ")
    for j in range(10 - i):
        print(j, end=" ")
    print()
"""

"""
for i in range(1, 10):
    for j in range(1, 10):
        if (j) * (i) < 10:
            print(" ", end="")
        print((j) * (i), end=" ")
    print()
"""

"""
for i in range(1, 10):
    if i < 9:
        print((18 - i * 2) * " ", end="")
    for j in range(i):
        print(j + 1, end=" ")
    for r in range(i - 1):
        print(j - r, end=" ")
    print()

"""
"""
for i in range(1, 10):
    if i < 9:
        print((18 - i * 2) * " ", end="")
    for j in range(i):
        print(j + 1, end=" ")
    for r in range(i - 1):
        print(j - r, end=" ")
    print()

for i in range(1, 10):
    for space in range(i):
        print(" ", end=" ")
    for j in range(9 - i):
       print(j + 1, end=" ")
    print()
    
#"""

#"""
for i in range(10):
    for j in range(10-i):
        print(" ", end=" ")
    for j in range(i):
        print(j + 1, end=" ")
    for r in range(i - 1):
        print(j - r, end=" ")
    print()


for i in range(2, 10):
    for space in range(i):
        print(" ", end=" ")
    for j in range(10 - i):
        print(j + 1, end=" ")
    for r in range(9 - i):
        print(j - r, end=" ")
    print()

#"""