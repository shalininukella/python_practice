import asyncio


async def func1():
    print("Func1 started")
    try:
        await asyncio.sleep(3)
    except asyncio.CancelledError:
        print("Func1 was cancelled!")
    finally:
        print("Func1 cleanup!")


async def main():
    task = asyncio.create_task(func1())
    await asyncio.sleep(1)  # Let func1 start
    task.cancel()
    await task


asyncio.run(main())


# Func1 started
# Func1 was cancelled!
# Func1 cleanup!

#have the explanation in the docs - python-2