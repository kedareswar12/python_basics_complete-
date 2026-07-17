import array
arr = array.array("i" , [1,2,3,4])
print(arr)
# array functions takes the two arguments only 
# array.array(typecode, initializer)

# | Typecode | Data Type          |
# | -------- | ------------------ |
# | `'b'`    | Signed char        |
# | `'B'`    | Unsigned char      |
# | `'h'`    | Signed short       |
# | `'H'`    | Unsigned short     |
# | `'i'`    | Signed int         |
# | `'I'`    | Unsigned int       |
# | `'l'`    | Signed long        |
# | `'L'`    | Unsigned long      |
# | `'q'`    | Signed long long   |
# | `'Q'`    | Unsigned long long |
# | `'f'`    | Float              |
# | `'d'`    | Double             |


import random
print(random.randint(1,100))
print(random.choice(['apple', 'banana', 'cherry']))

import os #file and the directory access 
print(os.getcwd())
# os.mkdir("test_dir") -> makes the directory 
# fd = os.open("sample.txt", os.O_CREAT | os.O_WRONLY)
# os.close(fd) 
# above lines creates the files 


# high level operations on the collection of files 
import shutil
shutil.copyfile('source.txt', 'destination.txt')
# u need to create the source.txt then you will be getting the destination.txt with the same contents 


# data serialiszation 
import json

data = {
    "Name": "Kedareswar",
    "Age": 21,
    "Language": "Telugu",
    "Country": "India"
}

json_str = json.dumps(data)
print(json_str)
# {"Name": "Kedareswar", "Age": 21, "Language": "Telugu", "Country": "India"}
print(type(json_str)) #<class 'str'>

parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data))
# {'Name': 'Kedareswar', 'Age': 21, 'Language': 'Telugu', 'Country': 'India'}
# <class 'dict'>


from datetime import datetime,timedelta

now =datetime.now()
print(now)

yeaterday = now-timedelta(days=1)
print(yeaterday)