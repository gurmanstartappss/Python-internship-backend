import time
from fastapi import Request


async def log_request(request: Request, call_next):
    start_time = time.time()

    print(f"Request: {request.method} {request.url.path}")

    response = await call_next(request)
    duration = time.time() - start_time

    print(f"Response: {response.status_code}")
    print(f"Duration: {duration:.4f}s")

    return response