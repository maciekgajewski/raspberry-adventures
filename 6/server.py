#!/usr/bin/python3

import asyncio
import websockets
import time
import json

def forward():
	print("moving forward...")
	time.sleep(1)

def backward():
	print("moving backward...")
	time.sleep(1)

def process_command(cmd):
	t = cmd['type']
	if (t == 'command'):
		c = cmd['command']
		if c == 'forward':
			forward()
		elif c == 'backward':
			backward()
		else:
			raise RuntimeError('unknown command')
	else:
		raise RuntimeError('unknown type')

@asyncio.coroutine
def server_loop(websocket, path):
	while True:
		print('receiving...')
		encoded = yield from websocket.recv()
		decoded = json.loads(encoded)
		print('>>>: {}'.format(encoded))	
		reply = {'result' : 'OK' }
		try:
			process_command(decoded)
		except Exception as e:
			reply = {'result' : 'error', 'msg' : str(e)}
			
		encoded_reply = json.dumps(reply)
		yield from websocket.send(encoded_reply)

start_server = websockets.serve(server_loop, 'localhost', 1980)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
