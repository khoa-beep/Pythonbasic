class Stack:
    def __init__(self):
        self._data = []

    def push(self, e):
        self._data.append(e)

    def pop(self):
        return self._data.pop()

    def len(self):
        return len(self._data)

    def is_empty(self):
        return not self._data

    def top(self):
        if self.is_empty():
            return False
        return self._data[-1]


def Binary(n):
    s = Stack()
    n = int(input())
    while n != 0:
        if(n % 2 == 0):
            s.push(0)
        else:
            s.push(1)
        n = n // 2
    v = ''
    while s.len() != 0:
        a = s.pop()
        v = v + str(a)
    print(v)

