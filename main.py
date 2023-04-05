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
###########################################
persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]


class Worker():
    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f'Worker {self.name}; passport-{self.passport}')


worker_objects = []

for i in persons:
    worker_objects.append(Worker(i[0], i[1], i[2], i[3]))

for i in worker_objects:
    i.get_info()

###########################################
class CustomLabel():
    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            setattr(self, key, value)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)