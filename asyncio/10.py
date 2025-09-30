import asyncio


async def async_generator():
    for i in range(5):
        await asyncio.sleep(5)
        yield i


async def main():
    async for value in async_generator():
        print("Received:", value)


asyncio.run(main())
