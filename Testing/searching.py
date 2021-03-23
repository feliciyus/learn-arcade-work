import random


def read_in_file(file_name):
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open(file_name)

    # Create an empty list to store our names
    name_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        line = line.strip()

        # print(line)

        # Add the name to the list
        name_list.append(line)

    my_file.close()

    return name_list


def linear_search(key, name_list):
    # Start at the beginning of the list
    current_list_position = 0

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the key
    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        # Advance to the next item in the list
        current_list_position += 1

    return current_list_position


def check_if_one_item_has_property(my_list, key):
    for item in my_list:
        if item == key:
            # Found an item that matched. Return True
            return True

        # Went through the whole list. Return False.
    return False


def check_if_all_items_have_property(my_list, key):
    """
    Return true if at ALL items have a property.
    """
    for item in my_list:
        if item != key:
            # Found an item that didn't match. Return False.
            return False

    # Got through the entire list. There were no mis-matches.
    return True


def get_matching_items(my_list, key):
    """
    Build a brand new list that holds all the items
    that match our property.
    """
    matching_list = []
    for item in my_list:
        if item == key:
            matching_list.append(item)
    return matching_list


def create_list(list_size):
    """ Create a list of random numbers """
    my_list = []

    for i in range(list_size):
        my_list.append(random.randrange(50))

    return my_list


def main():
    key = "MF DOOM"
    name_list = read_in_file("super_villains.txt")
    list_position = linear_search(key, name_list)
    if list_position < len(name_list):
        print("The name is at position", list_position)
    else:
        print("The name was not in the list.")

    sar = create_list(50)
    print(sar)

    key = 0
    result = check_if_one_item_has_property(sar, key)
    if result:
        print("atleast one item in the list is", key)
    else:
        print("No item in the list is", key)

    matching_list = get_matching_items(sar, key)
    print("Matching items:", matching_list)

    result = check_if_all_items_have_property(sar, key)
    print("All items in random list matching?", result)

    other_sar = [0, 0, 0, 0, 0]
    result = check_if_all_items_have_property(other_sar, key)
    print("All items in other list matching?", result)

    key = "Morgiana the Shrew"
    lower_bound = 0
    upper_bound = len(name_list) - 1
    found = False

    # Loop until we find the item, or our upper/lower bounds meet
    while lower_bound <= upper_bound and not found:

        # Find the middle position
        middle_pos = (lower_bound + upper_bound) // 2

        # Figure out if we:
        # move up the lower bound, or
        # move down the upper bound, or
        # we found what we are looking for
        if name_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif name_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        print("The name is at position", middle_pos)
    else:
        print("The name was not in the list.")


main()
