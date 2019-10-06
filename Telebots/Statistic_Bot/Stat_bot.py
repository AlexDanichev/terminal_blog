from telethon import TelegramClient, sync
import xlsxwriter

print("Hello world")
api_id = 1005783
api_hash = '09cb354a26d71b92d9c12e06a7760732'

client = TelegramClient('xxx', api_id, api_hash).start()

groups = []
for dialog in client.iter_dialogs():#выводит список диалогов
    if len(str(dialog.id)) <= 14:
        groups.append(dialog)
i = 0
for g in groups:
    print(str(i) + '- ' + g.title + str(g.id))
    i += 1
#pyinstaller -F -w Stat_bot.py
your_choice = input("Введите номер интересующей группы : " ) #записывает в файл данные пользователей, могут быть пропуски из за кодировки в именах
for user in client.iter_participants(entity=groups[int(your_choice)]):
    try:
        g = groups[int(your_choice)]
        print(user.phone,user.first_name, user.last_name,'@{}'.format(user.username))
        f = open("{}.txt".format(g.title), "a+")
        f.write("\n Phone " + str(user.phone) + "\nFirst Name: " + str(user.first_name) + "\nLast Name: " + str(
        user.last_name) + "\n Nick Name:  " + str('@{}'.format(user.username)))
    except:
        continue




