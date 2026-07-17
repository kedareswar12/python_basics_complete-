# reuseable of the code to to perform the specific task 


def greet():
  print("Hi welcome to learning python")

greet()

# positioanl arguments are passed based on the order of the parameters in the function 

def introduce(name, age):
  print(f"i am {name} and i am {age} years old")

introduce("Kedar" , 25)

# Keyword arguments are passes using the parameter names so the order doesnot mattter 

introduce(age =22 , name ="Kedar")

# default arguments 
# when no values are passes -> read this

# *args allows a function to accept any number of the positional arguments 
def add_numbers(*args):
  print(sum(args))

add_numbers(10,20,30,40,50)
# print(add_numbers)
# it store them as a tuple

# *kwars will make to accepct any number of the keyword arguments 
#it stores them as a dictionary
def show_profile(**kargs):
  print(kargs)

show_profile(name="Kedar", age=25, gender ="Male")

# global and the nonlocal

# lambda Expression > are small ananymous function used for short one line operations 

square  = lambda x: x*x
print(square(5))

add = lambda a,b: a+b
print(add(3,5))

# def add(a:int, b int )->int:
#   return a+b 

# map function
# mapping the function with the attrobutes
def square(x):
  return x*x
numbers =[1,2,3,4,5]
value =map(square,numbers)
print(list(value))
# [1, 4, 9, 16, 25]

numbers1 = [1,2,3,4]
numbers2 = [5,6,7,8]

added_numbers = map(lambda x,y:x+y, numbers1,numbers2 ) 
print (list(added_numbers))

# map() is used to convert list into integers 
str_numbers = ['1','2','3','4']
int_numbers =list(map(int ,str_numbers))
print (int_numbers)

# filter function

list11 = [1,2,32,1,3,4,3,2,4,2,23,42,2,42]
def even(x):
  if x%2 == 0:
    return True
  
answer=list(filter(even, list11))
print(answer)
# [2, 32, 4, 2, 4, 2, 42, 2, 42]


answer=list(map(even, list11))
print(answer)
# [None, True, True, None, None, True, None, True, True, True, None, True, True, True]

# usinf lambda and the filter
list33 = [1,3,4,5,6,7,4,7,7,8,66,5,4,6,8]
# def greater_than_5(x):
#   if x>5:
#     return True

ans1 =list( filter(lambda x : x>5 , list33))
print(ans1)