import asyncio

async def func1():
    print("Func1 started")
    await asyncio.sleep(3)
    print("Func1 stopped")

async def main():
  print("Main")
  task = asyncio.create_task(func1())
  await task
  print("Main Stopped")
  await asyncio.sleep(1)
  
asyncio.run(main())

#have the explanation in the docs - python-2
#refer 9.py as well
