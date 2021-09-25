# Pig Latin
# Date: 2021-09-25
# Task: "Write a program that takes a word as input and uses indexing
#   and slicing to return its Pig Latin equivalent."

def main():
    """ Main function for running pig latin game.
    """

    pig_latin_game()

def pig_latin_game():
    """ Turns the pig_latin function into a game.
    """
    print("Translate into IgPay AtinLay!!\n")

    string_input = input("What word do you want translated? ")

    running = True

    while running:

        print("\t{}".format(pig_latin(string_input)))

        string_input = input("Enter another word to keep playing? ('n' to end game) ")

        if string_input.lower() == 'n':
            running = False
            print("Ending game..")


def pig_latin(string):
    """ Translates an English word into Pig Latin.
          Takes all consonants before the first vowel then moves them to the end of the string,
          then adds -ay to the end.

    Args:
        string (str): String to be converted into Pig Latin.

    Returns:
        str: Pig Latin conversion of string.
    """

    vowels = ["a", "e", "i", "o", "u"]

    string = string.lower()

    count = 0

    for letter in string:

        if letter in vowels:
            pig = string[:count] + 'ay'

            break
        if letter == 'y' and count != 0:
            pig = string[:count] + 'ay'

            break

        count += 1

    return string[count:] + pig

if __name__ == '__main__':

    main()
