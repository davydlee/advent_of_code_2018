import os

with open('input.txt', 'r') as f:
    read_data = f.readlines()
    sum = 0
    for line in read_data:
        #print(line)
        sum += int(line)
    print("The sum is " + str(sum))