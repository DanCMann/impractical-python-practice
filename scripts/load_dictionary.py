"""Opens txt file and returns lower case words as a list.

Args:
    file (str): pathway of txt file

Returns:
    list: All of the words in lower case.

Requires-import sys
"""
import sys 

def load(file):
    """Opens txt file and returns lower case words as a list."""
    try:
        with open(file) as f:
            words = f.read().strip().split('\n')
            words = [word.lower() for word in words]
            return words
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file = sys.stderr)
        sys.exit(1)
