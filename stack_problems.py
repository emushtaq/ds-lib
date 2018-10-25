from abstract_dtypes.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print("\n----------- PARANTHESIS CHECKER: ")
print("original: {} result: {}".format('((()))', parChecker('((()))')))
print("original: {} result: {}".format('(()', parChecker('(()')))
print("original: {} result: {}".format('{{([][])}()}', parChecker('{{([][])}()}')))
print("original: {} result: {}".format('[{()]', parChecker('[{()]')))


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print("\n----------- BINARY: ")
print("original: {} result: {}".format(42, divideBy2(42)))

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print("\n----------- BASE CONVERTER GENERAL: ")
print("original: {} result: {}".format('25,2', baseConverter(25,2)))
print("original: {} result: {}".format('25,16', baseConverter(25,16)))
