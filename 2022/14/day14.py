#%% #Wsl doesn't easily allow for graphics..
import numpy as np
import matplotlib.pyplot as plt


class simulate_cave():
    def __init__(self, n) -> None:
        self.n = n
        self.cave = np.zeros((n*2,n), dtype=np.int64)
        self.S = np.array([500,0], dtype=np.int64)
        self.previous_path = "..."
        pass

    def build_cave(self, x, y) -> None:
        i=0
        for i in range(len(x)-1):
            X = np.sort([x[i], x[i+1]]) 
            Y = np.sort([y[i], y[i+1]])
            self.cave[X[0]:X[1]+1,Y[0]:Y[1]+1] = np.int64(2)
        return None
    
    def add_floor_in_cave(self) -> None:
        for i in range(len(self.cave[0])):
            if any(self.cave[:,i] == 2):
                y_lowest = i
        self.cave[:,y_lowest+2] = 2
    
    def sand_falling(self, x,y):
        if self.cave[x,y+1] == 0:  # Fall straight down
            return x,y+1
        elif self.cave[x-1,y+1] == 0:  # Down and left
            return x-1, y+1
        elif self.cave[x+1,y+1] == 0:  # Down and right
            return x+1,y+1
        else:
            return x, y
    
    def spawn_sand(self):
        sx = self.S[0]
        sy = self.S[1]
        looping = True
        path = ""
        
        c = 0
        while looping and c < 10000:
            if self.cave[self.S[0], self.S[1]] == 1:
                print("It's full!")
                return 0
            x , y = self.sand_falling(sx, sy)
            if sx == x and sy == y:
                self.cave[x,y] = 1
                return 1
            
            path += ".%d-%d"%(x,y)

            if abs(y) > 200: #void
                if path == self.previous_path:
                    # Everything falls!
                    return 0
                self.previous_path = path
                return 1
            sx = x; sy = y
            c+=1

    def visualize_cave(self):
        plt.imshow(np.transpose(self.cave[450:560, 0:190]))
        plt.show()
        return None

    def number_of_sand_in_simulation(self, flavour_text) -> int:
        unique, counts = np.unique(self.cave, return_counts=True)
        entries = dict(zip(unique, counts))
        print(flavour_text, entries[1])
        return entries[1]

def run_simulation(star = 1):
    cave = simulate_cave(500)
    with open("input.txt") as f:
        for l in f:
            l=l.strip("\n")
            l=l.split(" -> ")
            x=[] ; y=[]
            for p in l:
                x_,y_ = p.split(",")
                x.append(x_)
                y.append(y_)
            cave.build_cave(np.array(x, dtype=np.int64),np.array(y, dtype=np.int64))
    if star == 2:
        cave.add_floor_in_cave()
    spawn = True
    while spawn == True:
        spawn = cave.spawn_sand()
    cave.visualize_cave()
    cave.number_of_sand_in_simulation("Star %d : Total number of sand :"%star)

run_simulation(star = 1)
run_simulation(star = 2)

#%%
