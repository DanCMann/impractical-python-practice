'''
Chapter 3: Project 5 - Finding Phrase Anagrams
Date: 2022-04-19
Objective: Write a python program that lets a user interactively build an anagram phrase from the letters in their name

# Load a dictionary file
# Accept a name from the user
# Set limit = length of name
# Start empty list to hold anagram phrase
# while length of phrase < limit:
#   generate list of dictionary words that fit in name
#   present words to user
#   present remaining letters to user
#   present current phrase to user
#   ask user to input word or start over
#   If user input can be made from remaining letters
#       accept choice of new word or words from user
#       remove letters in choice from letters in name
#       return choice and remaining letters in name
#   If choice is not a valid selection; 
#       Ask user for new choice or let user start over
#   Add choice to phrase and show to user
#   Generate new list of words and repeat process
# When phrase length equals limit value: 
#   Display final phrase
#   Ask user to start over or exit. 
'''

from collections import Counter

# Load a dictionary file
import Dictionary

class Anagrams():
    def __init__(self, target_word):
        self.target_word = "".join(target_word).lower()
        print(self.target_word)
        self.dictionary = Dictionary.Dictionary("data/2of4brif.txt")
        self.word_set = set(self.dictionary.words)

        ws_remove = self.target_word.replace(" ", "")
        letters = sorted(list(ws_remove))
        self.list = []
        self.list = [word for word in self.word_set if sorted(list(word)) == letters]

    def print_anagrams(self):
        print("The anagrams for {} are:\n".format(self.target_word))
        print(*self.list, sep = '\n')
        print("\n")

class InputPhrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.phase_nospace = self.phrase.replace(" ", "")
        self.counter = Counter(self.phase_nospace)
        self.n_letters = self.counter.total()
        self.all_anagrams = []
        self._substring = []

    def add_anagrams(self, anagram_list):
        for anagram in anagram_list:
            if anagram not in self.all_anagrams:
                self.all_anagrams.append(anagram)

    def find_anagrams(self, all = True):
        self.anagrams = Anagrams(self.phrase)
        self.add_anagrams(self.anagrams.list)
        if all:
            self.find_partial_anagrams()

    def find_partial_anagrams(self):
        anagrams = []
        for word in self.anagrams.dictionary.words:
            test = ''
            word_letter_map = Counter(word.lower())
            for letter in word:
                if word_letter_map[letter] <= self.counter[letter]:
                    test += letter
            if Counter(test) == word_letter_map:
                self.add_anagrams([word])

    def print_all_anagrams(self):
        print(*self.all_anagrams)

class OutputPhrase():
    def __init__(self):
        self.list = []
        self.to_string()
        self.get_length()

    def to_string(self):
        self.string = ' '.join(self.list)

    def add_word(self, word):
        self.list.append(word)
        self.to_string()
        self.get_length()
    
    def get_length(self):
        ws_remove = self.string.replace(" ", "")
        self.counter = Counter(ws_remove)
        self.n_letters = self.counter.total()

class Program():
    def __init__(self):
        self.running = True
        # Start empty list to hold anagram phrase
        self.anagram_phrase = OutputPhrase()
        self.initial_phrase = InputPhrase("__init")

    def get_input(self, first = False):
        response = input("Please enter a word or phrase: ")
        if response == 'q':
            self.quit()

        if first:
            self.initial_phrase = InputPhrase(response)
        
        self.phrase = InputPhrase(response)

    def choose_word(self):
        self.phrase.print_all_anagrams()        
        selection = input("Please choose one of the words: ")
        
        if selection in self.phrase.all_anagrams:
            self.anagram_phrase.add_word(selection)
            print(self.anagram_phrase.string)
        elif selection == 'q':
            print("No choice...")
            self.quit()
        else:
            print("Selection not in list; please choose a word in the list")
            selection = self.choose_word()

    def get_remaining_chars(self):
        counter = self.anagram_phrase.counter
        self.remaining_letters = self.initial_phrase.counter - counter
        self.remaining_letters = "".join(self.remaining_letters.elements())

    def quit(self):
        self.running = False

    def main_task(self):
        # Accept a name from the user
        # This should be changed so that the leftover letters are automatically used and the user has the chance to accept or reject
        while self.anagram_phrase.n_letters < self.initial_phrase.n_letters or self.running == False:
            if self.initial_phrase.phrase == "__init":
                self.get_input(first=True)
            else:
                self.get_input()

            self.phrase.find_anagrams(all=True)
            if len(self.phrase.all_anagrams) < 1:
                print("No new anagrams found; starting over...")
                self.quit()
                break
            else:
                self.choose_word()
                self.get_remaining_chars()
                print("\nThese letters remain: {}".format(self.remaining_letters))
                print("\nCurrent phrase is: {}".format(self.anagram_phrase.string))

        print("The phrase is: {}".format(self.anagram_phrase.string))
        self.quit()

    def run(self):
        while self.running:
            self.main_task()

class Main():
    def __init__(self):
        self.running = True
        while self.running:
            anagrams = Program()
            anagrams.run()
            self.continue_program()
    
    def continue_program(self):
        cont = input("Do you want to play again? (y/n)")
        if cont.lower() == 'n':
            self.running = False
            print("Ending program...")
        elif cont.lower() != 'y':
            self.continue_program()

if __name__ == '__main__':
    Main()