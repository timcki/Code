#! /usr/local/bin/python3
count = 1
maxim = 0
a = input()
for char in a:
    if char not in 'AEIOU':
        count += 1
    else:
        maxim = count
        count = 2

print(count)
