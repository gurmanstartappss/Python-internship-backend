#performance profile:- performance profile is the process
#of measuring where a program spends its execution time and memory

#optimization:- it is the process of improving the speed and efficiency of the code

"""
1. cprofile:- it is pythons built-in profiler that measures how much time each
function takes during program execution, cprofile is for time
2. line_profiler:- it measures execution time line by line inside a function 
pip istall line profile- 
"""
# import cProfile
# def square():
#     total=0
#     for i in range(100000):
#         total+=i*i
#     print(total)
# cProfile.run("square()")


# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# cProfile.run("print(factorial(10))")

from line_profiler import profile

@profile
def square():
    total = 0
    for i in range(100000):
        total += i * i
    return total
n = square()
print(n)
# kernprof -l -v file.py--to run the file
#hits:- total number of time that line hit
#time: total execution time spent on that line
#per hit: average time spnt per execution of the line
#time:- time percentage of the total function's line
#line contents:- code of perticular time


#py-spy-it is an external profiler that can inspect a running
#python program without modifying its source code


# pip3 install py-spy
#uv pip install --system py-spy
#uv pip install --system line_profiler -cause in this uv path is used not normal path
#py-spy record -o profile.svg -- python my_script.py

# def square():
#     total=0
#     for i in range(100000):
#         total +=i*i
#     return total
# n=square()
# print(n)
"""import sys
print(sys.executable)"""

import time

def fast_fun():
    time.sleep(0.01)

def slow_bottleneck_function():
    total = 0
    for i in range(10000000):
        total += i
    return total

def main():
    print("start program")
    while True:
        fast_fun()
        slow_bottleneck_function()

if __name__ == "__main__":
    main()