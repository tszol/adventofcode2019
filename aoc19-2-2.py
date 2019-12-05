#!/usr/local/bin/python

fn = 'files/2-1.txt'

intcode = []

with open(fn) as fileobject:
    for line in fileobject:
        intcode = line.split(",")

for i in range(len(intcode)):
    intcode[i] = int(intcode[i])

intcode[1], intcode[2] = 12, 2

def calculate_trajectory(code):
    series = code
    for i in range(len(series)):
        if i % 4 != 0:
            continue
        elif series[i] == 99:
            break
        elif series[i] == 1:
            series[series[i+3]] = (series[series[i+1]]
                + series[series[i+2]])
        elif intcode[i] == 2:
            series[series[i+3]] = (series[series[i+1]]
                * series[series[i+2]])
        else:
            print("Program broke!")
            break

def find_noun_verb(code):
    for i in range(1, 100):
        for j in range (1, 100):
            copy = code[:]
            copy[1] = i
            copy[2] = j
            calculate_trajectory(copy)
            if copy[0] == 19690720:
                print(f"Noun: {copy[1]}, Verb: {copy[2]}")
                print(f"Result: {100 * copy[1] + copy[2]}")
                break
            else:
                continue
    print("Search ended.")


#calculate_trajectory(intcode)
find_noun_verb(intcode)

print(intcode[0])

print("Done!")
