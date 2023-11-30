
instructions = "instructions.txt"
initial_placements = "initial_configuration.txt"

def load_placements(initial_placements_file):

    placements = [[],[],[],[],[],[],[],[],[]]
    cc_initials = []
    with open(initial_placements_file) as cc:
        for line in cc:
            cc_initials.append(list(line))

    indexes = [1,5,9,13,17,21,25,29,33,37]
    cc_initials.reverse()

    for data in cc_initials[1:]:
        for i in range(9):
            if data[indexes[i]] != " ":
                placements[i].append(data[indexes[i]])
    return placements


def CrateMover9000(no_of_crates, start, end, placements):
    # star 1:
    for i in range(no_of_crates):
        placements[end].append(placements[start][-1])
        placements[start] = placements[start][:-1]
    return placements

def CrateMover9001(no_of_crates, start, end, placements):
    # star 2:
    placements[end] += placements[start][-no_of_crates:]
    placements[start] = placements[start][:-no_of_crates]
    return placements

star1 = load_placements(initial_placements)
star2 = load_placements(initial_placements)

with open(instructions) as f:
    for line in f:

        p1, p2 = line.split("from")
        p1 = p1.strip("move")
        p2, p3 = p2.split("to")

        no_of_crates=int(p1.strip(" "))
        start=int(p2.strip(" "))-1
        end=int(p3.strip(" "))-1

        star1 = CrateMover9000(no_of_crates, start, end, star1)
        star2 = CrateMover9001(no_of_crates, start, end, star2)
        

key1 = ""; key2 = ""
for j in range(len(star1)):
    key1 += star1[j][-1]
    key2 += star2[j][-1]
    

print(f"Star 1: CrateMover9000 {key1}")
print(f"Star 2: CrateMover9001 {key2}")


