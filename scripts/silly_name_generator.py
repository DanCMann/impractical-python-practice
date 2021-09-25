# Chapter 1: Silly Name Generator
# Date: 2021-09-20
# Author: Dan C. Mann
# Task: "[W]rite a simple Python program that generates nutty names by randomly combining first names and surnames."
import random

def main():
    """Sets up game.
    """
    vornamen = 'data/first_names.txt'
    nachnamen = 'data/last_names.txt'
    NameGame(vornamen, nachnamen)

def get_names(fname):
    """Opens a text file, splits line by commas, and returns a list of strings.

    Args:
        fname (string): Path to txt file.

    Returns:
        list: List of comma separated strings.
    """

    with open(fname) as file:
        lines = file.readline()

    names = lines.split(',')

    return names

def create_random_name(first_names, last_names):
    """Generates a random name from lists of first and last names.

    Args:
        first_names (list): list of strings used for first names.
        last_names (list): list of strings used for last names.

    Returns:
        string: A full name.
    """

    # Randomly select first name and assign to variable

    index = random.randint(0, len(first_names))
    first_name = first_names[index]


    # Randomly select last name

    index = random.randint(0, len(last_names))
    last_name = last_names[index]

    return first_name + " " + last_name

class NameGame():
    """Game that creates random names from text files containing first and last names.
    """
    def __init__(self, first_name_file, last_name_file):

        self.first_names = get_names(first_name_file)
        self.last_names = get_names(last_name_file)

        running = True

        while running:
            response = input("Do you want a silly name?: Y/N ")
            if response.lower() == 'y':
                self.name = create_random_name(self.first_names, self.last_names)
                print("Your Name is \n\t{}\n".format(self.name))
            else:
                print("OK, ending game")
                running = False


if __name__ == '__main__':
    main()
