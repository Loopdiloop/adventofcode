
def do_operation(operation, old):
    assert operation[0] == "new"
    assert operation[1] == "="

    if operation[2] == "old":
        a = old
    else:
        a = int(operation[2])

    if operation[4] == "old":
        b = old
    else:
        b = int(operation[4])

    if operation[3] == "*":
        result = a*b
    elif operation[3] == "+":
        result = a+b
    else:
        assert False

    return int(result)

def do_test(test_criteria, X):
    if test_criteria[0] == "divisible":
        if X%int(test_criteria[2]) == 0:
            return True
        else:
            return False
    else:
        assert False


if __name__ == "__main__":
    assert int(80) == do_operation(["new", "=", "old", "*", "4"], 20)
    assert not int(9) == do_operation(["new", "=", "old", "+", "old"], 5)

    assert do_test(["divisible", "by", "5"], 15)
    assert not do_test(["divisible", "by", "6"], 13)

    print("Tests ok.")