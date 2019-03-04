def cycle_array(array, rotations): # does not contain any validation
    for i in range(rotations):
        array.insert(0, array.pop(-1))
        # or array = [array[-1]] + array[:-1] 
