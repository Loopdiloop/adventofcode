# 1:
with open("input.txt") as inputfile:
    input = list(inputfile.read())
print("Final floor: ", input.count("(") - input.count(")"))

# 2:
input[:] = [1 if x == "(" else -1 for x in input]
pos=0
for i in range(len(input)):
    pos += input[i]
    if pos < 0:
        print("Basement alarm! ", i+1)
        break
