"""if we dont use asyncio"""
# import time
# def student():
#     print("studying")
#     time.sleep(5)
#     print("done study")
    
# def employee():
#     print("working")
#     time.sleep(5)
#     print("work done")
    
# student()
# employee()

# import asyncio
# async def student():
#     print("studying")
#     await asyncio.sleep(5)
#     print("done study")
    
# async def employee():
#     print("working")
#     await asyncio.sleep(5)
#     print("work done")

# async def main():
#     await asyncio.gather(
#     student(),employee())

# asyncio.run(main())


# async: declare an asynchronous function, create coroutine
# await: wait for an asynchronous operation to finish, pause the current coroutine
# await is executed when as task is remaining
# 1. Task Cancellation
# cancel the task.

# import asyncio

# async def upload_video():
#     print("Upload started")
#     try:
#         for i in range(10):
#             print(f"Uploading... {i+1}")
#             await asyncio.sleep(1)

#         print("Done upload")
#     except asyncio.CancelledError:
#         print("Upload cancelled!")
#         raise

# async def main():
#     task = asyncio.create_task(upload_video())
#     await asyncio.sleep(3)   # Let the upload run for 3 seconds
#     print("User clicked cancel")
#     task.cancel()            # Cancel the task

#     try:
#         await task
#     except asyncio.CancelledError:
#         print("Task cancellation confirmed.")

"""
asyncio.run(main()) # it is main task and upload video() working in the background
this pattern usage is :-
stop file upload
cancelpayment request
cancel api request

2) async queue:- works on basis of first in first out
usage:-restaurant food
# """
# import asyncio

# async def customer(queue):
#     for i in range(1, 6):
#         print(f"Customer Ordered {i}")
#         await queue.put(i)
#         await asyncio.sleep(1)

#     # Signal that no more orders are coming
#     await queue.put(None)

# async def chef(queue):
#     print("Chef is working...")

#     while True:
#         order = await queue.get()
#         if order is None:
#             break

#         print(f"Preparing order {order}")
#         await asyncio.sleep(3)
#         print(f"Order {order} completed")

#     print("Chef done with all orders.")

# async def main():
#     queue = asyncio.Queue()

#     await asyncio.gather(
#         customer(queue),
#         chef(queue)
#     )

# asyncio.run(main())

import asyncio

async def api(name):
    print(name,"started")
    await asyncio.sleep(2)
    if name=="API-1":
        raise Exception("server error")
    print(name,"completed")
    return name
async def main():
    task=[
        api("API-1"),
        api("API-2"),
        api("API-3")
    ]
    result = await asyncio.gather(
        *task,
        return_exceptions=True
    )
    print("result")
    for i in result:
        print(i)
    
asyncio.run(main())
"""
asyncio completed

Enum=it is a class used to define a collection of fixed constant value.it mak  es code more readable safe and easy
"""
from enum import Enum
class Role(Enum):
    ADMIN = "admin"
    
class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2
    ON_LEAVE = 3
    
print(Status.ACTIVE.name)                         