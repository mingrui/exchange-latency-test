import time
import asyncio
import websockets

var = []

async def bitmex_test():
    async with websockets.connect('wss://www.bitmex.com/realtime') as websocket:
        response = await websocket.recv()
        print(response)

        await websocket.send("ping")
        ping_time = time.time()
        response = await websocket.recv()
        pong_time = time.time()
        var.append(f'bitmex ping pong time: {(pong_time - ping_time)*1000.0} ms')


async def okex_test():
    async with websockets.connect('wss://real.okex.com:8443/ws/v3') as websocket:
        await websocket.send("ping")
        ping_time = time.time()
        response = await websocket.recv()
        pong_time = time.time()
        var.append(f'okex ping pong time: {(pong_time - ping_time)*1000.0} ms')

async def huobi_test():
    async with websockets.connect('wss://api-aws.huobi.pro/ws') as websocket:
        await websocket.send("ping")
        ping_time = time.time()
        response = await websocket.recv()
        pong_time = time.time()
        var.append(f'huobi ping pong time: {(pong_time - ping_time)*1000.0} ms')


asyncio.get_event_loop().run_until_complete(bitmex_test())
asyncio.get_event_loop().run_until_complete(okex_test())
asyncio.get_event_loop().run_until_complete(huobi_test())

print(var)