import asyncio

counter = 0

async def increment():
    global counter
    for _ in range(1000):
        counter += 1

async def main():
    await asyncio.gather(increment(), increment())
    print("Counter:", counter)

asyncio.run(main())

#causes race condition
