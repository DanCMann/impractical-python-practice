"""Opens txt file and returns lower case words as a list.

Args:
    file (str): pathway of txt file

Returns:
    list: All of the words in lower case.

Requires-import sys
"""
import sys 

class Dictionary():
    def __init__(self, file):
        self.file = file

        """Opens txt file and returns lower case words as a list."""
        try:
            with open(self.file) as f:
                self.words = f.read().strip().split('\n')
                self.words = [word.lower() for word in self.words]

        except IOError as e:
            print("{}\nError opening {}. Terminating program.".format(e, self.file), file = sys.stderr)
            sys.exit(1)
