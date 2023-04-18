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

######################################

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name, self.mileage, self.capacity = name, mileage, capacity

    def fare(self):
        return self.capacity * 100

    def display(self):
        print(f'Total {self.name} fare is: {self.fare()}')


class Bus(Vehicle):
    def __init__(self, name, mileage):
        super().__init__(name, mileage, capacity=50)

    def fare(self):
        return super().fare() * 1.1


class Taxi(Vehicle):
    def __init__(self, name, mileage):
        super().__init__(name, mileage, capacity=4)

    def fare(self):
        return super().fare() * 1.35