class Car:
    model = 'BMW'
    engine = 1.6
    
    #внутри класа можно указать не только переменные, но и функции
    @staticmethod
    def drive(self):
        print("let's go")

#для экземпляра класса эта функция будет bound method, а для самого класса main function
a = Car() 

#чтоб указать функцию, которая будет относиться и к классу и к его экземплярам нуно обратиться к декоратору staticmethod (см. выше)