# file handling: File handling allows python programs to store data
# permanently in files instead of keeping it only in memory

# open() function: it is used to open file for
# reading, writing or modifying its contents.

# file_name = open(filename, mode)

#modes:-
# r  : read
# w  : write
# a  : append data
# x  : create file
# rb : read for binary
# wb : write for binary

# to read a file 1st 
file = open("student.txt", "r")# open file
content = file.read(5)#read file
print(content)
print(file.read(8))#read in chunks and specific characters read
file.close()
print("1---------------------------------------")

#to write in a file 
# file = open("student.txt", "a") # open
# file.write("\npython demo")# write
# print(content)
# file.close()
# print("---------------------------------------")


# to read line by line to occupy less space in memory
file = open("student.txt", "r") # open
content=file.readlines()#readline / readlines
print(content)
file.close()
print("2---------------------------------------")


#
file = open("student.txt", "r") # open
lines=file.readlines()#readline / readlines
print(lines[2])#to acccess line number through indexing 
file.close()
print("3---------------------------------------")


#reading lines through loops 
file = open("student.txt", "r") # open
for line in file:
    print(line)
print("4---------------------------------------")


file = open("student.txt", "r")
print(file.tell())
file.read(5)# read 5 characters so cursor at o
print(file.tell())#return current position of currsor
file.close()
print("5---------------------------------------")


# read()- read entire file or specific characters (number of characters)
# readline- used to read line one by one
# readlines- used to read all lines and return as a list

#add paridhi to the file
file = open("students.txt", "w")
file.write("paridhi")
file.close()
print("6---------------------------------------")


#add multiple line from a lists(any iterable is possible)
data=["avantika\n","gurman\n","pranjali\n","druv\n"]
file = open("students.txt", "w")
file.writelines(data)
file.close()
print("7---------------------------------------")


#
# readlines() : reads all lines and return them as a list of strings

employees = {
    "paridhi": 50000,
    "avantika": 60000,
    "pranjali": 60000,
    "arya": 40000,
}

file = open("student.txt", "w")

for emp, salary in employees.items():
    file.write(f"{emp}: {salary}\n")

file.close()
print("8---------------------------------------")

# x : use for create new file (if not exist)
# w : use for write data, and also create file, if file not exist(overwrites  content)
# a : append data in the file and file not exist, its create file and append data

file = open("students.txt", "w")
file.write("jbhgvfxdkdhfigju")

# context manager:-auto handles opening and  closing the file and when any exception occurs then context manager handles that errors.no need to call close()
#either use finally to close the file or use with 
#dunder methods are used in this __enter__ and __exit__

    
try:
    with open("students.txt", "r") as file:
        data = file.read()
    print(data)
finally:
    print(file.closed)
    
# Handling Large Files (10GB): read line by line
# readline()

#(read(1024))----- reading chunks 