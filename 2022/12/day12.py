#%%

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Star 1

H = []
avail_moves = dict()
make_plots = True

with open("input.txt") as f:
    for line in f:
        line = line.strip("\n")
        H.append(list(line))
        if "S" in list(line):
            start1 = list(line).index("S")
            start0 = len(H)-1
        if "E" in list(line):
            end1 = list(line).index("E")
            end0 = len(H)-1

directions = dict(N = np.array([-1,0]), 
    W = np.array([0,-1]), 
    S = np.array([+1,0]), 
    E = np.array([0,+1]), 
    )

H[start0][start1] = "a"

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
            
            # Edge conditions:
            if i == int(0) and d == "N":
                movements[d] = 0
            if i == int(len(H))-1 and d == "S":
                movements[d] = 0
            if j == int(0) and d == "W":
                movements[d] = 0
            if j == int(len(H[0]))-1 and d == "E":
                movements[d] = 0

        avail_moves[str(i)+"_"+str(j)] = movements

if make_plots:
    image_bg = np.zeros((len(H), len(H[0])))
    for k in range(len(H)):
        for l in range(len(H[0])):
            image_bg[k,l] = ord(H[k][l])
    pixelvalue = np.max(image_bg)*0.95

current_locations = [[0,0]]
new_locations = [[start0, start1]]
winning = False
inverse = dict(N = "S", S = "N", W = "E", E ="W")
steps = 0

while not winning and steps < 20000 and len(new_locations)>0:
    current_locations = new_locations

    if make_plots:
        image = np.copy(image_bg) # zeros(())
        for locations in current_locations:
            image[locations[0], locations[1]] = pixelvalue*1.10 #ord(H[locations[0]][locations[1]])

        ax = sns.heatmap(image, 
            cmap="inferno", 
            cbar=False, 
            square=True, 
            xticklabels=False, 
            yticklabels=False, 
            edgecolors=None).get_figure()
        
        ax.savefig("plots/step_%d.png"%steps)
        ax.clf()
    
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
                    print("We found the way! from ", H[cur_loc[0]][cur_loc[1]], cur_loc[0], cur_loc[1], "to:", H[I][J],[I,J], "in", steps, "steps.")
                    winning = True

            try: 
                avail_moves[cur_loc_str][dir] = 0
            except: 
                continue

print("Ended!", winning)

#%%
