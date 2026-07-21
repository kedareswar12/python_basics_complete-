numbers = [1,2,3]
name = "Python"
student = {"name" : "Riya" , 
          "age" : 25}

for item in numbers:
  print(item)
  
  # list tuple string dictionary 
  
# diff between iterables between iterators 
# Iteratables vs Iterators 

# An iterator is a actual object that gives values one by one 

numbers =[10,20,30]
iterator = iter(numbers)
# made as iterator
# next() performs the next value 
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Iterator Protocol -> object should have this 
# __iter__ -> retrun iterator object
# __next__ -> return the next value

# print(iterator.__next__())
# print(iterator.__next__())


# Generators are a simple way to create iterators 


def count_up_to(limit):
  current =1
  while current <= limit:
    yield current
    current= current +1
  
for num in count_up_to(3):
  print(num)
  

# generator expression 

numbers = (x*x for x in range(100))

# for item in numbers:
#   print(item)
print(next(numbers))
print(next(numbers))


# map()

numbers=[1,2,3,4]
squares = map(lambda x : x*x , numbers)
print(squares)
print(next(squares))
print(next(squares))

# reduce() colappse many values to some values 
from functools import reduce 



numbers =[1,2,3,4]
product = reduce(lambda a,b : a*b , numbers )
print(product)

# functional programming











