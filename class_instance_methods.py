#метод экземпляра - функция, влияющая на экземпляр
def func(self):    #в качестве аргумента по умолчанию принято писать self
    None

class Person:
    
    def send_hello(self):   #при вызове обязательно надо указывать аргумент (можно экземпляр), иначе ничего не выйдет
        print('Hello')

p = Person()    #если не указать аргумент и вызвать от этого экземпляра функцию send_hello, то ничего не выйдет тк интерпритатор видит экхемпляр как аргумент функции