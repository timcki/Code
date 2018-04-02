with open('scratch') as i_file:
    for line in i_file:
        for number in line.split():
            print(number, end=' ')
