import asyncio


async def func1():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


asyncio.run(func1())


# Hello
# World