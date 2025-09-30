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
    print("before scheduling the task")
    task = asyncio.create_task(func1())
    await asyncio.sleep(1)  # Let func1 start
    print("after sleep and before cancelling the task")
    task.cancel()
    print("after cancelling,it will raise the error in the task1")
    await task

asyncio.run(main())

# before scheduling the task
# Func1 started
# after sleep and before cancelling the task
# after cancelling,it will raise the error in the task1
# Func1 was cancelled!
# Func1 cleanup!