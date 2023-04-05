#2.3 Практика "Создание класса и его методов"

class Stack():
    def __init__(self):
        self.values = []
    def push(self, item):
        self.values.append(item)
    def pop(self):
        if self.values:
            return self.values.pop()
        else:
            print('Empty Stack')
            return None
    def peek(self):
        if self.values:
            return self.values[-1]
        else:
            print('Empty Stack')
            return None
    def is_empty(self):
        return not self.values
    def size(self):
        return len (self.values)