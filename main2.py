class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User():
    def __init__(self, login, balance=0):
        self.login = login
        self.__balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self, money):
        self.__balance += money

    def payment(self, money):
        if money > self.__balance:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance -= money
            return True


class Cart():
    def __init__(self, user):
        self.user = user
        self.goods = dict()
        self.__total = 0

    def add(self, product, amount=1):
        if self.goods.get(product):
            self.goods[product] += amount
            self.__total += amount * product.price
        else:
            self.goods[product] = amount
            self.__total += amount * product.price

    def remove(self, product, amount=1):
        if amount >= self.goods[product]:
            self.__total -= self.goods[product] * product.price
            del self.goods[product]
        else:
            self.goods[product] -= amount
            self.__total -= amount * product.price

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        p_result = []
        for i, v in self.goods.items():
            p_result.append(f'{i.name} {i.price} {v} {i.price * v}')
        print('---Your check---')
        for i in sorted(p_result):
            print(i)
        print(f'---Total: {self.total}---')

