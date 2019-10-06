from telethon import TelegramClient, sync
import xlsxwriter
import time

print("Hello world")
api_id = 1005783
api_hash = '09cb354a26d71b92d9c12e06a7760732'
phone = '+380635362036'
client = TelegramClient(phone, api_id, api_hash).start()

groups = []
for dialog in client.iter_dialogs():#выводит список диалогов
    if len(str(dialog.id)) <= 14:
        groups.append(dialog)
i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1
#pyinstaller -F -w Stat_bot.py
your_choice = input("Введите номер интересующей группы : " ) #записывает в файл данные пользователей, могут быть пропуски из за кодировки в именах
g = groups[int(your_choice)]
f = open("{}.xlsx".format(g.title), "a+")
time.sleep(1)
f.close()
workbook = xlsxwriter.Workbook('{}.xlsx'.format(g.title))
worksheet = workbook.add_worksheet("My sheet")
row = 0
col = 0
for user in client.iter_participants(entity=groups[int(your_choice)]):
        g = groups[int(your_choice)]
        worksheet.write(row, col, user.first_name)
        worksheet.write(row, col + 1, user.last_name)
        worksheet.write(row, col + 2, user.phone)
        worksheet.write(row, col + 3, user.username)
        row += 1
        print(user.phone, user.first_name, user.last_name, '@{}'.format(user.username))

workbook.close()




