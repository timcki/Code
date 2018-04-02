from regex_handler import RegexHandlerFromFile, RegexHandlerFromInput
import argparse
from sys import stdin

global path
global regex
global input_t


def startup_handler():
    global path
    global regex
    global input_t

    parser = argparse.ArgumentParser(description='Grep like program to search files or text for keywords using regexes')
    exclusive = parser.add_mutually_exclusive_group()
    exclusive.add_argument('-p', '--path', help='Path to file to be searched.')
    exclusive.add_argument('-i', '--input', help='Choose to enter input manually instead of a file', action='store_true')
    parser.add_argument('-r', '--regex', help='Define the regular expression.')
    args = parser.parse_args()

    regex = args.regex
    path = args.path
    input_t = args.input


def main():
    startup_handler()

    if not input_t:
        handler = RegexHandlerFromFile(path, regex)
        handler.print_finds()
    else:
        text = ''
        for line in stdin:
            text += line
        handler = RegexHandlerFromInput(text, regex)
        handler.print_finds()

if __name__ == '__main__':
    main()
