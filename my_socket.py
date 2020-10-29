import asyncio
import websockets

LOGINS = {'q': 'q', 'w': 'w'}
USERS = set()
TMP = {'q': 'q', 'w': 'w'}
LogTmp_list = []
LoginTMP_dict = {}

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
            print(message)
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
                        LogTmp_list.append(message[0])
                        await asyncio.wait([websocket.send(message[0])])
                else:
                    await asyncio.wait([websocket.send('Ошибка!')])
            if 'message_from_user' in message[0]:
                if len(message) == 1:
                    if LogTmp_list[-1] not in LoginTMP_dict.keys():
                        LoginTMP_dict[LogTmp_list[-1]] = websocket
                    if LogTmp_list[-1] in LoginTMP_dict.keys() and LoginTMP_dict[LogTmp_list[-1]] != websocket:
                        LoginTMP_dict[LogTmp_list[-2]] = websocket
                    for key, value in LoginTMP_dict.items():
                        if websocket == value:
                            await asyncio.wait([websocket.send(f'Вы вошли под логином: {key}')])
                print(LogTmp_list)
                message.pop(0)
                if len(message) == 2:
                    print(LoginTMP_dict)
                    if message[0] in LoginTMP_dict.keys():
                        await asyncio.wait([LoginTMP_dict[message[0]].send(message[1])])
                    else:
                        await asyncio.wait([websocket.send('Ошибка! Нет такого получателя!!')])
    except websockets.exceptions.ConnectionClosedOK:
        print('Соединение закрыто...')
    finally:
        await removeUser(websocket)




start_server = websockets.serve(socket, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
