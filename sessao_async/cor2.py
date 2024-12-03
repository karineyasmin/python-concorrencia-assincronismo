import asyncio


async def diz_oi_demorado():
    print("Olá...")
    await asyncio.sleep(2)                                                       
    print("a todos...")


asyncio.run(diz_oi_demorado())
