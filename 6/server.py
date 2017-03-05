#!/usr/bin/python3

import asyncio
import websockets
import time

def forward():
	print("moving forward...")
	time.sleep(1)

def backward():
	print("moving backward...")
	time.sleep(1)

async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))

    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))

start_server = websockets.serve(hello, 'localhost', 1980)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
