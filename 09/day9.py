import numpy as np
import sys

try:
    star = int(sys.argv[1])
    assert star in [1,2]
except:
    star = 2

if star == 1:
    n = 2
elif star == 2:
    n = 10

#KNOTS.
K=np.zeros((n+2,2), dtype=np.int64)
previous_positions = []

movements = dict(R = np.array([1,0]),
    L = np.array([-1,0]),
    U = np.array([0,1]),
    D = np.array([0,-1]),
)

def stable(I_stable,J_stable): # IJ / HT doesn't matter
    diff_stable = I_stable - J_stable
    if all(np.absolute(diff_stable) <= np.ones(2)) == True:
        return True
    else:
        return False

def update_T(I,J): #I head, J tail
    diff = I-J
    abs_diff = list(np.absolute(diff))
    if [0] in abs_diff and [2] in abs_diff:
        J += (diff/2).astype(int)

    elif abs_diff == [1,2] or abs_diff == [2,1]:
        J += (diff/np.absolute(diff)).astype(np.int64)
    
    elif abs_diff == [2,2]:
        J += (diff/np.absolute(diff)).astype(np.int64)
    else:
        print("ERROR?! ", "pulling", I, " following", J, "diff is:", diff)
        assert False
    return J

with open("input.txt") as f:
    for line in f:
        l = line.strip("\n")
        l = l.split(" ")

        for i in range(int(l[1])):
            K[0] += movements[l[0]]
            for knot in range(1,n): #Move the rest of the knots after K[0]
                if not stable(K[knot-1], K[knot]):
                    K[knot] = update_T(K[knot-1], K[knot])
            
            tail_pos = str(K[n-1][0])+":"+str(K[n-1][1])
            if tail_pos not in previous_positions:
                previous_positions.append(tail_pos)

print("Star %d, number of previous positions for tail: "%star, len(previous_positions))



# For sanity:
def test_update_T():
    test1 = update_T(np.array([4,4]), np.array([4,6]))
    assert all(test1 == np.array([4,5])), test1

    test2 = update_T(np.array([-4,-4]), np.array([-6,-4]))
    assert all(test2 == np.array([-5,-4])), test2

    test3 = update_T(np.array([3,-7]), np.array([2,-9]))
    assert all(test3 == np.array([3,-8])), test3
    print("Test update ok.")

def test_stable():
    assert stable(np.array([4,4]), np.array([5,4]))
    assert stable(np.array([-4,-4]), np.array([-3,-3]))
    assert not stable(np.array([4,4]), np.array([5,6]))
    assert not stable(np.array([-4,4]), np.array([-5,6]))
    print("Test stable ok.")

if __name__=="__main__":
    test_update_T()
    test_stable()
