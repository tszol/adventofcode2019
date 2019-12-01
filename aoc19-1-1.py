#!/usr/local/bin/python

fn = 'files/1-1.txt'

tot_fuel_req = 0

with open(fn) as file_object:
    for line in file_object:
        mass = int(line.strip())
        fuel_req = (int(mass / 3)) - 2
        tot_fuel_req += fuel_req

print(tot_fuel_req)
