# allows that object of differnt class to be treated as object of common super class, it provides a way to perform single action in different forms. Polymorphism is typically achieved thriugh method overriding and the interfaces 

# Method Overriding 
# allows a child class to provide a specific implementation of a method that is already defined in its papent class 

# Base class 
class Animal:
  def speak(self):
    return "Sound of the amimal"

# Derived class
class Dog(Animal):
  def speak(self):
    return "woof!"

class Cat(Animal):
  def speak(self):
    return "Meow!!"

# Function that demonstrates polymorphism
def animal_speak(animal):
  print(animal.speak())

  
dog = Dog()
# print(dog.speak())
cat = Cat()
# print(cat.speak())
animal_speak(dog)


# Polymorphism with function and methods 
# Base 
class Shape():
  def area(self):
    return " The area of the figure"
# Derived class 
class Rectangle(Shape):
  def __init__(self,width,height):
    self.width =width
    self.height = height

  def area(self):
    return self.width * self.height 

# Derived class2
class Square(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side * self.side
  
# function that demonstrates the polymorphism
def print_area(shape):
  print(f" the area is {shape.area()}")

rectangle = Rectangle(4,5)
print(rectangle.area())

square = Square(5)

print_area(rectangle)
print_area(square)













