def print_hello():
    """ Prints hello """
    print("Hello!")


def print_goodbye():
    print("Bye!")


def main():
    print_hello()
    print_goodbye()


def print_number(my_number):
    print(my_number)


def add_numbers(a, b):
    print(a + b)

def sum_two_numbers(a, b):
    result = a + b
    return result


my_result = sum_two_numbers(22, 15)
print(my_result)


def volume_cylinder(radius, height):
    """ Returns volume of a cylinder given radius, height. """
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume


six_pack_volume = volume_cylinder(2.5, 5) * 6


def calculate_average(a, b):
    """ Calculate an average of two numbers """
    result = (a + b) / 2
    return result


x = 45
y = 56
average = calculate_average(x, y)
print(average)


def f(x):
    x += 1
    print(x)


x = 10
f(x)
# x doesnt increase in value
print(x)


def a(x):
    print("A start, x =", x)
    b(x + 1)
    print("A end, x =", x)


def b(x):
    print("B start, x =", x)
    c(x + 1)
    print("B end, x =", x)


def c(x):
    print("C start and end, x =", x)


a(5)

def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)


x = 10
y = 20
a(y, x)


def a(x, y):
    x = x + 1
    y = y + 1
    return x
    return y


x = 10
y = 20
z = a(x, y)

print(z)

def a(x, y):
    x = x + 1
    y = y + 1
    return x, y


x = 10
y = 20
z = a(x, y)

print(z)


def a(my_data):
    print("function a, my_data =  ", my_data)
    my_data = 20
    print("function a, my_data =  ", my_data)


my_data = 10

print("global scope, my_data =", my_data)
a(my_data)
print("global scope, my_data =", my_data)

def a(my_list):
    print("function a, list =  ", my_list)
    my_list = [10, 20, 30]
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)

def a(my_list):
    print("function a, list =  ", my_list)
    my_list[0] = 1000
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)







if __name__ == "__main__":
    main()

