class BankAccount:

    def __init__(self, name, balance, passport):
        #чтоб создать protected атрибут нужно перед именем поставить одно нижнее подчеркивание, а чтоб создать private нужно добавить 2 нижних подчеркивания
        self._name = name
        self._balance = balance
        self._passport = passport

acc1 = BankAccount('Bob', 100000, 456456456)