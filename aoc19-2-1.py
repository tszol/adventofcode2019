#!/usr/local/bin/python

fn = 'files/2-1.txt'

intcode = []


with open(fn) as fileobject:
    for line in fileobject:
        intcode = line.split(",")

for i in range(len(intcode)):
    intcode[i] = int(intcode[i])

intcode[1], intcode[2] = 0, 0

print(intcode)

for i in range(len(intcode)):
    if i % 4 != 0:
        continue
    elif intcode[i] == 99:
        print(f"Program stopped at position {i}")
        break
    elif intcode[i] == 1:
        intcode[intcode[i+3]] = (intcode[intcode[i+1]]
            + intcode[intcode[i+2]])
    elif intcode[i] == 2:
        intcode[intcode[i+3]] = (intcode[intcode[i+1]]
            * intcode[intcode[i+2]])
    else:
        print("Program broke!")
        break

print(intcode)

print("Done!")
