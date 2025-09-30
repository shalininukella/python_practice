#solution to avoid race conditions in 14.py

import asyncio

counter = 0
counter_lock = asyncio.Lock()  # Create a lock

async def increment():
    global counter
    for _ in range(1000):
        async with counter_lock:  # Only one task can increment at a time
            counter += 1

async def main():
    await asyncio.gather(increment(), increment())  # Run two increment tasks concurrently
    print("Counter:", counter)

asyncio.run(main())

#explanation is python-2 asyncio folder in output based folder 