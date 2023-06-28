#процедурное программирование - последовательное

#объектно-ориентированное - деление не объекты, позволяет проще читать код

#класс - основной элемент, в рамках которого осуществляется конструирование программ. Класс содержит в себе данные и код, который управляет этими данными

class Color:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r, g, b):     #пример создания метода (функции)
        red = r
        green = g
        blue = b

    def toHex(self):    #чтобы преобразовать число в 16-ую строку с префиксом 0x
        return '#%02x%02x%02x' 
    
class ColorAlpha(Color):    #создаем класс, наследованный от класса color
    alpha = 1   

    def __init__(self, r, g, b, a):  #добавляем тут еще и переменную альфа
        red = r
        green = g
        blue = b    
        alpha = a    

gray = Color(80, 80, 80)

red = ColorAlpha(255, 0, 0, .5)     #наполовину прозрачный красный цвет

#инкапсуляция - упаковка данных и функций в один компонент (например, класс) и последующий контроль доступа к этому компоненту, создавая тем самым "чёрный ящик" из объекта

#наследование - механизм наложения объекта или класса на другой объект (наследование на основе прототипа) или класс (наследование на основе классов) с сохранением аналогичной реализации

#полиморфизм - когда функция способна обработать данные разных типов