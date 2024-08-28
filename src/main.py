"""
This script demonstrates how to limit the number of connections and keep-alive connections
using the `httpx.Limits` class. This is useful when you want to control the number of
concurrent connections to a server.

In this example, we will send 100 requests to the same URL and limit the number of
connections to 5. This means that only 5 requests will be sent concurrently, and the
remaining requests will be queued until a connection becomes available.

To run this script, you need to install the `httpx` library. You can install it using pdm:
    $ pdm add httpx

Then, you can run the script as follows:
    $ pdm run python src/main.py
    
This will send 100 requests to the URL "https://httpbin.org/get" and print the first 20
characters of the response for each request along with the task index.

Note: The URL "https://httpbin.org/get" is a test URL that returns the request data in the
response. You can replace it with any other URL you want to test.

References:
- httpx documentation: https://www.python-httpx.org/
- httpx.Limits: https://www.python-httpx.org/advanced/#limits
- httpx.AsyncClient: https://www.python-httpx.org/async/#asyncclient
- asyncio.gather: https://docs.python.org/3/library/asyncio-task.html#asyncio.gather
- asyncio.create_task: https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task
- asyncio.run: https://docs.python.org/3/library/asyncio-task.html#asyncio.run
"""

import httpx
import asyncio
import time


async def fetch(url: str, index: int, client: httpx.AsyncClient):
    try:
        response = await client.get(url)
        print(f"Task {index}: {response.text[:20]}")  # Print first 20 chars and index
        return response.text
    except httpx.RequestError as e:
        print(f"Task {index}: An error occurred: {e}")
        return None


async def main():
    base_url = "https://httpbin.org/get"
    urls = [base_url for _ in range(100)]  # Generate 100 identical URLs

    # Set limits to control the number of connections
    limits = httpx.Limits(max_connections=5, max_keepalive_connections=50)

    async with httpx.AsyncClient(verify=False, limits=limits) as client:
        start_time = time.time()  # Start time measurement
        tasks = [
            asyncio.create_task(fetch(url, i, client)) for i, url in enumerate(urls)
        ]

        # Await all tasks to complete
        await asyncio.gather(*tasks)

        elapsed_time = time.time() - start_time
        print(f"\nTotal number of requests: {len(urls)}")
        print(f"Time elapsed: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
