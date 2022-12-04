
import numpy

input_file = "input.txt"

# Star 1
# Summing overlapping characters
sum_of_priorities = 0

with open(input_file) as f:
    for line in f:
        rugsack = list(line)
        compartment_capacity = int(len(rugsack)/2)
        item_types = []
        for item in rugsack[:compartment_capacity]:
            if item in rugsack[compartment_capacity:]:
                item_types.append(item)
        
        #Remove duplicates from item_types
        item_types = list(dict.fromkeys(item_types))

        #Sum
        for duplicate_item in item_types:
            priority = ord(duplicate_item) - 96  #Ascii-number of char, offset to a=1, b=2 etc.
            if priority < 0 :  #If the initial correction gives a negative number, letter is upper case.
                priority += 31+27  #If upper case, add correction so A=27, B=28 etc.
            sum_of_priorities += priority

print(f"Star 1: The sum of priorities of all duplicated: {sum_of_priorities}")

# Star 2
# Checking what each set of three elves have in common.

sum_of_priorities = 0

group_counter = 0
rugsacks = []

# with open as f
with open(input_file) as f:
    for line in f:
        rugsacks.append(list(line))

for n in range(int(len(rugsacks)/3)):
    elf0 = n*3-3
    elf1 = n*3-2
    elf2 = n*3-1

    item_types = []
    for item in rugsacks[elf0]:
        if item in rugsacks[elf1]:
            if item in rugsacks[elf2]:
                item_types.append(item)

    # Remove duplicates
    item_types = list(dict.fromkeys(item_types))

    # Remove newline-char
    if '\n' in item_types:
        item_types.remove('\n')

    # Sum the duuplicated items.
    for duplicates in item_types:
        priority = ord(duplicates) - 96
        if priority < 0 :
            priority += 31 + 27
        sum_of_priorities += priority

print(f"Star 2: Sum of the common items the elves carry: {sum_of_priorities}")
