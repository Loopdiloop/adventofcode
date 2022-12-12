import numpy as np

H=np.array([0,0], dtype=np.int64)
T=np.array([0,0], dtype=np.int64)
previous_positions = []

movements = dict(R = np.array([1,0]),
    L = np.array([-1,0]),
    U = np.array([0,1]),
    D = np.array([0,-1]),
)

def stable(H,T):
    diff = H-T
    if all(np.absolute(diff) <= np.ones(2)) == True:
        return True
    else:
        return False

def update_T(H,T):
    diff = H-T
    abs_diff = list(np.absolute(diff))
    if [0] in abs_diff and [2] in abs_diff:
        T += (diff/2).astype(int)

    elif abs_diff == [1,2] or abs_diff == [2,1]:
        T += (diff/np.absolute(diff)).astype(np.int64)
    
    else:
        print("ERROR?! ", H, T, diff)
        assert False
    return T

with open("input.txt") as f:
    for line in f:
        l = line.strip("\n")
        l = l.split(" ")
        for i in range(int(l[1])):
            H += movements[l[0]]
            if not stable(H,T):
                T = update_T(H,T)
            T_pos = str(T[0])+":"+str(T[1])
            if T_pos not in previous_positions:
                previous_positions.append(T_pos)

previous_positions.sort()
for element in previous_positions:
    print(element)
print("Previous positions: ", len(previous_positions))



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
