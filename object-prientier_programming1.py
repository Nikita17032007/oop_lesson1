#объект - фактически контейнер, сост из методов и атрибутов
a = [4, 5, 7]   #4, 5, 7 - данные; 
a.count()   #count - поведение

#экземпляры классов - например: экзмемпляры класса int - все числа от -беск. до + беск., класса list - все комбинации в квадратных скобках и т.д.

#классы - int, float, bool и т.д.

#создание своего класса 

class Car:  #класс должен начинаться с большой буквы
    model = 'bmw'   #пример введения данных, присваеваемых объектам при создании

#можно создать бесконечное множество объектов с этим классом
s = Car()
b = Car()

isinstance(a, Car)  #если напечатать это, то будет видно, что s принадлежит классу Car