#результат вызова класса - экземпляра класса
class Car:
    model = 'bmw'
    engine = 1.6

a = Car()
b = Car()

#с помощью .__dict__ моно обратиться и к атрибутам экземпляров класса
a.__dict__ 

#создание нового атрибута для экземпляра
a.seat = 4

#изменение атрибута у экземпляра 
a.model = 'Lada'

#локальный атрибут - ранее существовавший, но измененный 