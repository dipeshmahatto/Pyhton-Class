from abc import ABC,abstractmethod ;

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass  # ... or pass  to skip 
    
    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def __init__(self,name) -> None:
        self.name= name
    
    def start(self):
        print(f"{self.name} is starting....")

    def stop(self):
        print(f"{self.name} is stoped")

car = Car("Honda")
car.start()
car.stop()