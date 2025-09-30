import asyncio
import time

async def func1():
    print("Func1 started")
    time.sleep(2)  # Blocking call!
    print("Func1 finished")

async def main():
    await func1()

asyncio.run(main())

# Func1 started
# Func1 finished

# due to time.sleep() - it is blocking in nature
# asyncio.sleep() is non Blocking, and allows other tasks to run while one task is sleeping