
X = 1
cycle = 0
signal_strengths =dict()

with open("input.txt") as f:
    for line in f:
        l = line.strip("\n")
        l = l.strip(" ")
        l = l.split(" ")
       

        if l[0] == "addx": # l[1] = V
            #two cycles, adds/subtracts V
            cycle += 1
            signal_strengths[cycle] = cycle*X
            
            cycle +=1
            signal_strengths[cycle] = cycle*X
            X += int(l[1])

        elif l[0] == "noop":
            cycle += 1
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

