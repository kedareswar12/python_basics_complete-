# inheritance will allow a class to inherit attributes and methods from the other class(parent class / base class etc)

class Car:
  def __init__(self, windows, doors , enginetype):
    self.windows =  windows
    self.doors = doors
    self.enginetype = enginetype

  def drive(self):
    print(f"The person will drive the {self.enginetype} car")

  
    
car1 = Car(4,5,"petrol")
car1.drive()

# single inheritance 
class Tesla (Car):
  def __init__(self, windows, doors , engine_type , Isself_driving):
    super().__init__(windows, doors, engine_type)
    self.Isself_driving = Isself_driving
  
  def self_driving(self):
    print(f"Tesla supports self driving : {self.Isself_driving}")

tesla1 = Tesla(4,5,"Electric",True)
tesla1.self_driving()


# Multiple Inheritance 
# when a class inherits from more than one base class 
# Base class 1
class Animal:
  def __init__(self, name):
    self.name = name 

  def speek(self):
    print("Subclasses must implement this method")

# Base class 2 
class Pet:
  def __init__(self, owner):
    self.owner = owner

# Derived class 
class Dog(Animal, Pet):
  def __init__(self, name ,owner):
    Animal.__init__(self, name)
    Pet.__init__(self,owner)


  def speak(self):
    return f"{self.name} will speak oofff "


dog = Dog("Buddy", "Kedar")
print(dog.speak())

