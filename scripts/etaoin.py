# Poor Man's Bar Chart
# Date: 2021-09-26
# Task: "Write a Python script that takes a sentence (string)
#       as input and returns a simple bar chart"

from string import ascii_lowercase

def main():
    """ Runs program.
    """

    chart = PoorBarChart()
    chart.print_barchart()

class PoorBarChart():
    """ Gets sum of letters in a sentence and prints a simple bar chart showing letter counts.
    """

    def __init__(self):
        """ Initializes the dictionary will all of the lowercase letters.
        """
        self.letter_dict = {}

        for letter in ascii_lowercase:

            self.letter_dict.update({letter: 0})

        self.sentence = input("Enter a sentence: ")

        for letter in self.sentence.lower():

            if letter in self.letter_dict:

                self.letter_dict[letter] += 1

    def print_barchart(self):
        """ Prints the poor man barchart.
        """
        for letter, count in self.letter_dict.items():

            print("{} : {} ".format(letter, (letter+ ' ') * count))


if __name__ == '__main__':

    main()
