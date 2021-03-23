import re


def binary_search(key, name_list):
    """ Binary search """
    lower_bound = 0
    upper_bound = len(name_list) - 1
    found = False

    # Loop until we find the item, or our upper/lower bounds meet
    while lower_bound <= upper_bound and not found:
        # Find middle pos
        middle_pos = (lower_bound + upper_bound) // 2
        # Figure out if we:
        # move up the lower bound, or
        # move down the upper bound, or
        # we found what we are looking for
        if name_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        elif name_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        else:
            found = True

    return found


def linear_search(key, name_list):
    """ Linear search """

    # Start at the beginning of the list
    current_list_position = 0
    found = False
    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the key
    while current_list_position < len(name_list) and not found:
        # Check if key matches current word in dictionary
        if name_list[current_list_position] == key:
            found = True
        # Advance to the next item in the list
        current_list_position += 1

    return found


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


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


def main():
    # Getting two documents to compare
    dictionary_list = read_in_file("dictionary.txt")
    alice_file = open("AliceInWonderLand200.txt")

    print("--- Linear Search ---")
    line_number = 1
    for i in alice_file:
        word_list = split_line(i)
        for j in word_list:
            if not linear_search(j.upper(), dictionary_list):
                print("Line", line_number, "possible misspelled word:", j)
        line_number += 1

    alice_file.close()
    alice_file = open("AliceInWonderLand200.txt")
    print("--- Binary Search ---")
    line_number = 1
    for i in alice_file:
        word_list = split_line(i)
        for j in word_list:
            if not binary_search(j.upper(), dictionary_list):
                print("Line", line_number, "possible misspelled word:", j)
        line_number += 1

    alice_file.close()


main()
