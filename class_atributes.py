#атрибуты класса в данном случае - это name и age
class Person:
    name = 'Ivan'
    age = 30

#можно обратиться к атрибуту, введя сначала название класса, а потом через точку атрибут, значение которого надо узнать, но нельзя обратиться к атриуту, который не определен в классе
Person.age  #в данном случае если мы выведем эту команду, то покажет значение 30

#можно так же обратиться сразу ко всем атрибутам можно двумя способами
Person.__dict__

#с помощью getattr можно передать значение, которое вернется, если нету указанного атрибута
getattr(Person, 'x', 100)     #то есть если нет атрибута x, то вернет значение 100

#изменить значение атрибута очень легко
Person.name = 'Misha'   #т.е. теперь если мы вызовем атрибут name то нам вернет значение Misha
Person.s = 200     #с помощью изменения значения можно ввести несуществавшие ранее значения

#значение атрибута можно ввести с помощью функции setattr (объект, имя атрибута, значение)
setattr(Person, 'y', 150)

#удалить можно либо с помощью команды del Имя_класса.имя_атрибута либо функцией delattr
del Person.s
delattr(Person, 'y')

#добавим объект в наш класс
a = Person()
b = Person()

#если после добавления или удаления объектов указать новые атрибуты класса, то они автоматически присвоятся всем объектам

#так же можно добавлять атрибуты к отдельным объектам в классе
a.h = 400   #после этого у объекта а появится атрибут h, которого не будет у других объектов в классе