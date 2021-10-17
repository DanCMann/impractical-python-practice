''' Chapter 2: Finding Palingram Spells
    Date: 2021-10-16
    Task: "Use python to search an English language dictionary file for two word palingrams.
            Analyze and optimize the palingram code using the cProfile tool."
'''
import load_dictionary

def find_palingrams(wordlist):

    palingrams = []

    for word in wordlist:

        end = len(word)
        rev_word = word[::-1]

        for i in range(end):
            if word[i:] == rev_word[:end-i] and rev_word[end-i:] in wordlist: 
                palingrams.append((word, rev_word[end-i:]))
            if word[:i] == rev_word[end-i:] and rev_word[:end-i] in wordlist:
                palingrams.append((rev_word[:end-i], word))

    return palingrams

if __name__ == '__main__':

    file = "data/2of4brif.txt"
    words = load_dictionary.load(file)
    palingrams = find_palingrams(words)
    print(palingrams)
