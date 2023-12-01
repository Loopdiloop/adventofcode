addon=0

with open("input.txt") as openfile:
    for line in openfile.readlines():
        line=line.replace("\n", "")
        line=line.replace("one","o1e").replace("two","t2o").replace("three","t3e").replace("four","f4r").replace("five","f5e").replace("six","s6x").replace("seven","s7n").replace("eight","e8t").replace("nine","n9e")#.replace("zero", "0")
        
        for abc in list("abcdefghijklmnopqrstuvwxyz"):
            line=line.replace(abc, "")
        line=list(line)
        addon += int(str(line[0])+str(line[-1]))

print(addon)


