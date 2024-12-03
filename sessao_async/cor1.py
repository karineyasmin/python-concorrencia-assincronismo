import asyncio


async def diz_oi():
    print("Oi...")


# event_loop = asyncio.get_event_loop() # deprecated
asyncio.run(diz_oi())
