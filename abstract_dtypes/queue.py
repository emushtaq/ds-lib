from abstract_dtypes.exception import DS_LIB_ERROR


class Queue:
    def __init__(self):
        self.values = []

    def isEmpty(self):
        return self.values == []

    def enqueue(self, data):
        self.values.insert(0, data) # O(n)

    def dequeue(self):
        return self.values.pop()

    def size(self):
        return len(self.values)
