# import time 

# class Timer:
#     def __enter__(self):
#         self.start=time.time()
#         print("Time Started ")
#         return self
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         end=time.time()
#         print(f"Time Taken: {end - self.start} seconds")
        
# with Timer():
#     time.sleep(10)
    
# class Database:
#     def __enter__(self):
#         print("Database Connected")
#         return self

#     def query(self):
#         print("Executing Query")

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Database Closed")
#         return True


# with Database() as db:
#     db.query()      # exc_type = None
#     print(10 / 0)
    
"""# context lib=dont have to create a class just have to use decorator
# just have to import from contextlib and create a decorator and use the with keyword and yield """

# from contextlib import contextmanager
# @contextmanager
# def database():
#     print("connect")  # represents enter method
#     try:
#         yield  # represents the with data
#         print("Done ")# represents exit method
#     except Exception:
#         print("Disconnect")# if risky code has a exception then this runs

# with database() as db:
#     print(10/0)
#     print("HI")

"""stack=LIFO(last in first out)"""

# class Database:
#     def __enter__(self):
#         print("Database Connected")
#         return self

#     def query(self):
#         print("Query Executed")

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Database Closed")


# class Demo:
#     def __enter__(self):
#         print("Demo Connected")
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Demo Closed")


# with Database() as db ,Demo():
#     db.query()
#     print("hello")

"""EXITStack=sometimes you dont know how many resources you will need until runtime"""
# from contextlib import ExitStack
# files=["student.txt","student1.txt","student2.txt","student3.txt"]

# with ExitStack() as stack:
#     opened=[]
#     for file in files:
#         opened.append(stack.enter_context(open(file)))
        
#     for f in opened:
#         print(f.read())

"""
# asyncio-python's inbuilt lib for writing concurrent asynchronous programs
# async and await 2 keywords used in asynchronous 
# await=pause here until this asynchronous task is finished
# create coroutine objects of async functions, run that function
# time.sleep()=blocks the thread 
# 
"""
import asyncio
async def download():
    print("downloading ")
    await asyncio.sleep(3)
    print("finished")
    
asyncio.run(download())# this object is coroutine object and download is asynchronous
