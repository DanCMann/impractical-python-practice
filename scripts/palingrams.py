''' Chapter 2: Finding Palingram Spells
    Date: 2021-10-16
    Task: "Use python to search an English language dictionary file for two word palingrams.
            Analyze and optimize the palingram code using the cProfile tool."
'''
import load_dictionary

def find_palingrams(wordlist):

    palingrams = []
    palin_list = []

    count = 0
    for word in wordlist:

        if count % 500 == 0:
            print("MY LIST: {}\nBOOK LIST: {}\n\n".format(palingrams, palin_list))
            print("MY LIST: {}\nBOOK LIST: {}".format(len(palingrams), len(palin_list)))

        count += 1

        end = len(word)
        rev_word = word[::-1]

        for i in range(end):
            if word[i:] == rev_word[:end-i] and rev_word[end-i:] in wordlist: 
                palin_list.append((word, rev_word[end-i:]))
            if word[:i] == rev_word[end-i:] and rev_word[:end-i] in wordlist:
                palin_list.append((rev_word[:end-i], word))

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
