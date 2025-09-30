import asyncio


async def func1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")


async def func2():
    print("Task 2 started")
    for i in range(3):
        print(f"Task 2 - Working {i}")
        await asyncio.sleep(0.5)
    print("Task 2 finished")


async def main():
    await asyncio.gather(func1(), func2())


asyncio.run(main())

# Task 1 started
# Task 2 started
# Task 2 - Working 0
# Task 2 - Working 1
# Task 1 finished
# Task 2 - Working 2
# Task 2 finished
