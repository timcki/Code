#! /usr/local/bin/python3
# import argparse
from weather import weather
from changes import changes


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('echo')
    # args = parser.parse_args()
    # print(args.echo)
    zmiany = changes.Changes()
    zmiany.fetch_changes()


if __name__ == '__main__':
    main()
