class Cat:
    #для начала нужно создать private атрибут которая будет словарем
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    #при каждой инициализации объекта будем применять экземпляру переменную dict и в качестве значения выбираем атрибут 
    def __init__(self):
        self.__dict__ = Cat.__shared_attr

a = Cat()

#если заменить или добавить значение у одного объекта, то оно изменится и у остальных 
a.breed = 'siam'
a.name = 'Bob'

#так же если добавить новую переменную, то старые изменения перейдут на нее
b = Cat()