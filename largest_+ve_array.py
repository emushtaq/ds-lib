# return next largest consecutive positive in array

def largest_positive_in_array(array):
    largest = 1 # needs validation on the array element
    collection = set(array)

    while largest in collection:
        largest += 1

    return largest

if __name__ == '__main__':
    assert largest_positive_in_array([1,2,3,6,7]) == 4
