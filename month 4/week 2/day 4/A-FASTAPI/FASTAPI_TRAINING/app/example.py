import httpx
import asyncio

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response= await client.get("https://jsonplaceholder.typicode.com/todos/1")
        return response.json()
    
print(asyncio.run(fetch_data()))