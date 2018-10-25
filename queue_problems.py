from abstract_dtypes.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print("\n----------- PARANTHESIS CHECKER: ")
print("original: {} result: {}".format('"Bill","David","Susan","Jane","Kent","Brad", 7', hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7)))
