from abstract_dtypes.exception import DS_LIB_ERROR


class Stack:
    def __init__(self):
        self.values = []

    def push(self, data):
        return self.values.append(data)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[len(self.values) - 1]

    def isEmpty(self):
        return self.values == []

    def size(self):
        return len(self.values)
