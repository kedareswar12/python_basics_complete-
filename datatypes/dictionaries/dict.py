# dictionaries are the unordred collection of items , they store the data in key-value pairs 
# keys must be unique and they are immutable while values can be any type 

# creating the dictionaries 
empty_dict ={}
# empty_dict ={}
print(type(empty_dict))


student ={
  "Name":"Kedareswar",
  "age" :21,
  "grade":"BTech"
}

print(student)

student ={
  "Name":"Kedareswar",
  "age" :21,
  "Name":"BTech"
}
print(student)
# {'Name': 'BTech', 'age': 21}  -> updated one 

# accessing the dict elements 
print(student['age'])

# using get method
print(student.get('Name'))

