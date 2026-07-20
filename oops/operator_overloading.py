# ommon operatr overloading magic methods 

"""
__add__(self,other) : adds two objects using the - operator 
__sub__(self,other) : Subracts two objects using the - operator
__nul__(self,other) : Multiplies two objects using the * operator 
__truediv__(self,other): Divides twoo onjects using the / operator 
__eq__(self,other) : checks if two objects are equal using the == operator
__lt__(self,other) : checks if one object is less than another using the < operator

"""

class Vector:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def __add__(self,other):
    return Vector(self.x + other.x , self.y+other.y)
  def __sub__(self,other):
    return Vector(self.x - other.x , self.y- other.y)
  def __mul__(self,other):
    return Vector(self.x * other.x , self.y*other.y)
  def __eq__(self,other):
    return Vector(self.x == other.x , self.y == other.y)
  def __repr__(self):
    return f"Vector({self.x} , {self.y})"
v1 = Vector(2,3)
v2 = Vector(4,5)

print(v1+v2)