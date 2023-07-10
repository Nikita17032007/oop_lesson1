#магический метод - который начинается и заканчивается '__' (например init, call, str и тд)
class Cat:

    #метод init создан для инициализации (заполнения объекта значениями)
    
    #для того, чтобы заполнить значения в момент инициализации нужно указать параметры в скобках (в данном случае name, breed, age, color)
         
    def __init__(self, name, breed, age, color):    #принимает экземпляр, который создается в процессе вызова класса внутрь этого метода
        print('hello new object', self, name, breed = 'pers', age = 1, color = 'white')
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

Walt = Cat('Walt')    #если вызвать экземпляр, то у него будут значение имени Walt, а все остальные значения будут по умолчанию

Kelly = Cat(name = 'Kelly', breed = 'siam', age = 5, color = 'black' )    #тут уже у экземпляра будет каждый параметр своим

Bob = Cat()    #если вызвать этот экземпляр, то у него будет одна переменная (breed)
Bob.set_Value('Bob')    #после указания value у экземпляра появится две переменных (age, value)        

Tom = Cat()    #если вызвать этот экземпляр, то увидим примерно такое сообщение: hello new object is <__main__.Cat object at 0x00000000
