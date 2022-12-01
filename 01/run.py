
# A little cleaned up solution:

# star 1
elves=[]
calories=0

with open('rations.txt') as f:
    for line in f:
        try:
            line=int(line)
            calories += line
        except:
            elves.append(calories)
            calories = 0

print("Max calories by one elf:", max(elves))

# star 2
n_top_elves = 3
elves.sort()
print("Sum calories of the top %d elves: "%n_top_elves, sum(elves[-n_top_elves:]))

# -----------------------
# First, quick solution:

"""
elves=[]
calories=0

with open('rations.txt') as f:
    for line in f:
        try:
            line=int(line)
            calories += line
        except:
            elves.append(calories)
            calories = 0

print("Max:", max(elves))

sum_top_elves = 0; n_top_elves = 3
for i in range(n_top_elves):
    sum_top_elves += max(elves)
    elves.remove(max(elves))
    
print("Sum calories of the top %d elves: "%n_top_elves, sum_top_elves)
"""
