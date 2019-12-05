#!/usr/local/bin/python

fn = 'files/5-1.txt'

def read_and_parse(file):
    """Reads file line-by-line then converts items to integers"""
    split_file = []
    with open(file) as fileobject:
        for line in fileobject:
            split_file = line.split(",")
    for i in range(len(split_file)):
        split_file[i] = int(split_file[i])
    return split_file

def find_opcode_inputs(series, index, instruction):
    """Sets input indices based on paramters of instruction"""
    if instruction[2] == 0:  # If 1st param is "position"
        input_1 = series[series[index+1]]
    else:  #1st param is "immediate"
        input_1 = series[index+1]
    if instruction[1] == 0:  # If 2nd param is "position"
        input_2 = series[series[index+2]]
    else:  #2nd param is "immediate"
        input_2 = series[index+2]
    return input_1, input_2

def opcode_1(series, index, instruction):
    """Adds numbers in appropriate cell indices"""
    input_1, input_2 = find_opcode_inputs(series, index, instruction)
    series[series[index+3]] = (int(input_1)
                            + int(input_2)) # 3rd param is always 0

def opcode_2(series, index, instruction):
    """Multiplies numbers in appropriate cell indices"""
    input_1, input_2 = find_opcode_inputs(series, index, instruction)
    series[series[index+3]] = input_1 * input_2 # 3rd param is always 0

def opcode_3(series, index):
    """Takes an input and stores it at an index"""
    number = input("What is the input? ")
    series[series[index+1]] = number

def opcode_4(series, index):
    """Outputs the value at an index"""
    output = series[series[index+1]]
    print(f"Output from index {index}: {output}")

def opcode_5(series, index):
    """Pass"""
    pass

def opcode_6(series, index):
    """Pass"""
    pass

def opcode_7(series, index):
    """Pass"""
    pass

def opcode_8(series, index):
    """Pass"""
    pass

def parse_instruction(instruction):
    """Reads opcode instruction and parses into units, reversed"""
    instruction = str(instruction)
    parsed_instruction = []
    for i in instruction[:]:
        parsed_instruction.append(int(i))
    while len(parsed_instruction) != 5:
        parsed_instruction.insert(0, 0)
    return parsed_instruction

def run_intcode(intcode):
    intcode_running, i = True, 0
    while intcode_running:
        instruction = parse_instruction(intcode[i])
        if instruction[-1] == 9 and instruction[-2] == 9:
            intcode_running = False
        elif instruction[-1] == 1 and instruction[-2] == 0:
            opcode_1(intcode, i, instruction)
            i += 4
        elif instruction[-1] == 2 and instruction[-2] == 0:
            opcode_2(intcode, i, instruction)
            i += 4
        elif instruction[-1] == 3 and instruction[-2] == 0:
            opcode_3(intcode, i)
            i += 2
        elif instruction[-1] == 4 and instruction[-2] == 0:
            opcode_4(intcode, i)
            i += 2
        elif instruction[-1] == 5 and instruction[-2] == 0:
            opcode_5(intcode, i)
            i += 4
        elif instruction[-1] == 6 and instruction[-2] == 0:
            opcode_6(intcode, i)
            i += 4
        elif instruction[-1] == 7 and instruction[-2] == 0:
            opcode_7(intcode, i)
            i += 4
        elif instruction[-1] == 8 and instruction[-2] == 0:
            opcode_8(intcode, i)
            i += 4
        else:
            print("Program broke!")
            break


intcode = read_and_parse(fn)
# intcode = [1101,100,-1,4,0]
run_intcode(intcode)
print(intcode[0])
#print(parse_instruction(1002))

print("Done!")
