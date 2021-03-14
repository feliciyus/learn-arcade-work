import random


def main():

    print("""
Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and outrun the natives.
    """)

    km_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_travelled = -20
    drinks_left = 3
    oasis = 1
    done = False

    while not done:
        print("""
A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop for the night.
E. Status check.
Q. Quit.
        """)

        choice = input("What is your choice? ")

        if choice.upper() == "Q":
            print("\nQuitting the game...")
            done = True

        elif choice.upper() == "E":
            print("\nStatus:")
            print("You have travelled " + str(km_traveled) + " kilometers.")
            print("You have " + str(drinks_left) + " drinks left.")
            distance_between = km_traveled - natives_travelled
            print("The natives are " + str(distance_between) + " kilometers away.")

        elif choice.upper() == "D":
            camel_tiredness = 0
            print("\nThe camel is well rested and happy.")
            natives_travelled += random.randrange(7, 15)
            distance_between = km_traveled - natives_travelled
            print("But the natives are catching up! They are " + str(distance_between) + " kilometers away.")

        elif choice.upper() == "C":
            full_speed_km = random.randrange(10, 21)
            km_traveled += full_speed_km
            print("\nYou have travelled " + str(full_speed_km) + " kilometers. " + str(km_traveled) + " in total.")
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            natives_travelled += random.randrange(7, 15)
            if random.randrange(1, 21) == oasis:
                print("\nYou found an oasis! Your camel rest, you refill water and drink some..")
                thirst = 0
                camel_tiredness = 0
                drinks_left = 3

        elif choice.upper() == "B":
            moderate_speed_km = random.randrange(5, 13)
            km_traveled += moderate_speed_km
            print("\nYou have travelled " + str(moderate_speed_km) + " kilometers. " + str(km_traveled) + " in total.")
            thirst += 1
            camel_tiredness += 1
            natives_travelled += random.randrange(7, 15)
            if random.randrange(1, 21) == oasis:
                print("\nYou found an oasis! Your camel rest, you refill water and drink some..")
                thirst = 0
                camel_tiredness = 0
                drinks_left = 3

        elif choice.upper() == "A":
            if drinks_left > 0:
                drinks_left -= 1
                thirst = 0
                print("\nYou drink some water.")
            else:
                print("\nYou don't have any drinks left...")

        if km_traveled > 199:
            print("You won, you outrun the natives!")
            print("Good game!")
            break

        if km_traveled - natives_travelled < 0:
            print("The natives have caught you!")
            print("Game over!")
            break

        elif km_traveled - natives_travelled < 15:
            print("The natives are getting close!")

        if thirst > 6:
            print("You died of thirst!")
            print("Game over..")
            done = True

        elif thirst > 4 and not done:
            print("You are thirsty!")

        if camel_tiredness > 8 and not done:
            print("Your camel is dead!")
            print("Game over..")
            done = True

        elif camel_tiredness > 5 and not done:
            print("Your camel is getting tired!")


main()
