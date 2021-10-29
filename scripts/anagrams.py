''' Chapter 3: Solving Anagrams 
    Date: 2021-10-17
    Task: "Use Python and a dictionary file to find all the single-word anagrams for a given English word or a name."
'''

import load_dictionary

def find_anagrams(target_word, wordset):
    anagrams = []
    letters = sorted(list(target_word))
    anagrams = [word for word in wordset if sorted(list(word)) == letters]

    return anagrams

def game(words):

    running = True

    while running:
        response = input("Please enter a word to find all anagrams (enter n to quit): " )
        response = response.lower()
        if response == 'n':
            print("quitting anagrams...")
            running = False
        else:
            anagrams = find_anagrams(response, words)
            print("The anagrams for {} are:\n".format(response))
            print(*anagrams, sep = '\n')
            print("\n")


def main():
    file = "data/2of4brif.txt"
    wordlist = load_dictionary.load(file)
    words = set(wordlist)
    game(words)

if __name__ == '__main__':
    main()