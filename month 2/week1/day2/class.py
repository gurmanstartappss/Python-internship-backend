# mode=r,w,x,a

# r+ MODE
# If file EXISTS     -> opens for both reading and writing
# If file NOT EXISTS -> ERROR (FileNotFoundError)
# Does NOT delete old content automatically

with open("demo.txt", "r+") as file:
    data1 = file.read()
    print(data1)

    file.seek(0)          # move cursor to index 0
    file.write("demo\n")  # write from index 0

    data2 = file.read()
    print(data2)


print("----------------------------------")


# w+ MODE
# If file EXISTS     -> opens for reading and writing
#                       BUT deletes all old content first
# If file NOT EXISTS -> creates a new file
# Supports both reading and writing

with open("demo.txt", "w+") as file:
    file.write("demo\n")

    file.seek(0)          # move cursor back to index 0

    data = file.read()
    print(data)
    

# rb MODE=read binary files like images,pdf,videos
# r  = read
# b  = binary
#
# If file EXISTS     -> opens for reading
# If file NOT EXISTS -> ERROR (FileNotFoundError)
# Cannot write
# Returns data as bytes

with open("demo.txt", "rb") as file:
    data = file.read()
    print(data)
    
# ==================================================
# wb MODE
# ==================================================
# w = write
# b = binary
#
# If file EXISTS     -> opens the file and DELETES old content
# If file NOT EXISTS -> creates a new file
# Can write only
# Cannot read
# Must write data as BYTES

with open("demo.txt", "wb") as file:
    file.write(b"Hello\n")
    file.write(b"Gurman")
    
    
#csv-comma seperated file, saves data seperated by commas
import csv

data = [
    ["ID", "Name", "City"],       # header
    [1, "Gurman", "Indore"],      # student 1
    [2, "Avantika", "Badwani"]    # student 2
]

with open("students.csv", "w", newline="") as file: #w rewrites the file and creates a file if not exists
    writer = csv.writer(file)
    writer.writerows(data)
    
with open("students.csv", "r") as file:# used to read the data in csv that we are adding
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
# with open("employee.csv", "w", newline="") as file:
#     fields = ["ID", "Name", "City", "Salary"]
#     writer = csv.DictWriter(file, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(data)

# JSON : JavaScript Object Notation
# json module converts Python objects into JSON format
# or converts JSON format back into Python objects
import json
student={
    "id":1,
    "name":"demo",
    "city":"indore",
}
with open("student.json","w") as file:
    json.dump(student,file)#json takes two arguments 


with open("student.json", "r") as file:# Open student.json file in read mode
    data = json.load(file)# JSON file -> Python dictionary
    print(data["city"])# Print city value
    
    
    
#nested dict
import json

student = {
    "xyz": {
        "id": 1,
        "name": "demo",
        "city": "indore"
    }
}

# Python object -> JSON file
with open("students.json", "w") as file:
    json.dump(student, file)


# JSON file -> Python object
with open("students.json", "r") as file:
    data = json.load(file)

    # First access "xyz", then access "city"
    print(data["xyz"]["city"])
    

"""
pickle module:-serialisation

"""