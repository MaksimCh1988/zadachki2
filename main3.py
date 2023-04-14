class PowerTwo():
    def __init__(self, number):
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number + 1:
            raise StopIteration
        else:
            index = self.counter
            self.counter += 1
            return 2 ** index