import os

with open('input.txt', 'r') as f:
    read_data = f.readlines()
    valSet = set()
    sum = 0
    setHasValue = False
    loopsThroughInput = 0
    while setHasValue is False:
        for line in read_data:
            intVal = int(line)
            sum = sum + intVal
            if sum in valSet:
                setHasValue = True
                print("Repeat value is " + str(sum))
                break
            valSet.add(sum)
        loopsThroughInput = loopsThroughInput + 1
    print(loopsThroughInput)