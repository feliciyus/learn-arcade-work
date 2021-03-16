import arcade

class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        print("Woof says", self.name)


my_dog = Dog()

my_dog.name = "Spot"
my_dog.weight = 20
my_dog.age = 3

my_dog.bark()


class Ball():
    def __init__(self):
        # --- Class Attributes ---
        # Ball position
        self.x = 0
        self.y = 0

        # Ball's vector
        self.change_x = 0
        self.change_y = 0

        # Ball size
        self.size = 10

        # Ball color
        self.color = [255, 255, 255]

    # --- Class Methods ---
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color )


the_ball = Ball()
the_ball.x = 100
the_ball.y = 100
the_ball.change_x = 2
the_ball.change_y = 1
the_ball.color = [255, 0, 0]


class Cat():
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = 0

    def meow(self):
        print("Meow, my name is " + self.name)


cat1 = Cat()

cat1.name = "Jurga"
cat1.color = "Red"
cat1.weight = 10

cat1.meow()


class Monster():
    def __init__(self, new_name, new_health):
        self.name = new_name
        self.health = new_health

    def decrease_health(self):
        self.health -= 10
        print(self.health)
        if self.health <= 0:
            print("Monster died")


monster1 = Monster("Jonas", 30)
print(monster1.health)
monster1.decrease_health()
monster1.decrease_health()
monster1.decrease_health()


class Person():
    def __init__(self):
        self.name = ""

    def report(self):
        # Basic report
        print("Report for", self.name)


class Employee(Person):
    def __init__(self):
        # Call the parent/super class constructor first
        super().__init__()

        # Now set up our variables
        self.job_title = ""

    def report(self):
        # Here we override report and just do this:
        print("Employee report for", self.name)


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.email = ""

    def report(self):
        # Run the parent report:
        super().report()
        # Now add our own stuff to the end so we do both
        print("Customer e-mail:", self.email)


def main():
    john_smith = Person()
    john_smith.name = "John Smith"

    jane_employee = Employee()
    jane_employee.name = "Jane Employee"
    jane_employee.job_title = "Web Developer"

    bob_customer = Customer()
    bob_customer.name = "Bob Customer"
    bob_customer.email = "send_me@spam.com"

    john_smith.report()
    jane_employee.report()
    bob_customer.report()


main()


# Example of an instance variable
class ClassA():
    def __init__(self):
        self.y = 3

# Example of a static variable
class ClassB():
    x = 7


def main2():
    # Create class instances
    a = ClassA()
    b = ClassB()

    # Two ways to print the static variable.
    # The second way is the proper way to do it.
    print(b.x)
    print(ClassB.x)

    # One way to print an instance variable.
    # The second generates an error, because we don't know what instance
    # to reference.
    print(a.y)
    print(ClassA.y)


main2()