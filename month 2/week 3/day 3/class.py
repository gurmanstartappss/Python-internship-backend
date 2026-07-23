# # protocol similar to duck typing

# from typing import Protocol

# class Animal(Protocol):
#     def speak(self):
#         pass
    
# class Dog:
#     def speak(self):
#         print("Bark")

#     def demo(self):
#         print("Demo")


# class Cat:
#     def speak(self):
#         print("Meow")


# def make_sound(animal: Animal):
#     animal.demo()


# d = Dog()
# c = Cat()

# make_sound(d)

# # typeDict= specifies which keys should exist and what type their values must be
# from typing import TypedDict
# class Student(TypedDict):
#     id:int
#     name:str
#     marks:float
    
# s:Student={"id":101,"name":"gurman","marks":40.5}
# print(s["id"])

# 3 literal= in different programming language literal means assigning value but in python literal restricts a variable to specific fixed values instead of accepting any string, only predefined values are allowed 
# from typing import Literal
# def traffic_light(color:"""Literal["Red","yellow","green"]"""):
#     print(color)

# traffic_light("Red")

# 4 Generic and TypeVar
# get_int()
# get_str()
# get_float()
# get_item()

# from typing import TypeVar

# T = TypeVar("T")

# def demo(items: list[T]) -> T:
#     return items[0]

# s = demo([0.1, 2, 3, 4, 5])
# print(s)

# # 5 Mypy(static type)=before execution it check the type 
# # type hints dont stop wrong data during execution
# # eg in ide it shows suggestions same in mypy it gives suggestions before execution of the code 


# # 6 Pydantic is a Python library used for data validation and data parsing using type hints. Instead of manually checking whether data is valid, you define a model, and Pydantic validates the input for you.

# from pydantic import BaseModel

# class Student(BaseModel):
#     id: int
#     name: str
#     marks: float

# student = Student(id=20,name="demo",marks=56.0)

# print(student)
