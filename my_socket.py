import asyncio
import websockets
from time import sleep

LOGINS = {'q': 'q', 'w': 'w'}
USERS = set()
TMP = {'q': 'q', 'w': 'w'}
LogTmp_list = [1]
LoginTMP_dict = {}

async def addUser(websocket):
    USERS.add(websocket)

async def removeUser(websocket):
    USERS.remove(websocket)

async def reg(message, websocket):
    if len(message) == 0:
        websocket = websocket
    if len(message) == 2:
        if message[0] not in LOGINS.keys() and message[1] != '':
            LOGINS[message[0]] = message[1]
            await asyncio.wait([websocket.send('Вы успешно зарегистрированы!')])
            await asyncio.wait([websocket.send('refresh')])
            return 1
        if message[0] in LOGINS.keys():
            await asyncio.wait([websocket.send('Это имя занято!')])
        else:
            await asyncio.wait([websocket.send('Ошибка!')])


async def lo(message, websocket):
    if len(message) == 0:
        websocket = websocket
    if len(message) == 2 and message[1] != '':
        if LOGINS[message[0]] == message[1]:
            LogTmp_list.append(message[0])
            await asyncio.wait([websocket.send(message[0])])
            print("Логин отправился на сайт")

async def mes(message, websocket):
    if len(message) == 0:
        if LogTmp_list:
            LoginTMP_dict[LogTmp_list[-1]] = websocket
            await asyncio.wait([websocket.send(f'Вы вошли под логином: {LogTmp_list[-1]}')])
        else:
            await asyncio.wait([websocket.send('refresh')])
    if len(message) == 2:
        if message[0] in LoginTMP_dict.keys():
            for key, value in LoginTMP_dict.items():
                if websocket == value:
                    await asyncio.wait([websocket.send(f'Вы отправили сообщение {message[0]}: {message[1]}')])
                    await asyncio.wait([LoginTMP_dict[message[0]].send(f'{key} отправил Вам сообщение: {message[1]}')])
        else:
            await asyncio.wait([websocket.send('Ошибка! Нет такого получателя!!')])
    LogTmp_list.clear()

async def socket(websocket, path):
    await addUser(websocket)
    print(websocket)
    try:
        while True:
            message = await websocket.recv()
            message = list(message.split(';'))
            print(message)
            if 'reg_user_new' in message[0]:
                message.pop(0)
                await reg(message, websocket)
                continue
            if 'login_user' in message[0]:
                message.pop(0)
                await lo(message, websocket)
                continue
            if 'message_from_user' in message[0]:
                message.pop(0)
                await mes(message, websocket)

    except websockets.exceptions.ConnectionClosedOK:
        print('Соединение закрыто...')
    finally:
        await removeUser(websocket)


start_server = websockets.serve(socket, '127.0.0.1', 5678)
print("Норм сервер запустился")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
