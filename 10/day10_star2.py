
#%%
import numpy as np
from matplotlib import pyplot as plt

X = 1 #middle of sprite
cycle = -1
signal_strengths = dict()

class simulate_screen():
    def __init__(self):
        self.rows = np.tile(np.linspace(0,39,40).astype(np.int64), 50)
        self.visualization = np.zeros((7,41))

    def C(self, cycle, X):
        n_row = int(np.floor(cycle/40))
        if self.rows[cycle] in range(X-1, X+2):
            self.visualization[n_row, self.rows[cycle]] = 1
        return None

with open("input.txt") as f:
    S = simulate_screen()
    for line in f:
        l = line.strip("\n")
        l = l.strip(" ")
        l = l.split(" ")
       
        if l[0] == "addx": # l[1] = V
            #two cycles, adds/subtracts V
            
            cycle += 1
            S.C(cycle, X)
            signal_strengths[cycle] = cycle*X
            
            cycle +=1
            S.C(cycle, X)
            
            signal_strengths[cycle] = cycle*X
            X += int(l[1])

        elif l[0] == "noop":
            cycle += 1
            S.C(cycle, X)
            signal_strengths[cycle] = cycle*X
            
        elif l[0] == "" or l[0] == " ":
            continue
        else:
            print(line)
            print(len(l[0]), l[0])
            raise ValueError


interesting_cycles = [20, 60, 100, 140, 180, 220]
strength_sum = 0
for i in interesting_cycles:
    strength_sum += signal_strengths[i]
    print(i, signal_strengths[i])
print("Total strength: ", strength_sum)

plt.imshow(S.visualization, interpolation="nearest", cmap="gnuplot")
plt.show()

#%%