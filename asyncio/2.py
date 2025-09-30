import asyncio

async def func1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def func2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    await task1
    await task2

asyncio.run(main())


# Task 1 started
# Task 2 started
# Task 2 finished
# Task 1 finished