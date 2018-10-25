from abstract_dtypes.deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


print("\n----------- PALINDROME CHECKER: ")
print("original: {} result: {}".format("lsdkjfskf", palchecker("lsdkjfskf")))
print("original: {} result: {}".format("malayalam", palchecker("malayalam")))
