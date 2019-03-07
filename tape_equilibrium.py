# return min diff at point of equilibrium

def equilibrium(array):
    diff = None
    if len(array) > 0:
        left = array[0]
        right = sum(array) - left
        diff = abs(left - right)

        for i in range(1, len(array) - 1):
            left += array[i]
            right -= array[i]
            diff = min(diff, abs(left - right))
    return diff
    
if __name__ == '__main__':
    assert equilibrium([1,1,1,1])==0
    