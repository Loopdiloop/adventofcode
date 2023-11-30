

#%%

import numpy as np
import matplotlib.pyplot as plt

# Star 2

HH = []
startpunkter = []
with open("input.txt") as f:
    for line in f:
        line = line.strip("\n")
        line = list(line)
        HH.append(line)
        # from star 1:
        #if "S" in line:
        #    start1 = line.index("S")
        #    start0 = len(HH)-1
        if "E" in line:
            end1 = line.index("E")
            end0 = len(HH)-1
        for ii in range(len(line)):
            if line[ii] == "a":
                startpunkter.append([len(HH)-1,ii])

    directions = dict(N = np.array([-1,0]), 
        W = np.array([0,-1]), 
        S = np.array([+1,0]), 
        E = np.array([0,+1]), 
        )


path_lengths = dict()

for sp in range(len(startpunkter)):
    start0 = startpunkter[sp][0]
    start1 = startpunkter[sp][1]

    avail_moves = dict()
    H = np.copy(HH)

    for i in range(len(H)):
        for j in range(len(H[0])):
            movements = dict()
            for d in directions.keys():
                i_corr, j_corr = directions[d]
                a = H[i][j]

                if i+i_corr < len(H) and j+j_corr < (len(H[0])):
                    b = H[i+i_corr][j+j_corr]
                else:
                    b = "H"
                
                if b == "E" and a in["z","y"]:
                    movements[d] = int(1)
                elif int(abs(ord(b) - ord(a))) <= 1 and b != "E":
                    movements[d] = int(1)
                elif ord(a) - ord(b) > 0 and b != "E":
                    movements[d] = int(1)
                else:
                    movements[d] = int(0)
                
                # Brute force edge conditions:
                if i == int(0) and d == "N":
                    movements[d] = 0
                if i == int(len(H))-1 and d == "S":
                    movements[d] = 0
                if j == int(0) and d == "W":
                    movements[d] = 0
                if j == int(len(H[0]))-1 and d == "E":
                    movements[d] = 0

            avail_moves[str(i)+"_"+str(j)] = movements
            
    current_locations = [[0,0]]
    new_locations = [[start0, start1]]
    winning = False
    inverse = dict(N = "S", S = "N", W = "E", E ="W")
    steps = 0

    while not winning and steps < 400 and len(new_locations)>0:
        current_locations = new_locations

        steps += 1
        new_locations = []
        
        # For all locations
        for cur_loc in current_locations:
            cur_loc_str = str(cur_loc[0])+"_"+str(cur_loc[1])

            # For all directions, NSEWs
            for dir in directions.keys():
                if avail_moves[cur_loc_str][dir] == 1:
                    
                    I = cur_loc[0] + directions[dir][0]*avail_moves[cur_loc_str][dir]
                    J = cur_loc[1] + directions[dir][1]*avail_moves[cur_loc_str][dir]
                    
                    new_locations.append([I,J])

                    try:
                        avail_moves[str(I)+"_"+str(J)][inverse[dir]] = 0
                    except:
                        continue
                    if H[I][J] == "E":
                        print(f"We found the way! Began {H[start0][start1]},{[start0, start1]}, from {H[cur_loc[0]][cur_loc[1]]}, {cur_loc[0]}, {cur_loc[1]}, to: {H[I][J]}, {[I,J]}, in steps: {steps}")
                        if str(start0)+"_"+str(start1) not in path_lengths.keys():
                            path_lengths[str(start0)+"_"+str(start1)] = steps
                        winning = True

                try: 
                    avail_moves[cur_loc_str][dir] = 0
                except: 
                    continue

lengths = 1000
for p in path_lengths.keys():
    if path_lengths[p] < lengths:
        lengths = path_lengths[p]

print("Shortest path found: ", lengths)


#%%