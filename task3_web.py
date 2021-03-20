import asyncio
import websockets
import json

from task3 import appearance


async def socket(websocket, path):
    print(websocket)
    try:
        while True:
            message = await websocket.recv()
            a = ' '.join(message.split()).replace("'", '"')
            decoded = json.loads(a)
            print(appearance(decoded))
            await asyncio.wait([websocket.send(str(appearance(decoded)))])
    except websockets.exceptions.ConnectionClosedOK:
        print('Соединение закрыто...')


start_server = websockets.serve(socket, '127.0.0.1', 5678)
print("Сервер запустился")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
