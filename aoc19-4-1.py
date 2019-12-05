#!/usr/local/bin/python

low = 156666
high = 600000

split_numbers = []
passwords = []

for i in range(low, high + 1):
    split_numbers.append(str(i))

def is_ascending(list):
    previous = list[0]
    for number in list:
        if number < previous:
            return False
        previous = number
    return True

def has_double(list):
    previous = 0
    for number in list:
        if number == previous and list.count(number) == 2:
            return True
        previous = number
    return False

for number in split_numbers:
    if is_ascending(number) and has_double(number):
        passwords.append(number)

print(len(passwords))
