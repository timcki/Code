import re
from abc import ABC, abstractmethod
from termcolor import cprint, colored


class RegexHandler(ABC):

    def __init__(self, text, regex):
        self.text = text
        self.regex = regex
        self.count = 0
        self.already_changed = []

    def create_regex(self):
        try:
            return re.compile(self.regex)
        except:
            cprint('Wrong regex! Try again.', 'red')
            quit()

    @abstractmethod
    def handle_text(self):
        pass

    def print_finds(self):
        text = self.handle_text()
        print()
        if self.count == 0:
            cprint('\nNo matches!', 'red')
            print()
            quit()

        print('\n' + text + '\n')
        if self.count == 1:
            cprint('1 match found!', 'cyan')
            print()
            quit()

        cprint('{} matches found!'.format(self.count), 'cyan')


class RegexHandlerFromFile(RegexHandler):

    def __open_file(self):
        try:
            with open(self.text) as file:
                return file.read()
        except:
            cprint('Wrong path! Try again.', 'red')
            quit()

    def handle_text(self):

        file_text = self.__open_file()
        r = self.create_regex()

        for match in r.finditer(file_text):
            self.count += 1
            checking_now = match.group()

            if checking_now in self.already_changed:
                continue

            a = colored(checking_now, 'green')
            file_text = file_text.replace(checking_now, a)
            self.already_changed.append(checking_now)

        print(self.count)
        return file_text


class RegexHandlerFromInput(RegexHandler):

    def __get_text(self):
        try:
            t = self.text
            return t
        except:
            cprint('Wrong input!', 'red')
            quit()

    def handle_text(self):
        text = self.__get_text()
        r = self.create_regex()

        for match in r.finditer(text):
            self.count += 1
            checking_now = match.group()

            if checking_now in self.already_changed:
                continue

            a = colored(checking_now, 'green')
            text = text.replace(checking_now, a)
            self.already_changed.append(checking_now)

        return text
