import asyncio
import websockets
import requests

async def handle_message(websocket):
    try:
        while True:
            websocket.send('{"device"}')
            
            message = await websocket.recv()
            print(message)
            if(message == "Remote"):
                print()
    except websockets.exceptions.ConnectionClosedOK:
        print("Client connection closed")

async def start_server():
    async with websockets.serve(handle_message, "0.0.0.0", 8888):
        print('Websocket Server started')
        await asyncio.Future()
if __name__ == "__main__":
    asyncio.run(start_server())