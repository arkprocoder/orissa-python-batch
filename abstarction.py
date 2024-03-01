from abc import ABC , abstractmethod


class Plan(ABC):
    @abstractmethod
    def trip(self):
        pass

    @abstractmethod
    def movie(self):
        pass

    @abstractmethod
    def swimming(self):
        pass


class Execute(Plan):
    
    def greeting(self):
        print('Good Evening')

 
    def trip(self):
        print('Trip is going on')

    def movie(self):
        print('Had been to movie')

    def swimming(self):
        print('Had been to swiming')

obj=Execute()
obj.greeting()