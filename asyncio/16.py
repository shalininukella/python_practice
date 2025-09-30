import asyncio

counter = 0

async def increment():
    global counter
    for _ in range(10):
        print(counter)
        counter += 1
        asyncio.sleep(1)


async def main():
    await asyncio.gather(increment(), increment())
    print("Counter:", counter)

asyncio.run(main())

#explanation is python-2 asyncio folder in output based folder 

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# Counter: 20