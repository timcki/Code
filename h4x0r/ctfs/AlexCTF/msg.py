with open('msg') as f:
    one_time = f.readlines()

for line,number in zip(one_time, range(0, 10)):
    for x in range(0, len(one_time[number:]), 2):
        num = int(one_time[number][x:x+2], 16)
        print(num)

