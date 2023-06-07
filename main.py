from telethon import TelegramClient, events
from face_detection import face_detection
from chat_gpt import chat_gpt
import os

import time

api_id = 3005154
api_hash = '30eccfd99accf1199ae25f0dad3ff5ce'
chat = "syamsul95"
client = TelegramClient('telegram_gpt', api_id, api_hash)
client.start()
@client.on(events.NewMessage)
async def handle_new_message(event):
    print("======> start aplikasi <======")
    print(event.message.text)
    print(event.message)
    # user = str(event.message.from_id)
    # id_user = user.split("=")[1].replace(")","")
    # print(id_user)
    # username = await client.get_entity(int(id_user))
    # # send message
    # await client.send_message(username.username, "Photo Lagi Di Proses Mohon Tunggu")
    
    # download file photo
    if event.message.photo:
        await event.message.download_media('photo')
    # send message
    await event.message.reply("Photo Lagi Di Proses Mohon Tunggu")
    chat = face_detection()

    for i in chat.split("\n"):
        if "surprise" in i:
            data = i.split(":")
            if "POSSIBLE" in data[1]:
                await event.message.reply("😲")
                await event.message.reply(chat_gpt("terkejut"))
                break
            # await event.message.reply(chat_gpt("terkejut"))
            return
        elif "joy: POSSIBLE" in i:
            await event.message.reply("😄")
            return
        elif "anger: POSSIBLE" in i:
            await event.message.reply("😡")
            return
        
    os.remove("photo.jpg")
    # Make a request to the Completion API
client.run_until_disconnected()

