from telethon import TelegramClient, events

api_id = 6941358
api_hash = 'c8163e8dd5c243d9da0243f72f89f2ba'

client = TelegramClient('anon',api_id,api_hash)

@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()
    chat_id = event.chat_id
    msg = event.raw_text
    print("{} {}".format(chat_id,msg))

    if chat_id == -1001434119736:
        await client.send_message(-1001427784468,event.raw_text)


# Covi Alerts(Pune) = -1001434119736           1434119736
#Demo = -1001386976928                 1386976928
#Receiver group = -1001427784468       1427784468
#U45 Dose 1 Pune = -1001458398949
client.start()
client.run_until_disconnected()