''' Chapter 2: Finding Palingram Spells
    Date: 2021-10-16
    Task: "Use python to search an English language dictionary file for palindromes."
'''
import load_dictionary

if __name__ == '__main__':

    file = 'data/2of4brif.txt'
    words = load_dictionary.load(file)
    palin = [word for word in words if(word == word[::-1])]
    print(*palin, sep="\n")