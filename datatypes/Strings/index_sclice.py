# immutable -> they usually change the reference in the memory 
chai_type = "chai"
customer_name ="Priya"
print(f"Order for the {customer_name} : {chai_type} ")

chai_desc = "Aromatic and Bold"

# we know the indexing concept right so plese do follow -> indexing is inclusive in python every time add n+1 for clarity

print(f"The first word in the chai_desc: {chai_desc[0:8]}")
print(f"The first word in the chai_desc: {chai_desc[::-1]}")


label_text = "Hi_Kédar"
encoded_lable = label_text.encode("utf-8")
print(f"Non Encoded lable {label_text}")
print(f"Encoded lable : {encoded_lable}")

decoded_lable= encoded_lable.decode("utf-8")
print(f"Decoded lable : {decoded_lable}")

# important methods in python 

Name = "I am kedar"
print(Name.upper())
print(Name.capitalize()) #Makes only the first character into uppercase 
print(Name.title())  # First character of the evrry word capitalise

print("Kedar" in Name)
print(Name.find("kedar"))

# to get rid of spaces 
email = "                  kedareswartiruveedhi@gmail.com       "
print(email.strip())

sentence ="Python is powerful"
words = sentence.split()
# it will split the words through spaces into arrays

# join 
# <thing to join>.join()
print("-".join(words))
# P-y-t-h-o-n- -i-s- -p-o-w-e-r-f-u-l


# raw strings
path = r"/mnt/c/Users/kedar/OneDrive/Documents/Accenture/Kedar/AI_Engineering/Basics_of_python/datatypes/strings"

print(path)

# Escape sequence 
# /n
# /t
# /" <string> /"