from abc import ABC, abstractmethod

HOUSES = {}


class Person(ABC):
    def __init__(self, name, age, availability_of_money, having_your_own_home):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.having_your_own_home = having_your_own_home
        
    @abstractmethod
    def info(self):
        pass
        
    @abstractmethod
    def make_money(self, money):
        pass
    
    @abstractmethod
    def buy_a_house(self):
        pass
            
class Human(Person):
    def __init__(self, name, age, availability_of_money, having_your_own_home):
        super().__init__(name, age, availability_of_money, having_your_own_home)
        
    def info(self):
        print(f'My name is {self.name} and I am {self.age} years old')
        
    def make_money(self, money):
        self.availability_of_money = self.availability_of_money + money
        
    def buy_a_house(self, house):
        if (self.age >= 18) and (self.having_your_own_home == 0):
            if self.availability_of_money >= house.cost:
                print('You can buy this house')
            else:
                print('You do not have enough money or a house with such an area is not for sale!')
        else:
            print('The law does not allow you to make such purchases!')

class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost
        
        HOUSES[self.area] = [self.cost]     # In dict. format like: {40: 2000} where 40 is square in m2, 2000 - cost
                
                
class RealtorMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

                
class Realtor(metaclass=RealtorMeta):
    def __init__(self, realtor_name):
        self.realtor_name = realtor_name
        
    def info_all_houses(self, HOUSES):
        for key, value in HOUSES.items():
            print(f'A house with an area of {key}m2 costs {value}c.u.')
        
    def give_a_discount(self, human, house):
        if house.area > 200:
            print(f'Hey {human.name}, I can give you a 20% purchase discount')
        elif house.area < 40:
            print(f'Hey {human.name}, I can not give you a purchase discount')
        else:
            print(f'Hey {human.name}, I can give you a 10% purchase discount')
                        
    
    def steal_money(self, human):
        chance = range(1, 10)
        if human.availability_of_money > 0 and chance == 10:
            human.availability_of_money = 0
            print(f'Realtor {self.realtor_name} stole money from {human.name}')
        else:
            print('Hmmmm. Someday I will be lucky too')
        
        
human1 = Human('Andy', 20, 2000, 0)
human1.info()
human1.make_money(2500)
print(human1.availability_of_money)
human2 = Human('Angela', 17, 2000, 0)
human2.info()
human2.make_money(2500)
house1 = House(40, 2000)
house2 = House(80, 5000)
house3 = House(120, 10000)
human1.buy_a_house(house1)
human1.buy_a_house(house3)
human2.buy_a_house(house1)
realtor = Realtor('Moody')
realtor.steal_money(human1)
realtor.info_all_houses(HOUSES)
realtor.give_a_discount(human1, house2)
