import numpy

input_file = "input.txt"
ranges = numpy.loadtxt(input_file, delimiter=",", dtype=(str,str))

# Star 1
# Count ranges that fully contain their partner range

counter=0
for r in ranges:
    a,b = r[0].split("-")
    c, d = r[1].split("-")
    a = int(a); b = int(b); c = int(c); d = int(d)
    if (a <= c and b >= d) or (c <= a and d >= b):
        counter += 1

print(f"Star 1: Number of ranges fully enclosed: {counter}")

# Star 2
# Count ranges with any overlap.

counter=0
for r in ranges:
    a, b = r[0].split("-")
    c, d = r[1].split("-")
    a = int(a); b = int(b); c = int(c); d = int(d)
    
    if any(True for x in range(a,b+1) if x in range(c,d+1)):
        counter += 1

print(f"Star 2: Number of ranges with any overlap: {counter}")