#! /usr/local/bin/python3
def main():
     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
     compared = int(input())
     result = [number for number in a if number <= compared]
     print(result)
main()
