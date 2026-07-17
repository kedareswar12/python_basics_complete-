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
# use default in git 
print(student.get('last_name', "Not avalilabe"))
# output -> Not avalilabe

# Modifying the dictionary elements 
# they are mutable so you cn add update and delete elements but key need to be unique

# Adding the new key 



student ={
  "Name":"Kedar",
  "age" :21,
  "grade":"BTech"
}
student["address"] = "America - near white house"
print(student)

student['gender'] = 'Male'
print(student)


# delete the key
del student['gender'] ## deletes the key and the value pair 
print(student)


# dictionary methods 
keys = student.keys()
print(keys)
values = student.values()
print(values)

# Key value pairs 
print(student.items())


print("*******************************")

#### shallow copy 


student_copy = student
print(student)
print(student_copy)

student['Name']= "Kedareswar"
print(student)
print(student_copy)

# here if you see deep copy is happening 
# {'Name': 'Kedareswar', 'age': 21, 'grade': 'BTech', 'address': 'America - near white house'}
# {'Name': 'Kedareswar', 'age': 21, 'grade': 'BTech', 'address': 'America - near white house'}
# {'Name': 'Kedareswar', 'age': 21, 'grade': 'BTech', 'address': 'America - near white house'}
# {'Name': 'Kedareswar', 'age': 21, 'grade': 'BTech', 'address': 'America - near white house'}



# for shallow copy 

student_copy = student.copy() # here it will give the reference to another memory so it never change 
student ={
  "Name":"Kedar",
  "age" :21,
  "grade":"BTech"
}
student['Name']= "Kedareswar"
print(student)
student_copy = student.copy()
print(student_copy)


# iterating over the dictionaries 

print(student)

for keys in student.keys():
  print(keys)

for values in student.values():
  print(values)

# iterate over the key value pairs 
for key, value in student.items():
  print(f"{key}  : {value}" )

# Nested Dictionaries 
students = {
    "student1": {
        "name": "Aarav Sharma",
        "grade": "A",
        "age": 20,
        "address": "Hyderabad"
    },
    "student2": {
        "name": "Priya Reddy",
        "grade": "B+",
        "age": 19,
        "address": "Bengaluru"
    },
    "student3": {
        "name": "Rahul Verma",
        "grade": "A+",
        "age": 21,
        "address": "Chennai"
    },
    "student4": {
        "name": "Sneha Patel",
        "grade": "B",
        "age": 18,
        "address": "Mumbai"
    },
    "student5": {
        "name": "Vikram Singh",
        "grade": "C+",
        "age": 22,
        "address": "Pune"
    }
}

print(students)

# access the nested elements 
print(students["student2"]["address"])

# iteration over the nested student 
for student_id, student_info in students.items():
  print(f"{student_id} : {student_info}")
  for key,value in student_info.items():
    print(f"{key} : {value}")

# Dictionary Comprehension 
# eg getting the square 
squares ={x:x**2 for x in range(5)}
print (squares) 

squares ={x:x**2 for x in range(5) if x%2 ==0 }
print(squares)

# practical example 
numbers = [1,2,3,2,3,4,4,5,4,3,5,6,3,3,2,2,4,]
frequency={}

for number in numbers:
  if number in frequency:
    frequency[number]=frequency[number] +1
  else :
    frequency[number] =1
print(frequency)

# merging of the dictionary 
book = {
    "title": "Python Basics",
    "author": "John",
    "price": 499
}

phone = {
    "brand": "Samsung",
    "color": "Black",
    "storage": "128GB"
}

merged_dictionary = {**book,**phone}
print(merged_dictionary)