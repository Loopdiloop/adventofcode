
import sys
import yaml
from yaml.loader import SafeLoader

import utils

with open("input.yaml") as f:
    data = yaml.load(f, Loader=SafeLoader)

"""
Change in input data(!)
To run this script, a small change must be done to the input-file.
An additional line with "Result:" must be added 
before the If true/false statements to be a valid .yaml.
Use "change all occurances" in your editor.

Example:

Monkey 0:
  Starting items: 66, 59, 64, 51
  Operation: new = old * 3
  Test: divisible by 2
  Result:  
    If true: throw to monkey 1
    If false: throw to monkey 4

"""

inspections = dict()
smallest_common_denominator = 1
monkies = dict()

# Star 1 vs. star 2
try:
    s = int(sys.argv[1])
except:
    s = 1

rounds = [20, 10000]

for monky in data.keys():

    inspections[monky] = 0
    monkies[monky]= dict()

    # Fill inventory dict with lists of inventory
    starting_inventory_int = []
    starting_inventory = data[monky]["Starting items"]
    starting_inventory = str(starting_inventory).strip(" ")
    if "," in list(str(starting_inventory)):
        starting_inventory = starting_inventory.split(",")
        for i in range(len(starting_inventory)):
            starting_inventory_int.append(int(starting_inventory[i]))
    else:
        starting_inventory_int = [int(starting_inventory)]
    monkies[monky]["inventory"] = starting_inventory_int

    monkies[monky]["Operation"] = str(data[monky]["Operation"]).split(" ")

    monkies[monky]["Test"] = str(data[monky]["Test"]).split(" ")

    monkies[monky]["If true"] = str(data[monky]["Result"]["If true"]).split(" ")
    monkies[monky]["If false"] = str(data[monky]["Result"]["If false"]).split(" ")

    smallest_common_denominator *= int(monkies[monky]["Test"][2])




truefalse_key = ["If false", "If true"]
for R in range(rounds[s-1]):
    for M in monkies.keys():
        for I in monkies[M]["inventory"]:
            # Monkey inspects item I
            inspections[M] += 1
            # Update worry level for I
            I = utils.do_operation(monkies[M]["Operation"], I)
            # Drop in worry after inspection
            if s == 1: # Star 1
                I = int(I/3)
            else: 
                assert s == 2 # Star 2
                I = I%smallest_common_denominator
            testresult = utils.do_test(monkies[M]["Test"], I)
            # Find number of monkey to throw to.
            throw_to = monkies[M][truefalse_key[int(testresult)]][3]
            monkies["Monkey "+throw_to]["inventory"].append(I)

        monkies[M]["inventory"] = []
    print(f"{R} / 10 000")

inspected = []
for j in inspections.keys():
    print(f"{j} inspected {inspections[j]} times.")
    inspected.append(int(inspections[j]))

inspected.sort()
a = inspected[-1]
b = inspected[-2]
print(inspected, a*b)

