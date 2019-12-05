#!/usr/local/bin/python

from time import time

fn = 'files/3-1.txt'

def read_and_split_file_lines(filename):
    """Splits input into lines"""
    with open(filename) as f:
        lines = f.readlines()

    split_lines = [line.strip() for line in lines]

    vectors_1 = split_lines[0].split(',')
    vectors_2 = split_lines[1].split(',')

    return vectors_1, vectors_2

def read_directives(list):
    """Separates vector into direction and distance stored in tuple"""
    directives = []

    for vector in list:
        direction = vector[0].lower()
        distance = int(vector[1:])
        directives.append([direction, distance])

    return directives

def perform_directives(dir_list):
    """Runs the directive from list of tuples"""
    position = [0,0]
    position_list = []
    for directive in dir_list:
        if directive[0] == 'r':
            for i in range(directive[1]):
                position = (position[0], position[1] + 1)
                position_list.append(position)
        elif directive[0] == 'l':
            for i in range(directive[1]):
                position = (position[0], position[1] - 1)
                position_list.append(position)
        elif directive[0] == 'u':
            for i in range(directive[1]):
                position = (position[0] + 1, position[1])
                position_list.append(position)
        else:
            for i in range(directive[1]):
                position = (position[0] - 1, position[1])
                position_list.append(position)
    print(f"Length of wire: {len(position_list)}")
    return position_list

def test_for_equivalents(positions_1, positions_2):
    shared_positions = []
    spos_index_1 = []
    spos_index_2 = []
    for position in positions_1:
        if position in positions_2:
            shared_positions.append(position)
            spos_index_1.append(positions_1.index(position))
            spos_index_2.append(positions_2.index(position))
    return shared_positions, spos_index_1, spos_index_2

def find_shortest_distance(shared_list):
    shortest = False
    for position in shared_list:
        distance = abs(position[0]) + abs(position[1])
        if not shortest or abs(distance) < shortest:
            shortest = abs(distance)
    return shortest

def find_earliest_shared(ind1, ind2):
    sum_ind = []
    for i in range(len(ind1)):
        sum_ind.append(ind1[i] + ind2[i])
    print(min(sum_ind)+2)

start = time()
dir_1, dir_2 = read_and_split_file_lines(fn)
directives_1 = read_directives(dir_1)
directives_2 = read_directives(dir_2)
pos1 = perform_directives(directives_1)
pos2 = perform_directives(directives_2)
shared, sind_1, sind_2 = test_for_equivalents(pos1, pos2)
shortest = find_shortest_distance(shared)
print(shortest)
find_earliest_shared(sind_1, sind_2)
end = time()
print(f"Time: {end - start}")


"""
file_lines = read_and_split_file_lines(fn)
vectors_1 = write_line_to_list(file_lines[0])
vectors_2 = write_line_to_list(file_lines[1])
"""
