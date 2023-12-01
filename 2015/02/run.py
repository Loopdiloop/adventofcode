
def wrapping_paper_for_box(l,w,h):
    area = [l*w, w*h, h*l]
    return 2*sum(area) + min(area)

def ribbon_for_box(dim):
    #length + bow
    dim.sort()
    return 2*sum(dim[:2]) + dim[0]*dim[1]*dim[2]

paper = 0
ribbon = 0

with open("input.txt") as inputfile:
    lines = inputfile.readlines()
    for line in lines:
        line = line.strip("\n").split("x")
        line[:] = [int(x) for x in line]
        paper += wrapping_paper_for_box(line[0],line[1],line[2])
        ribbon += ribbon_for_box(line)
print("Paper: ", paper, "Ribbon: ", ribbon)

if __name__=="__main__":
    # test
    assert abs(58 - wrapping_paper_for_box(2,3,4))<0.0001
    assert abs(43 - wrapping_paper_for_box(1,1,10))<0.0001
