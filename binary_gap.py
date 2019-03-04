def binary_gap(decimal_number):
    result = 0
    present = False
    count = 0

    while decimal_number:
        if decimal_number & 1: # bitwise binary 1 check
            if present==False:
                present=True  # mark the first observed 1
            else:
                result = max(0, count) # account for max zeros

            count = 0  # reset counter

        else:   # 0 found, increment counter
            count += 1

        decimal_number>>1  # right-shift
