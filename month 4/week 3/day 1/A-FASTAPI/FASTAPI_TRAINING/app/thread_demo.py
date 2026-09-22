"""multithreading"""
# import threading
# import time

# def demo(name):
#     print(f"{name} started")
#     time.sleep(2)
#     print(f"{name} finished")

# thread1 = threading.Thread(target=demo, args=("Thread-1",))
# thread2 = threading.Thread(target=demo, args=("Thread-2",))
# thread3 = threading.Thread(target=demo, args=("Thread-3",))

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()

# print("main thread finished")


# from concurrent.futures import ThreadPoolExecutor
# import time

# def demo(n):
#     print(f"Task {n}")
#     time.sleep(2)
#     return f"Task finished {n}"


# numbers = [1, 2, 3, 4, 5, 6]

# with ThreadPoolExecutor(max_workers=3) as executor:
#     result = executor.map(demo, numbers)

#     for res in result:
#         print(res)


"""multiprocessing"""
# from multiprocessing import Process

# def calculate(number):
#     result = number * number
#     print(f"Square of {number} is {result}")


# processes = []

# for number in range(1, 6):
#     process = Process(target=calculate, args=(number,))
    
    
# from concurrent.futures import ProcessPoolExecutor
# import time

# def demo(n):
#     print(f"Task {n}")
#     time.sleep(2)
#     return f"Task finished {n}"


# numbers = [1, 2, 3, 4, 5, 6]

# with ProcessPoolExecutor(max_workers=3) as executor:
#     result = executor.map(demo, numbers)

#     for res in result:
#         print(res)