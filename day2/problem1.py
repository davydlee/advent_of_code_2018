import os

with open('input.txt', 'r') as f:
    read_data = f.readlines()
    #go through each line to find checksum eligibility
    twice = 0
    thrice = 0
    for line in read_data:
        map = dict()
        for letter in line:
            map[letter] = map.get(letter, 0) + 1
            #print(letter)
        if 2 in map.values():
            twice += 1
        if 3 in map.values():
            thrice += 1
    checksum = twice * thrice
    print(checksum)