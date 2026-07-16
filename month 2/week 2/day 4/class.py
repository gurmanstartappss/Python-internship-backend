result = ""

for word in ["python is easy language"]:
    result += word + ""
print(result)

#string concatinate
result2 = " ".join(["python is easy language"])
print(result2)

#membership test
num=[1,2,3,4]#O(n)
print(5 in num)

num={1,2,3,4,6,3,6,7,3,2,6,7} #O(1) because set uses hash tables
print(3 in num)

marks={
    100:90,
    101:88,
    102:87
}
student={100,101,102,103}
for stu in student:
    for key,value in marks.items():
        if student==key:
            print(f"student")
            
num = (i*i for i in range(1, 11))

print(sum(num))   # 385
print(sum(num))   # 0

#recursion fibonacci
# from functools import lru_cache#

# @lru_cache(maxsize=None)#least recently used one is removed
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# for i in range(10):
#     print(fib(i), end=" ")
    
from functools import cache

@cache
def square(n):
    return n * n

print(square(5))

#pyproject.toml: is the standard configuration all projects configurations are in this 
# #it stores metadata, dependencies and tool configuration
# virtual Environment
#dependency management-it is the process of installing updating removing and locking the versions of external libraries used in a project like mentioning the project requirements
# poetry just like a virtual env it manages package management and virtual env
# pip install poetry