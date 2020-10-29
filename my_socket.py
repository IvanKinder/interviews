import asyncio
import websockets

LOGINS = {}
USERS = set()
TMP = {}

async def addUser(websocket):
    USERS.add(websocket)

async def removeUser(websocket):
    USERS.remove(websocket)

async def socket(websocket, path):
    await addUser(websocket)
    print(len(USERS), USERS)
    try:
        while True:
            message = await websocket.recv()
            message = list(message.split())
            TMP[message[1]] = websocket
            print(message)
            print(TMP)
            if 'reg_user_new' in message[0]:
                message.pop(0)
                if len(message) == 2:
                    if message[0] not in LOGINS.keys():
                        LOGINS[message[0]] = message[1]
                        await asyncio.wait([websocket.send('Вы успешно зарегистрированы!')])
                    print(LOGINS)
                if len(message) < 2:
                    await asyncio.wait([websocket.send('Ошибка!')])
            if 'login_user' in message[0]:
                message.pop(0)
                if len(message) == 2:
                    if LOGINS[message[0]] == message[1]:
                        await asyncio.wait([websocket.send('y')])
                else:
                    await asyncio.wait([websocket.send('Ошибка!')])
            if 'message_from_user' in message[0]:
                message.pop(0)
                if len(message) == 2:
                    await asyncio.wait([websocket.send(f'{message[0]}: {message[1]}')])
                if len(message) == 1:
                    await asyncio.wait([websocket.send('Ошибка!!! Нет такого получателя...')])
    except websockets.exceptions.ConnectionClosedOK:
        print('Соединение закрыто...')
    finally:
        await removeUser(websocket)




start_server = websockets.serve(socket, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
