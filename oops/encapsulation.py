#  encapsulation involves building data and methods that operate on the data wothin a single unit

# concept of wrapping data and methods together as a single unit.

# getters and the setter method

# Public , protected and private 



# class Person:
#   def __init__(self, name,age):
#     self.name = name # public variable 
#     self.age = age 

# def get_name():
#   return person.name
  
# person = Person("Kedar", 21)

# **************************************************



# class Person:
#   def __init__(self, name,age,gender):
#     self.__name = name # private variable 
#     self.__age = age 
#     self.gender= gender # public variable 
  

# person = Person("Kedar", 21,"Male")
# print(dir(person))

# ['(_Person__age', '_Person__name)', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__'] no age and the name variable separately 

# *********************************************************
class Person:
  def __init__(self, name,age,gender):
    self._name = name # protected variable 
    self._age = age 
    self.gender= gender # public variable 

class Employee(Person):
  def __init__(self,name, age, gender):
    super().__init__(name,age,gender)

# def get_name(person):
#   return person._name

employee = Employee("Kedar", 21, " Male")

print(employee._name)




