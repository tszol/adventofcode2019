#!/usr/local/bin/python

fn = 'files/1-1.txt'

def calculate_initial_fuel(filename):
    """Calculate fuel based on file contents"""
    initial_fuel_req = 0
    with open(filename) as file_object:
        for line in file_object:
            mass = int(line.strip())
            fuel_req = int(mass / 3) - 2
            initial_fuel_req += fuel_req
    return initial_fuel_req

def calculate_total_fuel(filename):
    """Calculate fuel based on file contents"""
    total_fuel_req = 0
    with open(filename) as file_object:
        for line in file_object:
            mass = int(line.strip())
            init_fuel_req = int(mass / 3) - 2
            supp_fuel_req = calculate_supplemental_fuel(init_fuel_req)
            unit_fuel = init_fuel_req + supp_fuel_req
            total_fuel_req += unit_fuel
    return total_fuel_req

i_fuel = calculate_initial_fuel(fn)
print(i_fuel)
t_fuel = calculate_total_fuel(fn)
print(t_fuel)
