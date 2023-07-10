#1
class Human:

    def __init__(self, age, name, money, house, default_age = 30, default_name = 'Ivan'):
        self.name = name
        self.age = age
        self.money = money
        self.house = house

        def default_info():
            print(default_age, default_name)
        
        def info():
            print(name, age, house, money)
        
        def earn_money():
            money = money + 1000000
            print('your balance is: ', money)

        def buy_house():
            if money < self.cost:
                print('allright')
            else:
                print('not enough money, bro')
        
        def make_deal():
            if money >= self.cost:
                print('your new house!', 'https://onyx-realty.ru/houses/ownership/dom-u-morya-844232/')
            else:
                print('not enough money :(')
 

nikita = Human(age = 15, name = 'Nikita', money = 20000000, house = 'none')

class House:
    
    def __init__(self, cost, square):
        self.square = square
        self.cost = cost
        
        a = House(cost = 12500000, square = 147)


