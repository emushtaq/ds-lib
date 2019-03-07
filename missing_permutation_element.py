# An array A consisting of N different integers is given. 
# The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
from functools import reduce

def find_missing_element(A):
    # find the total sum of N+1 elements
    length = len(A)
    total_sum = sum(range(1, length+2))
        
    # find the partial sum of given array elements
    partial_sum = reduce(lambda x,y : x+y, A)

    print(A, total_sum, partial_sum)
    # XOR the sums to find the missing element
    return total_sum ^ partial_sum

if __name__ == "__main__":
    assert find_missing_element([1,3,4])==2
    assert find_missing_element([1,2,3,4,5,6,7,9,10,11])==8