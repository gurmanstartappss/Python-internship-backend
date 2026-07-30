# """
# Enum: It is a class used to define a collection of fixed constant values.
# It makes code more readable, safe, and easy to maintain.
# """

# from enum import Enum, Flag, auto


# # Enum Example
# class Role(Enum):
#     ADMIN = "admin"


# class Status(Enum):
#     ACTIVE = 1
#     INACTIVE = 2
#     ON_LEAVE = 3


# print(Status.ACTIVE.name)   # ACTIVE


# """
# Flag:
# A special type of Enum that allows multiple constant values
# to be combined using bitwise operators.
# used for file permissions api permissions 
# """


# class Permission(Flag):
#     READ = auto()       # 001 (1)
#     WRITE = auto()      # 010 (2)
#     EXECUTE = auto()    # 100 (4)


# # Give user READ and WRITE permissions
# user = Permission.READ | Permission.WRITE

# print(user)

# # Check permissions
# if Permission.WRITE in user:
#     print("Write Allowed")

# user = user^Permission.READ
# print(user)

"""date time: used for handling date and time"""
from datetime import datetime,date 
now=datetime.now()
print(now)
now=date.today()
print(now)

"""dateutil: used fdor parsing flexible date formats"""
from dateutil.parser import parse
d=parse("26 july 2026 4pm")
print(d)

#pytz=oldest library and now-a-days we use 
# zoneinfo- newest library
from datetime import datetime
from zoneinfo import ZoneInfo #OR
import pytz
Japan=datetime.now(ZoneInfo("Asia/Tokyo"))
print(Japan)

Japan=pytz.timezone("Asia/Tokyo")
print(datetime.now(Japan))

# Idiomatic Python: Write Python in a Pythonic way
num = [i for i in range(5)]

# print(num)
if not num:
    print("Empty")
else:
    print("Not Empty")
    
# Vulnerability:
# A vulnerability is a weakness or flaw in software, hardware,
# or a system that attackers can exploit to gain unauthorized
# access, steal data, or cause damage.