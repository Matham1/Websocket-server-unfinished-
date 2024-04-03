import asyncio
import websockets
import keyboard

# start the websocket client
async def start_client():
    async with websockets.connect('ws://192.168.104.83:8888/?token=${token}') as websocket:
        # await websocket.send('{"Car"}')
        while True:
            try:
                t = await websocket.recv()
                print("Moving in the x direction {}".format(t))
            except websockets.exceptions.ConnectionClosedOK:
                print("Client connection closed")
# run the clien
asyncio.run(start_client())