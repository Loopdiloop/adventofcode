import numpy as np

# def: x == ^, -x == v
#     y == >, -y == <
MOVEMENTS = {
    "^": np.array([1, 0]),
    "v": np.array([-1, 0]),
    ">": np.array([0, 1]),
    "<": np.array([0, -1]),
}

with open("input.txt") as inputfile:
    instructions = list(inputfile.read())

# Santa + robo-santa
star_instructions = [[instructions], [instructions[::2], instructions[1::2]]]
for star in [1,2]:
    houses_visited = {}
    houses_visited[tuple(np.array([0, 0]))] = 0

    for instr in star_instructions[star-1]:
        position = np.array([0, 0])
        houses_visited[tuple(position)] += 1

        for move in instr:
            position += MOVEMENTS[move]
            if tuple(position) in houses_visited.keys():
                houses_visited[tuple(position)] += 1
            else:
                houses_visited[tuple(position)] = 1

    print("Number of houses, star %i: "%star, len(houses_visited.keys()))




