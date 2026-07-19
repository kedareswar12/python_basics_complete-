# File I/O operations are the files input and the output operations 
# files are useful when we wanted to store the data permanantly instead keeping it  only in the memory 
file = open('notes.txt' , 'r')

content = file.read()
file.readline() # Read one line
file.readlines() 
file.close()

print(content)

file= open('notes.txt', 'a')
file.write("\nHello python I am here \n")
file.close()

print(content)


# 'r' -> read
# 'w' -> write
# 'a' -> pending 
# 'rb'-> read binary File
# 'x' -> creates new file , fials if the file exsists
#'wb' -> write binary

file= open('images.png' , 'rb')
data = file.read()
file.close()


# context managers 
# with -> it automatilcally clases after the file use 

