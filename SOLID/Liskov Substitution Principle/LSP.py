
"""
Neste exemplo, uma classe abstrata Vehicle define o método start_engine(). 
As classes Car e Motorcycle herdam de própria Vehicle e substituem o método 
start_engine() com sua implementação. O código que chama o método start_engine()
é capaz de substituir uma instância de Vehicle qualquer uma de suas 
subclasses sem afetar o comportamento esperado.
"""

class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started.")

def start_vehicle_engine(vehicle):
    vehicle.start_engine()

if __name__ == "__main__":

    car = Car()
    motorcycle = Motorcycle()

    start_vehicle_engine(car)  # Car engine started.
    start_vehicle_engine(motorcycle)  # Motorcycle engine started.