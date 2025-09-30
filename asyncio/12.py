# nested async function

import asyncio

async def inner():
    print("Inner started")
    await asyncio.sleep(1)
    print("Inner finished")

async def outer():
    print("Outer started")
    await inner()
    print("Outer finished")

asyncio.run(outer())

# Outer started
# Inner started
# Inner finished
# Outer finished