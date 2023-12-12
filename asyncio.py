import asyncio

async def drawing():
    while True:
        await asyncio.sleep(1)
        print("_______________👤__________________")

async def backend_operations():
    while True:
        await asyncio.sleep(1)
        print("fetching...")

async def game():
    # or await asyncio.gather(drawing(), backend_operations()) if you dont need to keep an individual reference
    task1 = asyncio.create_task(drawing())
    task2 = asyncio.create_task(backend_operations())
    await asyncio.sleep(2)
    
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    asyncio.run(game())
