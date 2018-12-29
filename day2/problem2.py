import os

with open('input.txt', 'r') as f:
    read_data = f.readlines()
    input_len = len(read_data)

    for x in range(input_len):
        line_len = len(read_data[x])
        for y in range(x+1, input_len):
            diff = 0
            string_a = read_data[x]
            string_b = read_data[y]
            print("x: " + str(x))
            print("y: " + str(y))
            print("string a: " + string_a)
            print("string b: " + string_b)
            print("string length: " + str(len(string_a)))
            for i in range(line_len):
                print(i)
                if string_a[i] != string_b[i]:
                    diff += 1
            if diff == 1:
                result = find_similar_letters(string_a, string_b)
                print("answer: " + result)

def find_similar_letters(self, a, b):
    for i in range(a):
        sim = ""
        if a[i] == b[i]:
            sim +=a[i]
    return sim
