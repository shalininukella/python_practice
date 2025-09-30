import asyncio


async def func1():
    print("Func1 started")
    await asyncio.sleep(1)
    raise ValueError("Something went wrong in func1!")


async def func2():
    print("Func2 started")
    await asyncio.sleep(2)
    print("Func2 finished")


async def main():
    try:
        await asyncio.gather(func1(), func2())
    except Exception as e:
        print("Caught an exception:", e)


asyncio.run(main())


# Func1 started
# Func2 started
# Caught an exception: Something went wrong in func1!