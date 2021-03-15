class Room:
    def __init__(self, description, north, east, south, west, up, down):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down


def main():
    room_list = []

    # Bedroom
    room = Room("""
You are in the messy bedroom you woke up in.
There is door to the east, leading to dark hall...""",
                None, 1, None, None, None, None)
    room_list.append(room)

    # Hall 1
    room = Room("""
You are in a dark hall. To the west - bedroom where you started
To the north the hall continues, to the east - door to get outside!""",
                3, None, None, 0, None, None)
    room_list.append(room)

    # Dining Room
    room = Room("""
You are in a dining room. Only some leftover food here.. To the east - long hallway""",
                None, 3, None, None, None, None)
    room_list.append(room)

    # Hall 2
    room = Room("""
You are in a long hall. To the west - dining room, south the hall continues,
To the north you see room with stairs""",
                4, None, 1, 2, None, None)
    room_list.append(room)

    # Stair room
    room = Room("""
You are in a room with stairs which goes up. You can go up
or to the south - long hallway""",
                None, None, 3, None, 5, None)
    room_list.append(room)

    # Stair room 2
    room = Room("""
You are in a room with stairs which goes down. You can go down
or to the south - hallway""",
                None, None, 7, None, None, 4)
    room_list.append(room)

    # Dark room
    room = Room("""
You are in a dark room and can't see anything. You need to find a light source.
East is back to hallway""",
                None, 7, None, None, None, None)
    room_list.append(room)

    # Hall 3
    room = Room("""
You are in a hallway, west - dark room, north - room with stairs that goes down,
south - continue the hallway""",
                5, None, 9, 6, None, None)
    room_list.append(room)

    # Bedroom 2
    room = Room("""
You are in a bedroom, you see a lantern in the north of the room on a table.
east - to the hallway""",
                None, 9, None, None, None, None)
    room_list.append(room)

    # Hall 4
    room = Room("""
You are in a hallway, north - continue the hallway,
west - bedroom""",
                7, None, None, 8, None, None)
    room_list.append(room)

    current_room = 0
    done = False
    keys = False
    lantern = False

    # Description and start of the game
    print("""ESCAPE ROOM
You wake up in a mysterious house and you need to escape it to win!
Controls - (n - north, s - south, e - east, w - west, up, down, q - to quit)""")

    while not done:
        print(room_list[current_room].description)
        print()
        direction = input("Which direction u go? ")

        # --Game mechanics--

        # Picking up lantern and changing description of current room
        # Changing description of dark room because we picked up a lantern
        if direction.lower() == "n" and current_room == 8:
            if lantern is False:
                print()
                print("You pick up the lantern, you might be able to see something in the dark.")
                lantern = True
                room_list[8].description = """
You are in a bedroom, you see a table to the north where the lantern was.
east - to the hallway"""
                room_list[6].description = """
Finally you can see in this room because of the lantern. There is a chest to the west,
East is back to hallway"""

            # Not letting to pick up lantern twice
            elif lantern is True:
                print()
                print("There is nothing on the table, you already picked up the lantern.")
            continue

        # Picking up keys and changing description of the current room
        if direction.lower() == "w" and current_room == 6 and lantern is True:
            if keys is False:
                print()
                print("You find keys in the chest, you might be able to get out of here!")
                keys = True
                room_list[6].description = """
There is empty chest to the west, east - to the hallway"""

            # Not letting to pick up keys twice
            elif keys is True:
                print()
                print("You already picked up the keys from the chest, it's empty..")
            continue

        # Trying to enter the door or winning the game
        if direction.lower() == "e" and current_room == 1:
            if keys is True:
                print("""
You try the keys and they fit the lock on the door!
You manage to escape, victory!!!""")
                break

            if keys is False:
                print()
                print("""The door seems locked, maybe you could find a key somewhere?""")
                room_list[1].description = """
You are in a dark hall. To the west - bedroom where you started
To the north the hall continues, to the east - door, but it's locked.."""
            continue

        # --Directions--

        # North
        if direction.lower() == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("You can't go that way..")
            else:
                current_room = next_room

        # South
        elif direction.lower() == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You can't go that way..")
            else:
                current_room = next_room

        # West
        elif direction.lower() == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You can't go that way..")
            else:
                current_room = next_room

        # East
        elif direction.lower() == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You can't go that way..")
            else:
                current_room = next_room

        # Up
        elif direction.lower() == "up":
            next_room = room_list[current_room].up
            if next_room is None:
                print()
                print("There is no stairs leading up..")
            else:
                current_room = next_room

        # Down
        elif direction.lower() == "down":
            next_room = room_list[current_room].down
            if next_room is None:
                print()
                print("There is no stairs leading down..")
            else:
                current_room = next_room

        # Quit the game
        elif direction.lower() == "q":
            print()
            print("Quitting the game.")
            break

        # Invalid direction
        else:
            print("I don't understand this direction. :(")


main()
