''' Chapter 2: Finding Palingram Spells
    Date: 2021-10-16
    Task: "Use python to search an English language dictionary file for two word palingrams.
            Analyze and optimize the palingram code using the cProfile tool."
'''
import load_dictionary

def find_palingrams(words):

    palingrams = []

    for word in words:

        end = len(word)
        rev_word = word[::-1]

        # In the original way that I did it, it did more checks.
        #  e.g., if you just searched 'grits' it would find 'stir'.
        #  But that seemed to be overkill, since 'stir' will find 'grits'.
        for i in range(end):
            if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words: 
                palingrams.append((word, rev_word[end-i:]))
            if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                palingrams.append((rev_word[:end-i], word))

    return palingrams

def main():
    file = "data/2of4brif.txt"
    wordlist = load_dictionary.load(file)
    words = set(wordlist)
    palingrams = find_palingrams(words)
    print(palingrams)


if __name__ == '__main__':
    main()