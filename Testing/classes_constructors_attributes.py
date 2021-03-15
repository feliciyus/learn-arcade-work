class Character:
    """
    This is a class that represents the player character.
    """
    def __init__(self):
        """ This is a method that sets up the variables in the object. """
        self.name = ""
        self.outfit = ""
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.armor_amount = 0
        self.max_speed = 0


class Address():
    def __init__(self, line1, line2, city, state, zip_code, country):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country


class Person():
    name: str = ""
    last_name: str = ""
    age: int = 0


class Dog():
    def __init__(self, new_name):
        """ Constructor """
        self.name = new_name
        print("A new dog is born!")


class Cat:
    population = 0

    def __init__(self, name):
        self.name = name
        Cat.population += 1


def print_address(address):
    """ Print an address to the screen """

    # If there is a line1 in the address, print it
    if len(address.line1) > 0:
        print(address.line1)
    # If there is a line2 in the address, print it
    if len(address.line2) > 0:
        print(address.line2)
    print(address.city + ", " + address.state + " " + address.zip_code)


def main():
    # Create an address
    my_address = Address("701 N. C Street",
                         "Carver Science Building",
                         "Indianapolis",
                         "IA",
                         "50125",
                         "USA")

    print_address(my_address)
    print()
    my_dog = Dog("Fluffy")
    print(my_dog.name)
    cat1 = Cat("Pat")
    cat2 = Cat("Pepper")
    cat3 = Cat("Jurga")

    print("The cat population is:", Cat.population)


main()
