# A class is a blue print for creating objects. Attributes and methods 

class Car:
  pass

audi = Car()
bmw = Car()

print(type(audi))
# <class '__main__.Car'>
print(audi)
# <__main__.Car object at 0x7f806c749b80>

# Instance variables and the methods 
class Dog:
  # constructor 
  # instance variables -> name and the method 
  def __init__(self, name, age):
    self.name = name
    self.age = age
    # print("Hi i am constructor") ->  this is executed first 

dog1 = Dog("Mark" , 2)
print(dog1)
print(dog1.name , dog1.age)


# Instance methods 
class Dog_bhai:
  def __init__(self, name, age):
    self.name = name
    self.age= age

  def barking(self):
    print(f"{self.name} says woof")

dog2 = Dog_bhai("Buddy",3)
dog2.barking()


# Modelling a bank account 

# Define a class for the bank account 

class Bank_Account:
  def __init__ (self, owner, balance = 0):
    self.owner = owner
    self.balance = balance 

  def deposit(self, amount):
    if(amount != 0):
      self.balance += amount
      print(f"{amount} is deposited. New balance is : {self.balance} ")

  def withdraw(self,amount):
    if amount< self.balance:
      self.balance = self.balance - amount
      print(f"The {amount} is withdrawed and the balance present is {self.balance}")

    elif amount > self.balance :
      print("Insufficeient funds")

  def get_balance(self):
      print("The total balance in your account is {self.balance}")
      return self.balance 

# create an object 
account1 = Bank_Account("Kedar" , 10000)
print(account1.balance)
# calls this instance method 
account1.deposit(5000)
account1.get_balance()
account1.withdraw(2000)






































