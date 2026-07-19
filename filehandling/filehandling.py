# File I/O operations are the files input and the output operations 
# files are useful when we wanted to store the data permanantly instead keeping it  only in the memory 
file = open('notes.txt' , 'r')

content = file.read()
file.readline() # Read one line
file.readlines() 
file.close()

# print(content)

file= open('notes.txt', 'a')
file.write("\nHello python I am here \n")
file.close()

# print(content)


# 'r' -> read
# 'w' -> write
# 'a' -> pending 
# 'rb'-> read binary File
# 'x' -> creates new file , fials if the file exsists
#'wb' -> write binary

# file= open('images.png' , 'rb')
# data = file.read()
# file.close()


# context managers 
# with -> it automatilcally clases after the file use 
# with open('notes.txt','r',encoding= 'utf-8') as file:
#   content = file.read()
# # to write in the file 

# with open('notes.txt', 'w', encoding= 'utf-8' )as file:
#   content = file.write("\n Hi now we are writing in the notes.txt file from the filehandling.py python file")

# print(content)

# working with paths with os.paths -> helps with files and folder paths 

import os 

path = 'notes.txt'

print(os.path.exists('notes.txt'))
print(os.path.abspath('notes.txt'))

print(os.path.join('data','notes.txt')) 

# pathlib -> is cleaner way to work
# basically it treat it as objects 


from pathlib import Path

path = Path("notes.txt")

print(path.name)
print(path.exists())


# standard streams -> python has 3 
# python has 3 standard streams that handle input output and the errors 

# stdin > standard input 
# stdout > standard output
# stderr > standard error


name = input("Enter your name : ")
print(name)
# here program pauses wait until the user writes 


import sys

data= sys.stdin.readlines()

print(data)

# 

import sys

data= sys.stdin.readlines()

print(data)

# 

import sys

data= sys.stdin.readlines()
# readline() -> reads the complete file (EOF _> End of file)
# read-> reads the entire strings 


print(data)

# ['\n', 'Hi i am wring the first line \n', 'hi i am wring th esecond line and to exit \n', 'in windows you can use ctrl + z and in the linux you can use ctrl + D ', '\n', '\n']


print("This is normal output")

sys.stdout.write("\n This is the output form the stdout statement \n")
# without \n it goes to the same line


# import sys

# sys.stdout.write("Hello")
# sys.stdout.write(" Python")

# Output:

# Hello Python

sys.stderr.write("This is the error we are getting but is act as  a print statement  ")

# Serilization 
# converting the python data into a format that can be saved in a file or yransffered over a network 

student={
  "name" : "Kedareswar",
  "age" : 32
}

# json -> readable text format 
# csv -> tabular data format
# pickle -> python specific binary format 


import json 

with open("student.json" , 'w' , encoding ='utf-8') as file:
  json.dump(student,file) # creates the file and writes the data 

with open('student.json' ,'r' ,encoding ='utf-8') as file:
  data =json.load(file) #reads the file 

print(data)



import csv

student = [
  ["Name", "Age"],
  ["Kedar" , "21"],
  ["Rahul", "32"]
]


with open('student.csv' ,'w', newline="" , encoding= 'utf-8' ) as file:
  writer=csv.writer(file)
  writer.writerows(student)

with open('student.csv' ,'r' , encoding='utf-8')as file:
  reader = csv.reader(file)
  
  for row in reader:
    print(row)


# Pickle 
import pickle

student ={
  "name": "Kedar",
  "age" : 32
}

# pickle.dump(studnet,file) -> creating th epkl file 
# pickle.load(file) -> read the pkl file 
































