from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Boat(Transport):
    def start_engine(self):
        print('Весла на воду')
    def stop_engine(self):
        print('Суши весла')
    def move(self):
        print('Греби-Гребу')
    def stop(self):
        print('Приплыли')

class Car(Transport):
    def start_engine(self):
        print('Машина завелась')
    def stop_engine(self):
        print('Машина развелась')
    def move(self):
        print('Покатились')
    def stop(self):
        print('Стоп')

class Electroscooter(Transport):
    def start_engine(self):
        print('Дрынь')
    def stop_engine(self):
        print('Выкл')
    def move(self):
        print('Оно едет!')
    def stop(self):
        print('Батареи сели?')

class Person:
    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.stop_engine()

if __name__ == '__main__':
    car = Car()
    boat = Boat()
    electroscooter = Electroscooter()
    person = Person()

    print('Покатаемся на лодке')
    person.use_transport(boat)
    print()
    print('А теперь а машине')
    person.use_transport(car)
    print()
    print('И к современным технологиям')
    person.use_transport(electroscooter)

