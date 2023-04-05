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


###########################################
class Task():
    def __init__(self, name, description, status=False):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        print(f"{self.name} ({'Сделана' if self.status else 'Не сделана'})")


class TaskList():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class TaskManager():
    def __init__(self, tasklist):
        self.task_list = tasklist

    def mark_done(self, task):
        task.status = True

    def mark_undone(self, task):
        task.status = False

    def show_tasks(self):
        for i in self.task_list.tasks:
            i.display()

        # Ниже код для проверки классов Task, TaskList и TaskManager


# Создаем список задач
todo = TaskList()
assert todo.tasks == []

# Создаем несколько задач и добавляем их в список
task1 = Task("Стирка", "Постирать трусы, носки, слюнявчики")
assert task1.name == 'Стирка'
assert task1.description == 'Постирать трусы, носки, слюнявчики'
assert task1.status is False
task1.display()

todo.add_task(task1)
assert len(todo.tasks) == 1

task2 = Task("Продукты", "Купить лук чеснок огурцы хлеб и биток")
assert task2.name == 'Продукты'
assert task2.description == 'Купить лук чеснок огурцы хлеб и биток'
assert task2.status is False

todo.add_task(task2)
assert len(todo.tasks) == 2

# Создаем менеджер задач и показываем список задач
manager = TaskManager(todo)
assert isinstance(manager.task_list, TaskList)
print('-----Список дел-----')
manager.show_tasks()

# Отмечаем первую задачу выполненной и показываем список задач
manager.mark_done(task1)

# Проверяем изменился ли статус 2мя способами
assert task1.status is True
assert manager.task_list.tasks[0].status is True

print('-----Список дел-----')
manager.show_tasks()

# Удаляем вторую задачу и показываем список задач
todo.remove_task(task2)

assert len(todo.tasks) == 1
assert len(manager.task_list.tasks) == 1

print('-----Список дел-----')
manager.show_tasks()