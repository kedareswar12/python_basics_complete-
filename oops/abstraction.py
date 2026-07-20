from abc import ABC , abstractmethod
# hiding the complex implementation details and showing only the necessary features pf an object 


class Vehicle(ABC):
  def drive(self):
    print("the vehicle is used for driving")

  @abstractmethod
  def start_enginine(self):
    pass

class Car(Vehicle):

  def start_enginine(self):
    print("Car engine started")

def operate_vehicle(vehicle):
  vehicle.start_engine()


car = Car()

