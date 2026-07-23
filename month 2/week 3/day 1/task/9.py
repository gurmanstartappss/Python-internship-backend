from collections import namedtuple
Student=namedtuple("Student","ID, Name , Salary")
s=Student(101,"gurman",100000)
s2=Student(101,"gurman",645345)
s3=Student(101,"gurman",657)
s4=Student(101,"gurman",678)

listt=[s,s4,s2,s3]

for i in listt:
    if i.Salary<50000:listt.remove(i)
print(listt)
        
