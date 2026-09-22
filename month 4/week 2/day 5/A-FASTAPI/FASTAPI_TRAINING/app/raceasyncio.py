import asyncio

counter = 0
lock = asyncio.Lock()

async def increment():
    global counter

    async with lock:
        counter += 1
        print(counter)

    await asyncio.sleep(2)
    return counter

print(counter)