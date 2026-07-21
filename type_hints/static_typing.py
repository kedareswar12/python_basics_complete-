# how to add t etype bits to the python codeusing the typing module 

# Type hints -> allows us to mention th eexcepted type of the variables methods and return values 

def greet( name : str ) -> str:
  return f"Hello,{name}"

message = greet("Kedar")
print(message)

name : str = "Kedar"
age : int = 21
marks: int = 9.23


def add(a:int , b:int) -> int:
  return a+b
result = add(20,30)
print(result)



# Typing module provides many useful types for writing bettere type hints 

from typing import Optional,Union,Any,TypeDict,NamedTuple












