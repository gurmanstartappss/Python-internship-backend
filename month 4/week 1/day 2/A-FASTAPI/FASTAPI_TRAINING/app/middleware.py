import time
from fastapi import Request

async def log_request(request: Request, call_next,):
    start_time = time.time()
    print(f"Request:{request.method} {request.url.path}")

    response = call_next(request)

    duration = await time.time() - start_time

    print(f"Response:{response.status_code}"
        f"Response:{duration: .4f}s")
    return response