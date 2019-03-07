# Check if array has all the elements of a sequence

def perm_check(array):
    counter = [0] * len(array)
    for elem in array:
        if not 1 <= elem <= len(array):
            return 0
        else:
            if counter[elem-1] == 1:
                return 0
            else:
                counter[elem-1] = 1
    return 1

if __name__ == '__main__':
    assert perm_check([1,2,3,4])==1
    assert perm_check([1,3,4])==0