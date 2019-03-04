# solution to the codility frogjump question
import math
def min_jumps(start, end, step):
    return math.ceil((end-start)/ step)