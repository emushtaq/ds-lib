from functools import reduce
# find the single lonely element in a duplicate int array. eg: [1,2,3,4,1,2,3] ==> 4
def find_missing_interger_in_sequence(array):
    return reduce(lambda x, y: x^y, array)