import asyncio


async def func1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")
    return 1


async def func2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")
    return 2


async def main():
    results = await asyncio.gather(func1(), func2())
    print("Results:", results)


asyncio.run(main())


# Task 1 started
# Task 2 started
# Task 1 finished
# Task 2 finished
# Results: [1, 2]