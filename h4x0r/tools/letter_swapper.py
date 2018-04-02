from termcolor import colored

class LetterSwapper:
    
    def __init__(self, folder_name):
        self.swap_letters = {}
        self.foler_name = foler_name

    
    def add_letter(self, letter_to_swap):
            self.swap_letters[letter] = letter

    def swap(self, x):
        try:
            return colored( self.swap_letters[x], 'yellow' )
        else:
            return colored( x, 'cyan' )

    def swap_text(self):
        try:
            with open(self.foler_name) as fil:
                lines = fil.read()
                for x in lines:
                    print(swap(x), end='')
        except:
            print('Cant read file')
