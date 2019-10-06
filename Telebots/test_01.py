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

groups = []
for dialog in client.iter_dialogs():#выводит список диалогов
    if len(str(dialog.id)) <= 14:
        groups.append(dialog)
i = 0
for g in groups:
    print(str(i) + '- ' + g.title+ str(g.id))
    i += 1
