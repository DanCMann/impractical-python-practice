''' Chapter 2: Finding Palingram Spells
    Date: 2021-10-16
    Task: "Use python to search an English language dictionary file for two word palingrams.
            Analyze and optimize the palingram code using the cProfile tool."
'''
import load_dictionary

def find_palingrams(wordlist):

    palingrams = []

    for word in wordlist:

        for i in range(len(word)):
            splice = word[i::-1]
            revsplice = word[i:][::-1]

            if splice in wordlist:
                palin = word + splice
                if palin == palin[::-1]:
                    palingrams.append(word + " " + splice)

            if revsplice in wordlist:
                palin = revsplice + word
                if palin == palin[::-1]:
                    palingrams.append(revsplice + " " + word)

    return palingrams

if __name__ == '__main__':

    file = "data/2of4brif.txt"
    words = load_dictionary.load(file)
    palingrams = find_palingrams(words)
